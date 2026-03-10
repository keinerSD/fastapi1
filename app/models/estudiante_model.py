from pydantic import BaseModel
import datetime
from typing import Optional

class Estudiante(BaseModel):
    id_estudiante: Optional[int] = None
    id_facultad: int
    id_programa: int
    id_usuario: int

    primer_nombre: str
    primer_apellido: str
    tipo_identificacion: str
    numero_identificacion: int
    genero: str
    telefono: int
    direccion: str

    fecha_registro: datetime.datetime

