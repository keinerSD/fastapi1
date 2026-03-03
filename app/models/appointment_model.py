from pydantic import BaseModel
import datetime

class Appointment(BaseModel):
    id_appointment: int = None
    id_student: int
    id_staff: int
    date: datetime.datetime
    motif: str = None
    state: str = "Pendiente"