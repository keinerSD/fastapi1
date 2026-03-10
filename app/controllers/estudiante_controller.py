import psycopg2
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from app.config.db_config import get_db_connection
from app.models.estudiante_model import Estudiante


class EstudianteController:

    def create_estudiante(self, estudiante: Estudiante):

        conn = None

        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                """INSERT INTO estudiante
                (matricula, nombre, apellido, fecha_nacimiento, genero, telefono, email, direccion)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s)""",
                (
                    estudiante.matricula,
                    estudiante.nombre,
                    estudiante.apellido,
                    estudiante.fecha_nacimiento,
                    estudiante.genero,
                    estudiante.telefono,
                    estudiante.email,
                    estudiante.direccion
                )
            )

            conn.commit()

            return {"resultado": "Estudiante creado correctamente"}

        except psycopg2.Error as err:

            if conn:
                conn.rollback()

            raise HTTPException(status_code=500, detail=str(err))

        finally:

            if conn:
                conn.close()


    def get_estudiante(self, id_estudiante: int):

        conn = None

        try:

            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                "SELECT * FROM estudiante WHERE id_estudiante = %s",
                (id_estudiante,)
            )

            result = cursor.fetchone()

            if not result:
                raise HTTPException(status_code=404, detail="Estudiante no encontrado")

            content = {
                "id_estudiante": result[0],
                "matricula": result[1],
                "nombre": result[2],
                "apellido": result[3],
                "fecha_nacimiento": result[4],
                "genero": result[5],
                "telefono": result[6],
                "email": result[7],
                "direccion": result[8]
            }

            return jsonable_encoder(content)

        except psycopg2.Error as err:

            raise HTTPException(status_code=500, detail=str(err))

        finally:

            if conn:
                conn.close()


    def get_estudiantes(self):

        conn = None

        try:

            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM estudiante")

            result = cursor.fetchall()

            if not result:
                raise HTTPException(status_code=404, detail="Estudiantes no encontrados")

            payload = []

            for data in result:

                payload.append({
                    "id_estudiante": data[0],
                    "matricula": data[1],
                    "nombre": data[2],
                    "apellido": data[3],
                    "fecha_nacimiento": data[4],
                    "genero": data[5],
                    "telefono": data[6],
                    "email": data[7],
                    "direccion": data[8]
                })

            return {"resultado": jsonable_encoder(payload)}

        except psycopg2.Error as err:

            raise HTTPException(status_code=500, detail=str(err))

        finally:

            if conn:
                conn.close()


    def update_estudiante(self, id_estudiante: int, estudiante: Estudiante):

        conn = None

        try:

            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                """UPDATE estudiante SET
                matricula = %s,
                nombre = %s,
                apellido = %s,
                fecha_nacimiento = %s,
                genero = %s,
                telefono = %s,
                email = %s,
                direccion = %s
                WHERE id_estudiante = %s""",
                (
                    estudiante.matricula,
                    estudiante.nombre,
                    estudiante.apellido,
                    estudiante.fecha_nacimiento,
                    estudiante.genero,
                    estudiante.telefono,
                    estudiante.email,
                    estudiante.direccion,
                    id_estudiante
                )
            )

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Estudiante no encontrado")

            conn.commit()

            return {"resultado": "Estudiante actualizado correctamente"}

        except psycopg2.Error as err:

            if conn:
                conn.rollback()

            raise HTTPException(status_code=500, detail=str(err))

        finally:

            if conn:
                conn.close()


    def delete_estudiante(self, id_estudiante: int):

        conn = None

        try:

            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                "DELETE FROM estudiante WHERE id_estudiante = %s",
                (id_estudiante,)
            )

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Estudiante no encontrado")

            conn.commit()

            return {"resultado": f"Estudiante con id {id_estudiante} eliminado correctamente"}

        except psycopg2.Error as err:

            if conn:
                conn.rollback()

            raise HTTPException(status_code=500, detail=str(err))

        finally:

            if conn:
                conn.close()


estudiante_controller = EstudianteController()
