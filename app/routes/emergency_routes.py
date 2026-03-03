from fastapi import APIRouter
from app.controllers.emergency_controller import emergency_controller
from app.models.emergency_model import Emergency

router = APIRouter(prefix="/emergencies", tags=["Emergencies"])

# CREATE
@router.post("/create_emergency")
def create_emergency(emergency: Emergency):
    return emergency_controller.create_emergency(emergency)

# GET ONE
@router.get("/get_emergency/{id_emergency}", response_model=Emergency)
def get_emergency(id_emergency: int):
    return emergency_controller.get_emergency(id_emergency)

# GET ALL
@router.get("/get_emergencies/")
def get_emergencies():
    return emergency_controller.get_emergencies()

# UPDATE
@router.put("/{id_emergency}")
def update_emergency(id_emergency: int, emergency: Emergency):
    return emergency_controller.update_emergency(id_emergency, emergency)

# DELETE
@router.delete("/{id_emergency}")
def delete_emergency(id_emergency: int):
    return emergency_controller.delete_emergency(id_emergency)