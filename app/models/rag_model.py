from pydantic import BaseModel

class SymptomsRequest(BaseModel):
    symptoms: str