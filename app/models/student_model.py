from pydantic import BaseModel
import datetime

class Students(BaseModel):
    id_student: int = None
    tuition: str 
    name: str
    last_name: str
    birthdate: datetime.date
    gender: str
    phone: int
    email: str
    address: str