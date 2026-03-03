import psycopg2
from fastapi import HTTPException
from app.config.db_config import get_db_connection
from app.models.student_model import Students
from fastapi.encoders import jsonable_encoder


class StudentController:

    def create_student(self, student: Students):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                """INSERT INTO students 
                (tuition, name, last_name, birthdate, gender, phone, email, address)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""",
                (
                    student.tuition,
                    student.name,
                    student.last_name,
                    student.birthdate,
                    student.gender,
                    student.phone,
                    student.email,
                    student.address
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


    def get_student(self, id_student: int):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM students WHERE id_student = %s",
                (id_student,)
            )
            result = cursor.fetchone()

            if not result:
                raise HTTPException(status_code=404, detail="Student not found")

            content = {
                'id_student': result[0],
                'tuition': result[1],
                'name': result[2],
                'last_name': result[3],
                'birthdate': result[4],
                'gender': result[5],
                'phone': result[6],
                'email': result[7],
                'address': result[8]
            }

            return jsonable_encoder(content)

        except psycopg2.Error as err:
            raise HTTPException(status_code=500, detail=str(err))

        finally:
            if conn:
                conn.close()


    def get_students(self):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM students")
            result = cursor.fetchall()

            if not result:
                raise HTTPException(status_code=404, detail="Students not found")

            payload = []
            for data in result:
                payload.append({
                    'id_student': data[0],
                    'tuition': data[1],
                    'name': data[2],
                    'last_name': data[3],
                    'birthdate': data[4],
                    'gender': data[5],
                    'phone': data[6],
                    'email': data[7],
                    'address': data[8]
                })

            return {"resultado": jsonable_encoder(payload)}

        except psycopg2.Error as err:
            raise HTTPException(status_code=500, detail=str(err))

        finally:
            if conn:
                conn.close()

    def update_student(self, id_student: int, student: Students):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                """UPDATE students SET
                    tuition = %s,
                    name = %s,
                    last_name = %s,
                    birthdate = %s,
                    gender = %s,
                    phone = %s,
                    email = %s,
                    address = %s
                   WHERE id_student = %s""",
                (
                    student.tuition,
                    student.name,
                    student.last_name,
                    student.birthdate,
                    student.gender,
                    student.phone,
                    student.email,
                    student.address,
                    id_student
                )
            )
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Student not found")

            conn.commit()
            return {"resultado": "Estudiante actualizado correctamente"}

        except psycopg2.Error as err:
            if conn:
                conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))

        finally:
            if conn:
                conn.close()

    def delete_student(self, id_student: int):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM students WHERE id_student = %s",
                (id_student,)
            )
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Student not found")

            conn.commit()
            return {"resultado": f"Estudiante con id {id_student} eliminado correctamente"}

        except psycopg2.Error as err:
            if conn:
                conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))

        finally:
            if conn:
                conn.close()
                
student_controller = StudentController()