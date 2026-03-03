import psycopg2
from fastapi import HTTPException
from app.config.db_config import get_db_connection
from app.models.nursing_staff_model import NursingStaff
from fastapi.encoders import jsonable_encoder

class NursingStaffController:

    def create_staff(self, staff: NursingStaff):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                """INSERT INTO nursing_staff
                (name, last_name, range, phone, email, state)
                VALUES (%s, %s, %s, %s, %s, %s)""",
                (
                    staff.name,
                    staff.last_name,
                    staff.range,
                    staff.phone,
                    staff.email,
                    staff.state
                )
            )
            conn.commit()
            return {"resultado": "Personal de enfermería creado correctamente"}
        except psycopg2.Error as err:
            if conn:
                conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn:
                conn.close()

    def get_staff(self, id_staff: int):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM nursing_staff WHERE id_staff = %s",
                (id_staff,)
            )
            result = cursor.fetchone()
            if not result:
                raise HTTPException(status_code=404, detail="Staff not found")
            content = {
                "id_staff": result[0],
                "name": result[1],
                "last_name": result[2],
                "range": result[3],
                "phone": result[4],
                "email": result[5],
                "state": result[6]
            }
            return jsonable_encoder(content)
        except psycopg2.Error as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn:
                conn.close()

    def get_staffs(self):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM nursing_staff")
            result = cursor.fetchall()
            if not result:
                raise HTTPException(status_code=404, detail="No staff found")
            payload = []
            for data in result:
                payload.append({
                    "id_staff": data[0],
                    "name": data[1],
                    "last_name": data[2],
                    "range": data[3],
                    "phone": data[4],
                    "email": data[5],
                    "state": data[6]
                })
            return {"resultado": jsonable_encoder(payload)}
        except psycopg2.Error as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn:
                conn.close()

    def update_staff(self, id_staff: int, staff: NursingStaff):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                """UPDATE nursing_staff SET
                    name = %s,
                    last_name = %s,
                    range = %s,
                    phone = %s,
                    email = %s,
                    state = %s
                   WHERE id_staff = %s""",
                (
                    staff.name,
                    staff.last_name,
                    staff.range,
                    staff.phone,
                    staff.email,
                    staff.state,
                    id_staff
                )
            )
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Staff not found")
            conn.commit()
            return {"resultado": "Personal de enfermería actualizado correctamente"}
        except psycopg2.Error as err:
            if conn:
                conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn:
                conn.close()

    def delete_staff(self, id_staff: int):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM nursing_staff WHERE id_staff = %s",
                (id_staff,)
            )
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Staff not found")
            conn.commit()
            return {"resultado": f"Personal de enfermería con id {id_staff} eliminado correctamente"}
        except psycopg2.Error as err:
            if conn:
                conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn:
                conn.close()

nursing_staff_controller = NursingStaffController()