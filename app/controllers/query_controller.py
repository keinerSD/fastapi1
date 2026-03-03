import psycopg2
from fastapi import HTTPException
from app.config.db_config import get_db_connection
from app.models.query_model import Query
from fastapi.encoders import jsonable_encoder

class QueryController:

    def create_query(self, query: Query):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                """INSERT INTO queries
                (id_appointment, diagnosis, treatment, observations, query_date)
                VALUES (%s, %s, %s, %s, %s)""",
                (
                    query.id_appointment,
                    query.diagnosis,
                    query.treatment,
                    query.observations,
                    query.query_date
                )
            )
            conn.commit()
            return {"resultado": "Consulta creada correctamente"}
        except psycopg2.Error as err:
            if conn:
                conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn:
                conn.close()

    def get_query(self, id_query: int):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM queries WHERE id_query = %s",
                (id_query,)
            )
            result = cursor.fetchone()
            if not result:
                raise HTTPException(status_code=404, detail="Query not found")
            content = {
                "id_query": result[0],
                "id_appointment": result[1],
                "diagnosis": result[2],
                "treatment": result[3],
                "observations": result[4],
                "query_date": result[5]
            }
            return jsonable_encoder(content)
        except psycopg2.Error as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn:
                conn.close()

    def get_queries(self):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM queries")
            result = cursor.fetchall()
            if not result:
                raise HTTPException(status_code=404, detail="No queries found")
            payload = []
            for data in result:
                payload.append({
                    "id_query": data[0],
                    "id_appointment": data[1],
                    "diagnosis": data[2],
                    "treatment": data[3],
                    "observations": data[4],
                    "query_date": data[5]
                })
            return {"resultado": jsonable_encoder(payload)}
        except psycopg2.Error as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn:
                conn.close()

    def update_query(self, id_query: int, query: Query):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                """UPDATE queries SET
                    id_appointment = %s,
                    diagnosis = %s,
                    treatment = %s,
                    observations = %s,
                    query_date = %s
                   WHERE id_query = %s""",
                (
                    query.id_appointment,
                    query.diagnosis,
                    query.treatment,
                    query.observations,
                    query.query_date,
                    id_query
                )
            )
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Query not found")
            conn.commit()
            return {"resultado": "Consulta actualizada correctamente"}
        except psycopg2.Error as err:
            if conn:
                conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn:
                conn.close()

    def delete_query(self, id_query: int):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM queries WHERE id_query = %s",
                (id_query,)
            )
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Query not found")
            conn.commit()
            return {"resultado": f"Consulta con id {id_query} eliminada correctamente"}
        except psycopg2.Error as err:
            if conn:
                conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn:
                conn.close()

query_controller = QueryController()