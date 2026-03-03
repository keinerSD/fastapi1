from pydantic import BaseModel
import datetime

class UniversityAccident(BaseModel):
    id_accident: int = None
    id_student: int
    place: str = None
    descripcion: str = None
    date: datetime.date = None
    attended_by: int = None