from fastapi import APIRouter, HTTPException
from app.controllers.medical_equipment_controller import *
from app.models.medical_equipment_model import MedicalEquipments

router = APIRouter(prefix="/medicalequipments",tags=["MedicalEquipments"])

nuevo_equipo = MedicalEquipmentsController()


@router.post("/create_medicalequipment")
async def create_medicalequipment(medicalequipment: MedicalEquipments):
    rpta = nuevo_equipo.create_medicalequipment(medicalequipment)
    return rpta

@router.get("/get_medicalequipment/{id_equipment}",response_model=MedicalEquipments)
async def get_medicalequipment(id_equipment: int):
    rpta = nuevo_equipo.get_medicalequipment(id_equipment)
    return rpta

@router.get("/get_medicalequipments/")
async def get_medicalequipments():
    rpta = nuevo_equipo.get_medicalequipments()
    return rpta

@router.put("/{id_equipment}")
def update_equipment(id_equipment: int, equipment: MedicalEquipments):
    return medical_equipment_controller.update_equipment(id_equipment, equipment)

@router.delete("/{id_equipment}")
def delete_equipment(id_equipment: int):
    return medical_equipment_controller.delete_equipment(id_equipment)