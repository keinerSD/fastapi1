from pydantic import BaseModel

class Programa(BaseModel):
    id_programa: int = None
    id_facultad: int
    nombre: str
    descripcion: str
