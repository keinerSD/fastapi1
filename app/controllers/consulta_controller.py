import psycopg2
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from app.config.db_config import get_db_connection
from app.models.consulta_model import Consulta


class ConsultaController:

    def create_consulta(self, consulta: Consulta):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                """INSERT INTO consulta
                (id_estudiante, id_usuario, diagnostico, observaciones, motivo_consulta, fecha_entrada, fecha_salida)
                VALUES (%s,%s,%s,%s,%s,%s,%s) RETURNING id_consulta""",
                (
                    consulta.id_estudiante,
                    consulta.id_usuario,
                    consulta.diagnostico,
                    consulta.observaciones,
                    consulta.motivo_consulta,
                    consulta.fecha_entrada,
                    consulta.fecha_salida
                )
            )
            id_consulta = cursor.fetchone()[0]
            conn.commit()

            return {"resultado": "Consulta creada correctamente", "id_consulta": id_consulta}

        except psycopg2.Error as err:
            if conn:
                conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))

        finally:
            if conn:
                conn.close()

    def get_consultas(self):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("""
                SELECT 
                    c.id_consulta,
                    c.id_estudiante,
                    c.id_usuario,
                    c.diagnostico,
                    c.observaciones,
                    c.motivo_consulta,
                    c.fecha_entrada,
                    c.fecha_salida,
                    e.primer_nombre,
                    e.primer_apellido,
                    e.numero_identificacion,
                    u.primer_nombre,
                    u.primer_apellido
                FROM consulta c
                INNER JOIN estudiante e ON c.id_estudiante = e.id_estudiante
                INNER JOIN usuario u ON c.id_usuario = u.id_usuario
            """)

            result = cursor.fetchall()
            if not result:
                raise HTTPException(status_code=404, detail="Consultas no encontradas")

            payload = []
            for data in result:
                payload.append({
                    "id_consulta": data[0],
                    "id_estudiante": data[1],
                    "id_usuario": data[2],
                    "diagnostico": data[3],
                    "observaciones": data[4],
                    "motivo_consulta": data[5],
                    "fecha_entrada": data[6],
                    "fecha_salida": data[7],
                    "nombre_estudiante": f"{data[8]} {data[9]}",
                    "cedula": data[10],
                    "nombre_enfermera": f"{data[11]} {data[12]}",
                    "es_emergencia": True if "emergencia" in (data[5] or "").lower() else False
                })

            return {"resultado": jsonable_encoder(payload)}

        except psycopg2.Error as err:
            raise HTTPException(status_code=500, detail=str(err))

        finally:
            if conn:
                conn.close()

    def get_consulta(self, id_consulta: int):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
    
            cursor.execute("""
                SELECT 
                    c.id_consulta,
                    c.id_estudiante,
                    c.id_usuario,
                    c.diagnostico,
                    c.observaciones,
                    c.motivo_consulta,
                    c.fecha_entrada,
                    c.fecha_salida,
                    e.primer_nombre,
                    e.primer_apellido,
                    e.numero_identificacion,
                    u.primer_nombre,
                    u.primer_apellido,
                    sv.presion_arterial,
                    sv.temperatura,
                    sv.peso,
                    sv.altura,
                    sv.saturacion_oxigeno,
                    sv.frecuencia_cardiaca,
                    sv.tipo_sangre
                FROM consulta c
                INNER JOIN estudiante e ON c.id_estudiante = e.id_estudiante
                INNER JOIN usuario u ON c.id_usuario = u.id_usuario
                LEFT JOIN signos_vitales sv ON c.id_consulta = sv.id_consulta
                WHERE c.id_consulta = %s
            """, (id_consulta,))
    
            data = cursor.fetchone()
            if not data:
                raise HTTPException(status_code=404, detail="Consulta no encontrada")
    
            return {
                "resultado": {
                    "id_consulta":        data[0],
                    "id_estudiante":      data[1],
                    "id_usuario":         data[2],
                    "diagnostico":        data[3],
                    "observaciones":      data[4],
                    "motivo_consulta":    data[5],
                    "fecha_entrada":      data[6],
                    "fecha_salida":       data[7],
                    "nombre_estudiante":  f"{data[8]} {data[9]}",
                    "cedula":             data[10],
                    "nombre_enfermera":   f"{data[11]} {data[12]}",
                    "presion_arterial":   data[13],
                    "temperatura":        data[14],
                    "peso":               data[15],
                    "altura":             data[16],
                    "saturacion_oxigeno": data[17],
                    "frecuencia_cardiaca":data[18],
                    "tipo_sangre":        data[19]
                }
            }
    
        except psycopg2.Error as err:
            raise HTTPException(status_code=500, detail=str(err))
    
        finally:
            if conn:
                conn.close()    

    def get_consultas_by_cedula(self, cedula: str):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            query = """
                SELECT
                    c.id_consulta,
                    c.fecha_entrada,
                    c.fecha_salida,
                    c.motivo_consulta,
                    c.diagnostico,
                    c.observaciones,
                    e.primer_nombre,
                    e.primer_apellido
                FROM consulta c
                INNER JOIN estudiante e ON c.id_estudiante = e.id_estudiante
                WHERE e.numero_identificacion = %s
                ORDER BY c.fecha_entrada DESC
            """

            cursor.execute(query, (cedula,))
            rows = cursor.fetchall()

            consultas = []
            for row in rows:
                consultas.append({
                    "id_consulta": row[0],
                    "fecha_entrada": row[1],
                    "fecha_salida": row[2],
                    "motivo_consulta": row[3],
                    "diagnostico": row[4],
                    "observaciones": row[5],
                    "primer_nombre": row[6],
                    "primer_apellido": row[7]
                })

            return consultas

        except Exception:
            raise HTTPException(status_code=500, detail="Error obteniendo consultas")

        finally:
            if conn:
                conn.close()

    def update_consulta(self, id_consulta: int, consulta: Consulta):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                """UPDATE consulta SET
                id_estudiante = %s,
                id_usuario = %s,
                diagnostico = %s,
                observaciones = %s,
                motivo_consulta = %s,
                fecha_entrada = %s,
                fecha_salida = %s
                WHERE id_consulta = %s""",
                (
                    consulta.id_estudiante,
                    consulta.id_usuario,
                    consulta.diagnostico,
                    consulta.observaciones,
                    consulta.motivo_consulta,
                    consulta.fecha_entrada,
                    consulta.fecha_salida,
                    id_consulta
                )
            )

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Consulta no encontrada")

            conn.commit()
            return {"resultado": "Consulta actualizada correctamente"}

        except psycopg2.Error as err:
            if conn:
                conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))

        finally:
            if conn:
                conn.close()

    def delete_consulta(self, id_consulta: int):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("DELETE FROM consulta WHERE id_consulta = %s", (id_consulta,))
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Consulta no encontrada")

            conn.commit()
            return {"resultado": f"Consulta con id {id_consulta} eliminada correctamente"}

        except psycopg2.Error as err:
            if conn:
                conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))

        finally:
            if conn:
                conn.close()

    def get_consultas_estudiante(self, id_estudiante: int):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM consulta WHERE id_estudiante = %s", (id_estudiante,))
            result = cursor.fetchall()

            payload = []
            for data in result:
                payload.append({
                    "id_consulta": data[0],
                    "id_estudiante": data[1],
                    "id_usuario": data[2],
                    "diagnostico": data[3],
                    "observaciones": data[4],
                    "motivo_consulta": data[5],
                    "fecha_entrada": data[6],
                    "fecha_salida": data[7]
                })

            return {"resultado": jsonable_encoder(payload)}

        except psycopg2.Error as err:
            raise HTTPException(status_code=500, detail=str(err))

        finally:
            if conn:
                conn.close()


consulta_controller = ConsultaController()
