from fastapi_mail import ConnectionConfig

conf = ConnectionConfig(
    MAIL_USERNAME="nurseapp.soporte@gmail.com",
    MAIL_PASSWORD="nuuq mxfy tiqj ctwa",
    MAIL_FROM="kokeiner2007@gmail.com",
    MAIL_PORT=587,
    MAIL_SERVER="smtp.gmail.com",
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False
)