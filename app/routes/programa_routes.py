from fastapi import APIRouter, HTTPException
from app.controllers.programa_controller import *
from app.models.programa_model import Programa
from fastapi_mail import FastMail, MessageSchema
from app.config.email_config import conf

router = APIRouter(prefix="/programas", tags=["Programas"])

nuevo_programa = ProgramaController()


@router.post("/create_programa")
async def create_programa(programa: Programa):

    rpta = nuevo_programa.create_programa(programa)

    mensaje = MessageSchema(
        subject="Programa creado",
        recipients=["garciapecam@gmail.com"],
        body=f"Se creó el programa: {programa.nombre}",
        subtype="plain"
    )

    await FastMail(conf).send_message(mensaje)

    return rpta

@router.get("/get_programas_por_facultad/{id_facultad}")
async def get_programas_por_facultad(id_facultad: int):
    return programa_controller.get_programas_por_facultad(id_facultad)


@router.get("/get_programas/")
async def get_programas():
    rpta = nuevo_programa.get_programas()
    return rpta

@router.put("/{id_programa}")
async def update_programa(id_programa: int, programa: Programa):

    rpta = nuevo_programa.update_programa(id_programa, programa)

    mensaje = MessageSchema(
        subject="Programa actualizado",
        recipients=["garciapecam@gmail.com"],
        body=f"Se actualizó el programa con ID: {id_programa}",
        subtype="plain"
    )

    await FastMail(conf).send_message(mensaje)

    return rpta


@router.delete("/{id_programa}")
async def delete_programa(id_programa: int):

    rpta = nuevo_programa.delete_programa(id_programa)

    mensaje = MessageSchema(
        subject="Programa eliminado",
        recipients=["garciapecam@gmail.com"],
        body=f"Se eliminó el programa con ID: {id_programa}",
        subtype="plain"
    )

    await FastMail(conf).send_message(mensaje)

    return rpta