from fastapi import APIRouter
from app.controllers.derivation_controller import derivation_controller
from app.models.derivation_model import Derivation

router = APIRouter(prefix="/derivations", tags=["Derivations"])

# CREATE
@router.post("/create_derivation")
def create_derivation(derivation: Derivation):
    return derivation_controller.create_derivation(derivation)

# GET ONE
@router.get("/get_derivation/{id_derivation}", response_model=Derivation)
def get_derivation(id_derivation: int):
    return derivation_controller.get_derivation(id_derivation)

# GET ALL
@router.get("/get_derivations/")
def get_derivations():
    return derivation_controller.get_derivations()

# UPDATE
@router.put("/{id_derivation}")
def update_derivation(id_derivation: int, derivation: Derivation):
    return derivation_controller.update_derivation(id_derivation, derivation)

# DELETE
@router.delete("/{id_derivation}")
def delete_derivation(id_derivation: int):
    return derivation_controller.delete_derivation(id_derivation)