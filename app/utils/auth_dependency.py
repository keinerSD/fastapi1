from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.utils.jwt_utils import decodificar_token

bearer = HTTPBearer()

def get_usuario_actual(
    credentials: HTTPAuthorizationCredentials = Depends(bearer)
):
    payload = decodificar_token(credentials.credentials)
    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido o expirado"
        )
    return payload

def requiere_rol(*roles: str):
    """
    Uso: Depends(requiere_rol("medico", "admin"))
    Usa el nombre del rol de tu tabla rol.nombre
    """
    def verificar(usuario=Depends(get_usuario_actual)):
        if usuario.get("rol") not in roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Acceso denegado. Roles permitidos: {list(roles)}"
            )
        return usuario
    return verificar