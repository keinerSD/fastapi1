import psycopg2
from fastapi import HTTPException
from app.config.db_config import get_db_connection
from app.models.medical_equipment_model import MedicalEquipments
from fastapi.encoders import jsonable_encoder


class MedicalEquipmentsController:

    def create_medicalequipment(self, medicalequipment: MedicalEquipments):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                """INSERT INTO MedicalEquipments 
                (name, descripcion, serial_number, acquisition_date, state, location)
                VALUES (%s, %s, %s, %s, %s, %s)""",
                (
                    medicalequipment.name,
                    medicalequipment.descripcion,
                    medicalequipment.serial_number,
                    medicalequipment.acquisition_date,
                    medicalequipment.state,
                    medicalequipment.location
                )
            )
            conn.commit()
            return {"resultado": "Equipo Médico creado correctamente"}

        except psycopg2.Error as err:
            if conn:
                conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))

        finally:
            if conn:
                conn.close()


    def get_medicalequipment(self, id_equipment: int):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM MedicalEquipments WHERE id_equipment = %s",
                (id_equipment,)
            )
            result = cursor.fetchone()

            if not result:
                raise HTTPException(status_code=404, detail="Equipo not found")

            content = {
                'id_equipment': result[0],
                'name': result[1],
                'descripcion': result[2],
                'serial_number': result[3],
                'acquisition_date': result[4],
                'state': result[5],
                'location': result[6]
            }

            return jsonable_encoder(content)

        except psycopg2.Error as err:
            raise HTTPException(status_code=500, detail=str(err))

        finally:
            if conn:
                conn.close()


    def get_medicalequipments(self):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM MedicalEquipments")
            result = cursor.fetchall()

            if not result:
                raise HTTPException(status_code=404, detail="Equipos not found")

            payload = []
            for data in result:
                payload.append({
                    'id_equipment': data[0],
                    'name': data[1],
                    'descripcion': data[2],
                    'serial_number': data[3],
                    'acquisition_date': data[4],
                    'state': data[5],
                    'location': data[6]
                })

            return {"resultado": jsonable_encoder(payload)}

        except psycopg2.Error as err:
            raise HTTPException(status_code=500, detail=str(err))

        finally:
            if conn:
                conn.close()

    def update_equipment(self, id_equipment: int, equipment: MedicalEquipments):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                """UPDATE medical_equipments SET
                    name = %s,
                    descripcion = %s,
                    serial_number = %s,
                    acquisition_date = %s,
                    state = %s,
                    location = %s
                   WHERE id_equipment = %s""",
                (
                    equipment.name,
                    equipment.descripcion,
                    equipment.serial_number,
                    equipment.acquisition_date,
                    equipment.state,
                    equipment.location,
                    id_equipment
                )
            )
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Medical equipment not found")
            conn.commit()
            return {"resultado": "Equipo médico actualizado correctamente"}
        except psycopg2.Error as err:
            if conn:
                conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn:
                conn.close()

    def delete_equipment(self, id_equipment: int):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM medical_equipments WHERE id_equipment = %s", (id_equipment,))
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Medical equipment not found")
            conn.commit()
            return {"resultado": f"Equipo médico con id {id_equipment} eliminado correctamente"}
        except psycopg2.Error as err:
            if conn:
                conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn:
                conn.close()
medical_equipment_controller = MedicalEquipmentsController()