from pydantic import BaseModel
import datetime

class Emergencia(BaseModel):
    id_emergencia: int = None
    id_usuario: int
    id_estudiante: int

    fecha: datetime.datetime
    descripcion: str
    atencion_prestada: str
