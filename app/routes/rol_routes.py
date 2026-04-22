from fastapi import APIRouter
from app.controllers.rol_controller import *
from app.models.rol_model import Rol
from fastapi_mail import FastMail, MessageSchema
from app.config.email_config import conf

router = APIRouter(prefix="/roles", tags=["Roles"])

nuevo_rol = RolController()


@router.post("/create_rol")
async def create_rol(rol: Rol):

    rpta = nuevo_rol.create_rol(rol)

    mensaje = MessageSchema(
        subject="Rol creado",
        recipients=["garciapecam@gmail.com"],
        body=f"""
        Se creó un rol:

        Nombre: {rol.nombre}
        """,
        subtype="plain"
    )

    await FastMail(conf).send_message(mensaje)
    return rpta


@router.get("/get_rol/{id_rol}", response_model=Rol)
async def get_rol(id_rol: int):
    return nuevo_rol.get_rol(id_rol)


@router.get("/get_roles/")
async def get_roles():
    return nuevo_rol.get_roles()


@router.put("/{id_rol}")
async def update_rol(id_rol: int, rol: Rol):

    rpta = nuevo_rol.update_rol(id_rol, rol)

    mensaje = MessageSchema(
        subject="Rol actualizado",
        recipients=["garciapecam@gmail.com"],
        body=f"""
        Se actualizó un rol:

        Nombre: {rol.nombre}
        """,
        subtype="plain"
    )

    await FastMail(conf).send_message(mensaje)
    return rpta


@router.delete("/{id_rol}")
async def delete_rol(id_rol: int):

    rol = nuevo_rol.get_rol(id_rol)

    rpta = nuevo_rol.delete_rol(id_rol)

    mensaje = MessageSchema(
        subject="Rol eliminado",
        recipients=["garciapecam@gmail.com"],
        body=f"""
        Se eliminó un rol:

        Nombre: {rol.nombre}
        """,
        subtype="plain"
    )

    await FastMail(conf).send_message(mensaje)
    return rpta