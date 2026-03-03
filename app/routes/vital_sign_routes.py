from fastapi import APIRouter
from app.controllers.vital_sign_controller import vital_sign_controller
from app.models.vital_sign_model import VitalSign

router = APIRouter(prefix="/vital_signs", tags=["VitalSigns"])

# CREATE
@router.post("/create_vital_sign")
def create_vital_sign(vital_sign: VitalSign):
    return vital_sign_controller.create_vital_sign(vital_sign)

# GET ONE
@router.get("/get_vital_sign/{id_signs}", response_model=VitalSign)
def get_vital_sign(id_signs: int):
    return vital_sign_controller.get_vital_sign(id_signs)

# GET ALL
@router.get("/get_vital_signs/")
def get_vital_signs():
    return vital_sign_controller.get_vital_signs()

# UPDATE
@router.put("/{id_signs}")
def update_vital_sign(id_signs: int, vital_sign: VitalSign):
    return vital_sign_controller.update_vital_sign(id_signs, vital_sign)

# DELETE
@router.delete("/{id_signs}")
def delete_vital_sign(id_signs: int):
    return vital_sign_controller.delete_vital_sign(id_signs)