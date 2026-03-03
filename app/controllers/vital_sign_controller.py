import psycopg2
from fastapi import HTTPException
from app.config.db_config import get_db_connection
from app.models.vital_sign_model import VitalSign
from fastapi.encoders import jsonable_encoder

class VitalSignController:

    def create_vital_sign(self, vital_sign: VitalSign):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                """INSERT INTO vital_signs
                (id_query, blood_pressure, temperature, weight, height)
                VALUES (%s, %s, %s, %s, %s)""",
                (
                    vital_sign.id_query,
                    vital_sign.blood_pressure,
                    vital_sign.temperature,
                    vital_sign.weight,
                    vital_sign.height
                )
            )
            conn.commit()
            return {"resultado": "Signos vitales creados correctamente"}
        except psycopg2.Error as err:
            if conn:
                conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn:
                conn.close()

    def get_vital_sign(self, id_signs: int):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM vital_signs WHERE id_signs = %s",
                (id_signs,)
            )
            result = cursor.fetchone()
            if not result:
                raise HTTPException(status_code=404, detail="Vital sign not found")
            content = {
                "id_signs": result[0],
                "id_query": result[1],
                "blood_pressure": result[2],
                "temperature": float(result[3]) if result[3] is not None else None,
                "weight": float(result[4]) if result[4] is not None else None,
                "height": float(result[5]) if result[5] is not None else None
            }
            return jsonable_encoder(content)
        except psycopg2.Error as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn:
                conn.close()

    def get_vital_signs(self):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM vital_signs")
            result = cursor.fetchall()
            if not result:
                raise HTTPException(status_code=404, detail="No vital signs found")
            payload = []
            for data in result:
                payload.append({
                    "id_signs": data[0],
                    "id_query": data[1],
                    "blood_pressure": data[2],
                    "temperature": float(data[3]) if data[3] is not None else None,
                    "weight": float(data[4]) if data[4] is not None else None,
                    "height": float(data[5]) if data[5] is not None else None
                })
            return {"resultado": jsonable_encoder(payload)}
        except psycopg2.Error as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn:
                conn.close()

    def update_vital_sign(self, id_signs: int, vital_sign: VitalSign):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                """UPDATE vital_signs SET
                    id_query = %s,
                    blood_pressure = %s,
                    temperature = %s,
                    weight = %s,
                    height = %s
                   WHERE id_signs = %s""",
                (
                    vital_sign.id_query,
                    vital_sign.blood_pressure,
                    vital_sign.temperature,
                    vital_sign.weight,
                    vital_sign.height,
                    id_signs
                )
            )
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Vital sign not found")
            conn.commit()
            return {"resultado": "Signos vitales actualizados correctamente"}
        except psycopg2.Error as err:
            if conn:
                conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn:
                conn.close()

    def delete_vital_sign(self, id_signs: int):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM vital_signs WHERE id_signs = %s",
                (id_signs,)
            )
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Vital sign not found")
            conn.commit()
            return {"resultado": f"Signo vital con id {id_signs} eliminado correctamente"}
        except psycopg2.Error as err:
            if conn:
                conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn:
                conn.close()

vital_sign_controller = VitalSignController()