from pydantic import BaseModel

class Facultad(BaseModel):
    id_facultad: int = None
    nombre: str
    descripcion: str
