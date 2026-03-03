from pydantic import BaseModel
import datetime

class MedicalEquipments(BaseModel):
    id_equipment: int = None
    name: str
    descripcion: str = None
    serial_number: str = None
    acquisition_date: datetime.date = None
    state: str = "Operativo"
    location: str = None