from fastapi import FastAPI, Form
import aiosmtplib
from email.message import EmailMessage

app = FastAPI()

# Email Configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "your-email@gmail.com"
SENDER_PASSWORD = "your-app-password"
RECEIVER_EMAIL = "your-email@gmail.com"

@app.post("/send-email/")
async def send_email(
    full_name: str = Form(...),
    email: str = Form(...),
    phone: str = Form(...),
    subject: str = Form(...),
    message: str = Form(...)
):
    msg = EmailMessage()
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECEIVER_EMAIL
    msg["Subject"] = f"New Contact Form Submission: {subject}"
    msg.set_content(f"""
        Name: {full_name}
        Email: {email}
        Phone: {phone}

        Message:
        {message}
    """)

    try:
        await aiosmtplib.send(
            msg, hostname=SMTP_SERVER, port=SMTP_PORT, start_tls=True,
            username=SENDER_EMAIL, password=SENDER_PASSWORD
        )
        return {"message": "Email sent successfully!"}
    except Exception as e:
        return {"message": f"Error sending email: {str(e)}"}
