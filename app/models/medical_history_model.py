from pydantic import BaseModel
from typing import Optional

class MedicalHistories(BaseModel):
    id_history: int = None
    id_student: int = None
    blood_type: str