from fastapi import APIRouter
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

    await FastMail(conf).send_message(mensaje)
    return rpta


@router.get("/get_clinicas/")
async def get_clinicas():
    return nueva_clinica.get_clinicas()


@router.put("/{id_clinica}")
async def update_clinica(id_clinica: int, clinica: Clinica):

    rpta = nueva_clinica.update_clinica(id_clinica, clinica)

    mensaje = MessageSchema(
        subject="Clínica actualizada",
        recipients=["garciapecam@gmail.com"],
        body=f"""
        Se actualizó una clínica:

        Nombre: {clinica.nombre}
        """,
        subtype="plain"
    )

    await FastMail(conf).send_message(mensaje)
    return rpta


@router.delete("/{id_clinica}")
async def delete_clinica(id_clinica: int):

    clinica = nueva_clinica.get_clinica(id_clinica)

    rpta = nueva_clinica.delete_clinica(id_clinica)

    mensaje = MessageSchema(
        subject="Clínica eliminada",
        recipients=["garciapecam@gmail.com"],
        body=f"""
        Se eliminó una clínica:

        Nombre: {clinica.nombre}
        """,
        subtype="plain"
    )

    await FastMail(conf).send_message(mensaje)
    return rpta