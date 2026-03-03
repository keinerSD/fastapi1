import psycopg2
from fastapi import HTTPException
from app.config.db_config import get_db_connection
from app.models.appointment_model import Appointment
from fastapi.encoders import jsonable_encoder

class AppointmentController:

    def create_appointment(self, appointment: Appointment):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                """INSERT INTO appointment
                (id_student, id_staff, date, motif, state)
                VALUES (%s, %s, %s, %s, %s)""",
                (
                    appointment.id_student,
                    appointment.id_staff,
                    appointment.date,
                    appointment.motif,
                    appointment.state
                )
            )
            conn.commit()
            return {"resultado": "Cita creada correctamente"}
        except psycopg2.Error as err:
            if conn:
                conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn:
                conn.close()

    def get_appointment(self, id_appointment: int):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM appointment WHERE id_appointment = %s",
                (id_appointment,)
            )
            result = cursor.fetchone()
            if not result:
                raise HTTPException(status_code=404, detail="Appointment not found")
            content = {
                "id_appointment": result[0],
                "id_student": result[1],
                "id_staff": result[2],
                "date": result[3],
                "motif": result[4],
                "state": result[5]
            }
            return jsonable_encoder(content)
        except psycopg2.Error as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn:
                conn.close()

    def get_appointments(self):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM appointment")
            result = cursor.fetchall()
            if not result:
                raise HTTPException(status_code=404, detail="No appointments found")
            payload = []
            for data in result:
                payload.append({
                    "id_appointment": data[0],
                    "id_student": data[1],
                    "id_staff": data[2],
                    "date": data[3],
                    "motif": data[4],
                    "state": data[5]
                })
            return {"resultado": jsonable_encoder(payload)}
        except psycopg2.Error as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn:
                conn.close()

    def update_appointment(self, id_appointment: int, appointment: Appointment):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                """UPDATE appointment SET
                    id_student = %s,
                    id_staff = %s,
                    date = %s,
                    motif = %s,
                    state = %s
                   WHERE id_appointment = %s""",
                (
                    appointment.id_student,
                    appointment.id_staff,
                    appointment.date,
                    appointment.motif,
                    appointment.state,
                    id_appointment
                )
            )
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Appointment not found")
            conn.commit()
            return {"resultado": "Cita actualizada correctamente"}
        except psycopg2.Error as err:
            if conn:
                conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn:
                conn.close()

    def delete_appointment(self, id_appointment: int):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM appointment WHERE id_appointment = %s",
                (id_appointment,)
            )
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Appointment not found")
            conn.commit()
            return {"resultado": f"Cita con id {id_appointment} eliminada correctamente"}
        except psycopg2.Error as err:
            if conn:
                conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn:
                conn.close()

appointment_controller = AppointmentController()