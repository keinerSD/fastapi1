from fastapi import APIRouter
from app.models.rag_model import SymptomsRequest
from app.services.rag_service import medical_rag_query

router = APIRouter()

@router.post("/medical-ai")
def medical_ai(data: SymptomsRequest):

    result = medical_rag_query(data.symptoms)

    return {
        "response": result
    }