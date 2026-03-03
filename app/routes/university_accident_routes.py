from fastapi import APIRouter
from app.controllers.university_accident_controller import university_accident_controller
from app.models.university_accident_model import UniversityAccident

router = APIRouter(prefix="/university_accidents", tags=["UniversityAccidents"])

# CREATE
@router.post("/create_accident")
def create_accident(accident: UniversityAccident):
    return university_accident_controller.create_accident(accident)

# GET ONE
@router.get("/get_accident/{id_accident}", response_model=UniversityAccident)
def get_accident(id_accident: int):
    return university_accident_controller.get_accident(id_accident)

# GET ALL
@router.get("/get_accidents/")
def get_accidents():
    return university_accident_controller.get_accidents()

# UPDATE
@router.put("/{id_accident}")
def update_accident(id_accident: int, accident: UniversityAccident):
    return university_accident_controller.update_accident(id_accident, accident)

# DELETE
@router.delete("/{id_accident}")
def delete_accident(id_accident: int):
    return university_accident_controller.delete_accident(id_accident)