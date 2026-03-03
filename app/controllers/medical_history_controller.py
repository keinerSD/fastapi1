import psycopg2
from fastapi import HTTPException
from app.config.db_config import get_db_connection
from app.models.medical_history_model import MedicalHistories
from fastapi.encoders import jsonable_encoder


class MedicalHistoryController:

    def create_medicalhistory(self, medicalhistory: MedicalHistories):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                """INSERT INTO MedicalHistories (id_student, blood_type)
                   VALUES (%s, %s)""",
                (medicalhistory.id_student, medicalhistory.blood_type)
            )
            conn.commit()
            return {"resultado": "Historial médico creado correctamente"}

        except psycopg2.Error as err:
            if conn:
                conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))

        finally:
            if conn:
                conn.close()


    def get_medicalhistory(self, id_history: int):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM MedicalHistories WHERE id_history = %s",
                (id_history,)
            )
            result = cursor.fetchone()

            if not result:
                raise HTTPException(status_code=404, detail="Historial médico not found")

            content = {
                'id_history': result[0],
                'id_student': result[1],
                'blood_type': result[2]
            }

            return jsonable_encoder(content)

        except psycopg2.Error as err:
            raise HTTPException(status_code=500, detail=str(err))

        finally:
            if conn:
                conn.close()


    def get_medicalhistories(self):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM MedicalHistories")
            result = cursor.fetchall()

            if not result:
                raise HTTPException(status_code=404, detail="Historiales médicos not found")

            payload = []
            for data in result:
                payload.append({
                    'id_history': data[0],
                    'id_student': data[1],
                    'blood_type': data[2]
                })

            return {"resultado": jsonable_encoder(payload)}

        except psycopg2.Error as err:
            raise HTTPException(status_code=500, detail=str(err))

        finally:
            if conn:
                conn.close()
    def update_history(self, id_history: int, history: MedicalHistories):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                """UPDATE medical_histories SET
                    id_student = %s,
                    blood_type = %s
                   WHERE id_history = %s""",
                (history.id_student, history.blood_type, id_history)
            )
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Medical history not found")
            conn.commit()
            return {"resultado": "Historial médico actualizado correctamente"}
        except psycopg2.Error as err:
            if conn:
                conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn:
                conn.close()

    def delete_history(self, id_history: int):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM medical_histories WHERE id_history = %s", (id_history,))
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Medical history not found")
            conn.commit()
            return {"resultado": f"Historial médico con id {id_history} eliminado correctamente"}
        except psycopg2.Error as err:
            if conn:
                conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn:
                conn.close()

medical_history_controller = MedicalHistoryController()