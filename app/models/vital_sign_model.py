from pydantic import BaseModel
import datetime

class VitalSign(BaseModel):
    id_signs: int = None
    id_query: int
    blood_pressure: str = None
    temperature: float = None
    weight: float = None
    height: float = None