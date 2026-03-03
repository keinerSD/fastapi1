from fastapi import APIRouter, HTTPException
from app.controllers.medical_history_controller import *
from app.models.medical_history_model import MedicalHistories

router = APIRouter(prefix="/medicalhistories",tags=["MedicalHistories"])

nueva_historia = MedicalHistoryController()


@router.post("/create_medicalhistory")
async def create_medicalhistory(medicalhistory: MedicalHistories):
    rpta = nueva_historia.create_medicalhistory(medicalhistory)
    return rpta


@router.get("/get_medicalhistory/{id_history}",response_model=MedicalHistories)
async def get_medicalhistory(id_history: int):
    rpta = nueva_historia.get_medicalhistory(id_history)
    return rpta

@router.get("/get_medicalhistories/")
async def get_medicalhistories():
    rpta = nueva_historia.get_medicalhistories()
    return rpta

@router.put("/{id_history}")
def update_history(id_history: int, history: MedicalHistories):
    return medical_history_controller.update_history(id_history, history)

@router.delete("/{id_history}")
def delete_history(id_history: int):
    return medical_history_controller.delete_history(id_history)