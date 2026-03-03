from fastapi import APIRouter
from app.controllers.appointment_controller import appointment_controller
from app.models.appointment_model import Appointment

router = APIRouter(prefix="/appointments", tags=["Appointments"])

# CREATE
@router.post("/create_appointment")
def create_appointment(appointment: Appointment):
    return appointment_controller.create_appointment(appointment)

# GET ONE
@router.get("/get_appointment/{id_appointment}", response_model=Appointment)
def get_appointment(id_appointment: int):
    return appointment_controller.get_appointment(id_appointment)

# GET ALL
@router.get("/get_appointments/")
def get_appointments():
    return appointment_controller.get_appointments()

# UPDATE
@router.put("/{id_appointment}")
def update_appointment(id_appointment: int, appointment: Appointment):
    return appointment_controller.update_appointment(id_appointment, appointment)

# DELETE
@router.delete("/{id_appointment}")
def delete_appointment(id_appointment: int):
    return appointment_controller.delete_appointment(id_appointment)