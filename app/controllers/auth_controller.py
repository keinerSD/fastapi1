import psycopg2
from fastapi import HTTPException
from app.config.db_config import get_db_connection
from app.models.auth_model import Login, Register
from app.utils.jwt_utils import hashear_password, verificar_password, crear_token

class AuthController:

    def login(self, datos: Login):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("""
                SELECT u.id_usuario, u.email, u.password, u.id_rol, r.nombre
                FROM usuario u
                INNER JOIN rol r ON u.id_rol = r.id_rol
                WHERE u.email = %s
            """, (datos.email,))

            result = cursor.fetchone()

            if not result:
                raise HTTPException(status_code=401, detail="Credenciales inválidas")

            id_usuario, email, password_hash, id_rol, nombre_rol = result

            if not verificar_password(datos.password, password_hash):
                raise HTTPException(status_code=401, detail="Credenciales inválidas")

            token = crear_token({
                "sub": str(id_usuario),
                "email": email,
                "id_rol": id_rol,
                "rol": nombre_rol
            })

            return {
                "access_token": token,
                "token_type": "bearer",
                "id_usuario": id_usuario,
                "email": email,
                "id_rol": id_rol,
                "rol": nombre_rol
            }

        except psycopg2.Error as err:
            print(err)
            if conn:
                conn.rollback()
            raise HTTPException(status_code=500, detail="Error en el servidor")

        finally:
            if conn:
                conn.close()

    def register(self, datos: Register):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT id_usuario FROM usuario WHERE email = %s", (datos.email,))
            if cursor.fetchone():
                raise HTTPException(status_code=400, detail="El usuario ya existe")

            password_hash = hashear_password(datos.password)

            cursor.execute("""
                INSERT INTO usuario (primer_nombre, primer_apellido, email, password)
                VALUES (%s, %s, %s, %s)
            """, (datos.primer_nombre, datos.primer_apellido, datos.email, password_hash))

            conn.commit()
            return {"resultado": "Registro exitoso"}

        except psycopg2.Error as err:
            print(err)
            if conn:
                conn.rollback()
            raise HTTPException(status_code=500, detail="Error en el servidor")

        finally:
            if conn:
                conn.close()
