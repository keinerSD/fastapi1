from pydantic import BaseModel
import datetime

class Emergency(BaseModel):
    id_emergency: int = None
    id_student: int
    date: datetime.date = None
    descripcion: str = None
    attention_provided: str = None
    id_staff: int = None