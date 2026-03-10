from pydantic import BaseModel

class Usuario(BaseModel):
    id_usuario: int = None
    primer_nombre: str
    primer_apellido: str
    telefono: str
    email: str
    password: str
    estado: bool
    id_rol: int
