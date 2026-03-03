from pydantic import BaseModel
import datetime

class Derivation(BaseModel):
    id_derivation: int = None
    id_query: int
    destination_institution: str
    reason: str = None
    derivation_date: datetime.date = None