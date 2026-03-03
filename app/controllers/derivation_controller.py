import psycopg2
from fastapi import HTTPException
from app.config.db_config import get_db_connection
from app.models.derivation_model import Derivation
from fastapi.encoders import jsonable_encoder

class DerivationController:

    def create_derivation(self, derivation: Derivation):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                """INSERT INTO derivations
                (id_query, destination_institution, reason, derivation_date)
                VALUES (%s, %s, %s, %s)""",
                (
                    derivation.id_query,
                    derivation.destination_institution,
                    derivation.reason,
                    derivation.derivation_date
                )
            )
            conn.commit()
            return {"resultado": "Derivación creada correctamente"}
        except psycopg2.Error as err:
            if conn:
                conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn:
                conn.close()

    def get_derivation(self, id_derivation: int):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM derivations WHERE id_derivation = %s",
                (id_derivation,)
            )
            result = cursor.fetchone()
            if not result:
                raise HTTPException(status_code=404, detail="Derivation not found")
            content = {
                "id_derivation": result[0],
                "id_query": result[1],
                "destination_institution": result[2],
                "reason": result[3],
                "derivation_date": result[4]
            }
            return jsonable_encoder(content)
        except psycopg2.Error as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn:
                conn.close()

    def get_derivations(self):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM derivations")
            result = cursor.fetchall()
            if not result:
                raise HTTPException(status_code=404, detail="No derivations found")
            payload = []
            for data in result:
                payload.append({
                    "id_derivation": data[0],
                    "id_query": data[1],
                    "destination_institution": data[2],
                    "reason": data[3],
                    "derivation_date": data[4]
                })
            return {"resultado": jsonable_encoder(payload)}
        except psycopg2.Error as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn:
                conn.close()

    def update_derivation(self, id_derivation: int, derivation: Derivation):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                """UPDATE derivations SET
                    id_query = %s,
                    destination_institution = %s,
                    reason = %s,
                    derivation_date = %s
                   WHERE id_derivation = %s""",
                (
                    derivation.id_query,
                    derivation.destination_institution,
                    derivation.reason,
                    derivation.derivation_date,
                    id_derivation
                )
            )
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Derivation not found")
            conn.commit()
            return {"resultado": "Derivación actualizada correctamente"}
        except psycopg2.Error as err:
            if conn:
                conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn:
                conn.close()

    def delete_derivation(self, id_derivation: int):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM derivations WHERE id_derivation = %s",
                (id_derivation,)
            )
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Derivation not found")
            conn.commit()
            return {"resultado": f"Derivación con id {id_derivation} eliminada correctamente"}
        except psycopg2.Error as err:
            if conn:
                conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn:
                conn.close()

derivation_controller = DerivationController()