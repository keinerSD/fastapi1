from fastapi import FastAPI
from app.routes.student_routes import router as student_router
from app.routes.medical_equipment_routes import router as medical_equipment_router
from app.routes.medical_history_routes import router as medical_history_router
from app.routes.university_accident_routes import router as university_accident_router
from app.routes.derivation_routes import router as derivation_router
from app.routes.emergency_routes import router as emergency_router
from app.routes.vital_sign_routes import router as vital_sign_router
from app.routes.query_routes import router as query_router
from app.routes.appointment_routes import router as appointment_router
from app.routes.nursing_staff_routes import router as nursing_staff_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    #"http://localhost.tiangolo.com",
    #"https://localhost.tiangolo.com",
    "http://localhost"
    #"http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(student_router)
app.include_router(medical_equipment_router)
app.include_router(medical_history_router)
app.include_router(university_accident_router)
app.include_router(derivation_router)
app.include_router(emergency_router)
app.include_router(vital_sign_router)
app.include_router(query_router)
app.include_router(appointment_router)
app.include_router(nursing_staff_router)

@app.get("/")
def root():
    return {"message": "API corriendo correctamente"}