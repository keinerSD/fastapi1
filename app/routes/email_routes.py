from fastapi import APIRouter
from fastapi_mail import FastMail, MessageSchema, MessageType
from app.config.email_config import conf

router = APIRouter(prefix="/email", tags=["Email"])

@router.post("/reporte_generado")
async def enviar_email_reporte():
    mensaje = MessageSchema(
        subject="📊 Nuevo reporte generado",
        recipients=["garciapecam@gmail.com"],
        body=f"""
        <html>
          <body style="font-family: Segoe UI, sans-serif; padding: 20px; color: #1a237e;">
            <h2>Nuevo reporte generado</h2>
            <p>Hola, te informamos que se ha generado un nuevo reporte en el sistema.</p>
            <p style="color: #546e7a; font-size: 14px;">Este es un mensaje automático, por favor no responder.</p>
          </body>
        </html>
        """,
        subtype=MessageType.html
    )

    fm = FastMail(conf)
    await fm.send_message(mensaje)
    return {"mensaje": "Email enviado correctamente"}