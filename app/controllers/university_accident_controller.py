import psycopg2
from fastapi import HTTPException
from app.config.db_config import get_db_connection
from app.models.university_accident_model import UniversityAccident
from fastapi.encoders import jsonable_encoder

class UniversityAccidentController:

    def create_accident(self, accident: UniversityAccident):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                """INSERT INTO university_accidents
                (id_student, place, descripcion, date, attended_by)
                VALUES (%s, %s, %s, %s, %s)""",
                (
                    accident.id_student,
                    accident.place,
                    accident.descripcion,
                    accident.date,
                    accident.attended_by
                )
            )
            conn.commit()
            return {"resultado": "Accidente universitario creado correctamente"}
        except psycopg2.Error as err:
            if conn:
                conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn:
                conn.close()

    def get_accident(self, id_accident: int):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM university_accidents WHERE id_accident = %s",
                (id_accident,)
            )
            result = cursor.fetchone()
            if not result:
                raise HTTPException(status_code=404, detail="Accident not found")
            content = {
                "id_accident": result[0],
                "id_student": result[1],
                "place": result[2],
                "descripcion": result[3],
                "date": result[4],
                "attended_by": result[5]
            }
            return jsonable_encoder(content)
        except psycopg2.Error as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn:
                conn.close()

    def get_accidents(self):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM university_accidents")
            result = cursor.fetchall()
            if not result:
                raise HTTPException(status_code=404, detail="No accidents found")
            payload = []
            for data in result:
                payload.append({
                    "id_accident": data[0],
                    "id_student": data[1],
                    "place": data[2],
                    "descripcion": data[3],
                    "date": data[4],
                    "attended_by": data[5]
                })
            return {"resultado": jsonable_encoder(payload)}
        except psycopg2.Error as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn:
                conn.close()

    def update_accident(self, id_accident: int, accident: UniversityAccident):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                """UPDATE university_accidents SET
                    id_student = %s,
                    place = %s,
                    descripcion = %s,
                    date = %s,
                    attended_by = %s
                   WHERE id_accident = %s""",
                (
                    accident.id_student,
                    accident.place,
                    accident.descripcion,
                    accident.date,
                    accident.attended_by,
                    id_accident
                )
            )
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Accident not found")
            conn.commit()
            return {"resultado": "Accidente universitario actualizado correctamente"}
        except psycopg2.Error as err:
            if conn:
                conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn:
                conn.close()

    def delete_accident(self, id_accident: int):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM university_accidents WHERE id_accident = %s",
                (id_accident,)
            )
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Accident not found")
            conn.commit()
            return {"resultado": f"Accidente universitario con id {id_accident} eliminado correctamente"}
        except psycopg2.Error as err:
            if conn:
                conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn:
                conn.close()

university_accident_controller = UniversityAccidentController()