from fastapi import APIRouter
from app.controllers.consulta_controller import *
from app.models.consulta_model import Consulta
from fastapi_mail import FastMail, MessageSchema
from app.config.email_config import conf

router = APIRouter(prefix="/consultas", tags=["Consultas"])

nueva_consulta = ConsultaController()


@router.post("/create_consulta")
async def create_consulta(consulta: Consulta):

    rpta = nueva_consulta.create_consulta(consulta)

    mensaje = MessageSchema(
        subject="Nuevo reporte generado",
        recipients=["garciapecam@gmail.com"],
        body=f"""
        Se ha generado un nuevo reporte:

        Estudiante ID: {consulta.id_estudiante}
        Diagnóstico: {consulta.diagnostico}
        Motivo: {consulta.motivo_consulta}
        """,
        subtype="plain"
    )

    fm = FastMail(conf)
    await fm.send_message(mensaje)

    return rpta

@router.get("/get_consulta/{id_consulta}")
async def get_consulta(id_consulta: int):

    controller = ConsultaController()

    return controller.get_consulta(id_consulta)

@router.get("/get_consultas_estudiante/{id_estudiante}")
async def get_consultas_estudiante(id_estudiante: int):
    rpta = nueva_consulta.get_consultas_estudiante(id_estudiante)
    return rpta

@router.get("/get_consultas/{cedula}")
async def get_consultas(cedula: str):

    resultado = nueva_consulta.get_consultas_by_cedula(cedula)

    return {
        "resultado": resultado
    }

@router.get("/get_consultas/")
async def get_consultas():
    rpta = nueva_consulta.get_consultas()
    return rpta

@router.put("/{id_consulta}")
async def update_consulta(id_consulta: int, consulta: Consulta):

    rpta = nueva_consulta.update_consulta(id_consulta, consulta)

    mensaje = MessageSchema(
        subject="Reporte actualizado",
        recipients=["garciapecam@gmail.com"],
        body=f"""
        Se actualizó un reporte:

        ID Consulta: {id_consulta}
        Diagnóstico: {consulta.diagnostico}
        """,
        subtype="plain"
    )

    fm = FastMail(conf)
    await fm.send_message(mensaje)

    return rpta

@router.delete("/{id_consulta}")
async def delete_consulta(id_consulta: int):

    rpta = nueva_consulta.delete_consulta(id_consulta)

    mensaje = MessageSchema(
        subject="Reporte eliminado",
        recipients=["garciapecam@gmail.com"],
        body=f"Se eliminó el reporte con ID: {id_consulta}",
        subtype="plain"
    )

    fm = FastMail(conf)
    await fm.send_message(mensaje)

    return rpta