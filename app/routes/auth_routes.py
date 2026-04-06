from fastapi import APIRouter, Depends
from app.controllers.auth_controller import AuthController
from app.models.auth_model import Login, Register
from app.utils.auth_dependency import get_usuario_actual

router = APIRouter()
nuevo_auth = AuthController()

@router.post("/login")
async def login(datos: Login):
    rpta = nuevo_auth.login(datos)
    return rpta

@router.post("/register")
async def register(datos: Register):
    rpta = nuevo_auth.register(datos)
    return rpta

@router.get("/me")
async def mi_perfil(usuario=Depends(get_usuario_actual)):
    return {
        "id_usuario": usuario.get("sub"),
        "email": usuario.get("email"),
        "rol": usuario.get("rol")
    }
