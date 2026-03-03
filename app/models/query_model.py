from pydantic import BaseModel
import datetime

class Query(BaseModel):
    id_query: int = None
    id_appointment: int = None
    diagnosis: str = None
    treatment: str = None
    observations: str = None
    query_date: datetime.datetime = None