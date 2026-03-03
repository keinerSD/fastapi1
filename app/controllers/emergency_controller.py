import psycopg2
from fastapi import HTTPException
from app.config.db_config import get_db_connection
from app.models.emergency_model import Emergency
from fastapi.encoders import jsonable_encoder

class EmergencyController:

    def create_emergency(self, emergency: Emergency):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                """INSERT INTO emergencies
                (id_student, date, descripcion, attention_provided, id_staff)
                VALUES (%s, %s, %s, %s, %s)""",
                (
                    emergency.id_student,
                    emergency.date,
                    emergency.descripcion,
                    emergency.attention_provided,
                    emergency.id_staff
                )
            )
            conn.commit()
            return {"resultado": "Emergencia creada correctamente"}
        except psycopg2.Error as err:
            if conn:
                conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn:
                conn.close()

    def get_emergency(self, id_emergency: int):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM emergencies WHERE id_emergency = %s",
                (id_emergency,)
            )
            result = cursor.fetchone()
            if not result:
                raise HTTPException(status_code=404, detail="Emergency not found")
            content = {
                "id_emergency": result[0],
                "id_student": result[1],
                "date": result[2],
                "descripcion": result[3],
                "attention_provided": result[4],
                "id_staff": result[5]
            }
            return jsonable_encoder(content)
        except psycopg2.Error as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn:
                conn.close()

    def get_emergencies(self):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM emergencies")
            result = cursor.fetchall()
            if not result:
                raise HTTPException(status_code=404, detail="No emergencies found")
            payload = []
            for data in result:
                payload.append({
                    "id_emergency": data[0],
                    "id_student": data[1],
                    "date": data[2],
                    "descripcion": data[3],
                    "attention_provided": data[4],
                    "id_staff": data[5]
                })
            return {"resultado": jsonable_encoder(payload)}
        except psycopg2.Error as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn:
                conn.close()

    def update_emergency(self, id_emergency: int, emergency: Emergency):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                """UPDATE emergencies SET
                    id_student = %s,
                    date = %s,
                    descripcion = %s,
                    attention_provided = %s,
                    id_staff = %s
                   WHERE id_emergency = %s""",
                (
                    emergency.id_student,
                    emergency.date,
                    emergency.descripcion,
                    emergency.attention_provided,
                    emergency.id_staff,
                    id_emergency
                )
            )
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Emergency not found")
            conn.commit()
            return {"resultado": "Emergencia actualizada correctamente"}
        except psycopg2.Error as err:
            if conn:
                conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn:
                conn.close()

    def delete_emergency(self, id_emergency: int):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM emergencies WHERE id_emergency = %s",
                (id_emergency,)
            )
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Emergency not found")
            conn.commit()
            return {"resultado": f"Emergencia con id {id_emergency} eliminada correctamente"}
        except psycopg2.Error as err:
            if conn:
                conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn:
                conn.close()

emergency_controller = EmergencyController()