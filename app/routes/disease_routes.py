from fastapi import APIRouter
from app.models.disease_model import SymptomsInput
from app.controllers.disease_controller import predict_disease

router = APIRouter()

@router.post("/predict")

def predict_route(data: SymptomsInput):

    result = predict_disease(data.symptoms)

    return {"predictions": result}