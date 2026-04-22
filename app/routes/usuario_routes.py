from fastapi import APIRouter, HTTPException
from app.controllers.usuario_controller import *
from app.models.usuario_model import Usuario
from fastapi_mail import FastMail, MessageSchema
from app.config.email_config import conf

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

nuevo_usuario = UsuarioController()


@router.post("/create_usuario")
async def create_usuario(usuario: Usuario):

    rpta = nuevo_usuario.create_usuario(usuario)

    mensaje = MessageSchema(
        subject="Usuario creado",
        recipients=["garciapecam@gmail.com"],
        body=f"""
        Se creó un usuario:

        Nombre: {usuario.primer_nombre} {usuario.primer_apellido}
        """,
        subtype="plain"
    )

    await FastMail(conf).send_message(mensaje)

    return rpta

@router.get("/get_usuario/{id_usuario}", response_model=Usuario)
async def get_usuario(id_usuario: int):
    rpta = nuevo_usuario.get_usuario(id_usuario)
    return rpta


@router.get("/get_usuarios/")
async def get_usuarios():
    rpta = nuevo_usuario.get_usuarios()
    return rpta

@router.put("/{id_usuario}")
async def update_usuario(id_usuario: int, usuario: Usuario):

    rpta = nuevo_usuario.update_usuario(id_usuario, usuario)

    mensaje = MessageSchema(
        subject="Usuario actualizado",
        recipients=["garciapecam@gmail.com"],
        body=f"Se actualizó el usuario con ID: {id_usuario}",
        subtype="plain"
    )

    await FastMail(conf).send_message(mensaje)

    return rpta


@router.delete("/{id_usuario}")
async def delete_usuario(id_usuario: int):

    rpta = nuevo_usuario.delete_usuario(id_usuario)

    mensaje = MessageSchema(
        subject="Usuario eliminado",
        recipients=["garciapecam@gmail.com"],
        body=f"Se eliminó el usuario con ID: {id_usuario}",
        subtype="plain"
    )

    await FastMail(conf).send_message(mensaje)

    return rpta