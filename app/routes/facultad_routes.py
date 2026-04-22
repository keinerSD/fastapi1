from fastapi import APIRouter, HTTPException
from app.controllers.facultad_controller import *
from app.models.facultad_model import Facultad
from fastapi_mail import FastMail, MessageSchema
from app.config.email_config import conf

router = APIRouter(prefix="/facultades", tags=["Facultades"])

nueva_facultad = FacultadController()


@router.post("/create_facultad")
async def create_facultad(facultad: Facultad):

    rpta = nueva_facultad.create_facultad(facultad)

    mensaje = MessageSchema(
        subject="Facultad creada",
        recipients=["garciapecam@gmail.com"],
        body=f"Se creó la facultad: {facultad.nombre}",
        subtype="plain"
    )

    await FastMail(conf).send_message(mensaje)

    return rpta

@router.get("/get_facultad/{id_facultad}", response_model=Facultad)
async def get_facultad(id_facultad: int):
    rpta = nueva_facultad.get_facultad(id_facultad)
    return rpta


@router.get("/get_facultades/")
async def get_facultades():
    rpta = nueva_facultad.get_facultades()
    return rpta

@router.put("/{id_facultad}")
async def update_facultad(id_facultad: int, facultad: Facultad):

    rpta = nueva_facultad.update_facultad(id_facultad, facultad)

    mensaje = MessageSchema(
        subject="Facultad actualizada",
        recipients=["garciapecam@gmail.com"],
        body=f"Se actualizó la facultad con ID: {id_facultad}",
        subtype="plain"
    )

    await FastMail(conf).send_message(mensaje)

    return rpta


@router.delete("/{id_facultad}")
async def delete_facultad(id_facultad: int):

    rpta = nueva_facultad.delete_facultad(id_facultad)

    mensaje = MessageSchema(
        subject="Facultad eliminada",
        recipients=["garciapecam@gmail.com"],
        body=f"Se eliminó la facultad con ID: {id_facultad}",
        subtype="plain"
    )

    await FastMail(conf).send_message(mensaje)

    return rpta