from pydantic import BaseModel
import datetime

class Derivacion(BaseModel):
    id_derivacion: int = None
    id_consulta: int
    id_clinica: int

    razon: str
    fecha: datetime.datetime
