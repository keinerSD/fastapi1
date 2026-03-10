from pydantic import BaseModel

class Clinica(BaseModel):
    id_clinica: int = None
    nombre: str
    ubicacion: str
