from pydantic import BaseModel
import datetime

class Consulta(BaseModel):
    id_consulta: int = None
    id_estudiante: int
    id_usuario: int

    diagnostico: str
    observaciones: str
    motivo_consulta: str

    fecha_entrada: datetime.datetime
    fecha_salida: datetime.datetime
