from fastapi import APIRouter, HTTPException
from app.controllers.student_controller import *
from app.models.student_model import Students

router = APIRouter(prefix="/students",tags=["Students"])

nuevo_estudiante = StudentController()


@router.post("/create_student")
async def create_student(student: Students):
    rpta = nuevo_estudiante.create_student(student)
    return rpta


@router.get("/get_student/{id_student}",response_model=Students)
async def get_student(id_student: int):
    rpta = nuevo_estudiante.get_student(id_student)
    return rpta

@router.get("/get_students/")
async def get_students():
    rpta = nuevo_estudiante.get_students()
    return rpta

@router.put("/{id_student}")
def update_student(id_student: int, student: Students):
    return student_controller.update_student(id_student, student)

# DELETE
@router.delete("/{id_student}")
def delete_student(id_student: int):
    return student_controller.delete_student(id_student)