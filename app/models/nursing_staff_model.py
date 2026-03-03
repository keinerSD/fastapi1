from pydantic import BaseModel

class NursingStaff(BaseModel):
    id_staff: int = None
    name: str
    last_name: str
    range: str = None
    phone: str = None
    email: str = None
    state: str = "Activo"