from fastapi import APIRouter
from app.controllers.nursing_staff_controller import nursing_staff_controller
from app.models.nursing_staff_model import NursingStaff

router = APIRouter(prefix="/nursing_staff", tags=["NursingStaff"])

# CREATE
@router.post("/create_staff")
def create_staff(staff: NursingStaff):
    return nursing_staff_controller.create_staff(staff)

# GET ONE
@router.get("/get_staff/{id_staff}", response_model=NursingStaff)
def get_staff(id_staff: int):
    return nursing_staff_controller.get_staff(id_staff)

# GET ALL
@router.get("/get_staffs/")
def get_staffs():
    return nursing_staff_controller.get_staffs()

# UPDATE
@router.put("/{id_staff}")
def update_staff(id_staff: int, staff: NursingStaff):
    return nursing_staff_controller.update_staff(id_staff, staff)

# DELETE
@router.delete("/{id_staff}")
def delete_staff(id_staff: int):
    return nursing_staff_controller.delete_staff(id_staff)