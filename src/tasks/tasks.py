import smtplib
from email.message import EmailMessage

from celery import Celery
import sys
from pathlib import Path
sys.path.append(str(Path('').absolute().parent))

# import os, sys
# sys.path.insert(0, os.getcwd())

from config import SMTP_PASSWORD, SMTP_USER

SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 465

celery_app = Celery('tasks', broker='redis://localhost:6379')


def get_email_template_dashboard(username: str):
    email = EmailMessage()
    email['Subject'] = 'Натрейдил Отчет Дашборд'
    email['From'] = SMTP_USER
    email['To'] = SMTP_USER

    email.set_content(
        '<div>'
        f'<h1 style="color: red;">Здравствуйте, {username}, а вот и ваш отчет. Зацените 😊</h1>'
        '<img src="https://koshka.top/uploads/posts/2021-11/1637911871_10-koshka-top-p-chertezh-koshki-12.jpg width="600">'
        '</div>',
        subtype='html'
    )
    return email


@celery_app.task
def send_email_report_dashboard(username: str):
    email = get_email_template_dashboard(username)
    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.send_message(email)
