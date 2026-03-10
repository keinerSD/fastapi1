from pydantic import BaseModel

class SignosVitales(BaseModel):
    id_signos: int = None
    id_consulta: int

    presion_arterial: str
    temperatura: float
    peso: float
    altura: float
    saturacion_oxigeno: float
    frecuencia_cardiaca: float
    tipo_sangre: str

