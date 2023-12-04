# config_data

from dotenv import load_dotenv
import os

load_dotenv()

SMTP_USER = 'vladimir.malchevskiy@gmail.com'
SMTP_PASSWORD = 'qwhh hdax byse rzvj'


DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")

DB_PASS = os.environ.get("DB_PASS")
