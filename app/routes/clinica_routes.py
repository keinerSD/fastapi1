from fastapi import APIRouter, HTTPException
from app.controllers.clinica_controller import *
from app.models.clinica_model import Clinica
from fastapi_mail import FastMail, MessageSchema
from app.config.email_config import conf

router = APIRouter(prefix="/clinicas", tags=["Clinicas"])

nueva_clinica = ClinicaController()


@router.post("/create_clinica")
async def create_clinica(clinica: Clinica):

    rpta = nueva_clinica.create_clinica(clinica)

    mensaje = MessageSchema(
        subject="Clínica creada",
        recipients=["garciapecam@gmail.com"],
        body=f"""
        Se creó una clínica:

        Nombre: {clinica.nombre}
        """,
        subtype="plain"
    )

    fm = FastMail(conf)
    await fm.send_message(mensaje)

    return rpta


@router.put("/{id_clinica}")
def update_clinica(id_clinica: int, clinica: Clinica):
    return nueva_clinica.update_clinica(id_clinica, clinica)


@router.get("/get_clinicas/")
async def get_clinicas():
    rpta = nueva_clinica.get_clinicas()
    return rpta


@router.put("/{id_clinica}")
def update_clinica(id_clinica: int, clinica: Clinica):
    return clinica_controller.update_clinica(id_clinica, clinica)


@router.delete("/{id_clinica}")
async def delete_clinica(id_clinica: int):

    rpta = nueva_clinica.delete_clinica(id_clinica)

    mensaje = MessageSchema(
        subject="Clínica eliminada",
        recipients=["garciapecam@gmail.com"],
        body=f"Se eliminó la clínica con ID: {id_clinica}",
        subtype="plain"
    )

    fm = FastMail(conf)
    await fm.send_message(mensaje)

    return rpta
