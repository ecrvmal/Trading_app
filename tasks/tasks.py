import smtplib
from email.message import EmailMessage
from celery import Celery
from config import SMTP_USER, SMTP_PASSWORD

SMTP_HOST = 'smtp.gmail.com'
SMTP_PORT = 465

celery = Celery('tasks', broker='redis://localhost:6379')     # fastapi app

def get_email_template_dashboard(username: str):
    email = EmailMessage()
    email['Subject'] = 'Information for '
    email['From'] = SMTP_USER
    email['To'] = SMTP_USER
    email.set_content(
    '<div>'
    f'<h1 style=”color: Ped;">Hello {username}, here is your report, please check </h1>'  \
    '<img src=" https://sun9-18.userapi.com/impf/c624316/v624316886/399de/jkz4qhE0MVw.jpg" ' \
    'style="width:600 px; height: 600px;”>'
    '</div>',
    subtype = 'html'
    )
    return email


@celery.task                                                 # fastAPI decorator for celery app
def send_email_report_dashboard(username: str):
    email = get_email_template_dashboard(username)
    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.send_message(email)
