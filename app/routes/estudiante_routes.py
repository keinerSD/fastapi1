from fastapi import APIRouter, HTTPException
from app.controllers.estudiante_controller import *
from app.models.estudiante_model import Estudiante
from fastapi_mail import FastMail, MessageSchema
from app.config.email_config import conf

router = APIRouter(prefix="/estudiantes", tags=["Estudiantes"])

nuevo_estudiante = EstudianteController()


@router.post("/create_estudiante")
async def create_estudiante(estudiante: Estudiante):

    rpta = nuevo_estudiante.create_estudiante(estudiante)

    mensaje = MessageSchema(
        subject="Nuevo estudiante registrado",
        recipients=["garciapecam@gmail.com"],  
        body=f"""
        Se registró un nuevo estudiante:

        Nombre: {estudiante.primer_nombre} {estudiante.primer_apellido}
        Documento: {estudiante.numero_identificacion}
        """,
        subtype="plain"
    )

    fm = FastMail(conf)
    await fm.send_message(mensaje)

    return rpta


@router.get("/get_estudiante/{numero_identificacion}", response_model=Estudiante)
async def get_estudiante(numero_identificacion: int):
    return nuevo_estudiante.get_estudiante(numero_identificacion)


@router.get("/get_estudiantes/")
async def get_estudiantes():
    return nuevo_estudiante.get_estudiantes()


@router.put("/{id_estudiante}")
def update_estudiante(id_estudiante: int, estudiante: Estudiante):
    return nuevo_estudiante.update_estudiante(id_estudiante, estudiante)


@router.delete("/{id_estudiante}")
async def delete_estudiante(id_estudiante: int):

    rpta = nuevo_estudiante.delete_estudiante(id_estudiante)

    mensaje = MessageSchema(
        subject="Estudiante eliminado",
        recipients=["garciapecam@gmail.com"],
        body=f"Se eliminó el estudiante con ID: {id_estudiante}",
        subtype="plain"
    )

    fm = FastMail(conf)
    await fm.send_message(mensaje)

    return rpta