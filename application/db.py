import mysql.connector
from config import DB_Config
from dotenv import load_dotenv

load_dotenv()

def conectar_banco():
    conn = mysql.connector.connect(**DB_Config.db_config)
    return conn