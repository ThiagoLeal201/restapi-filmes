import mysql.connector

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Leal@2021',
    'database': 'filmes',
    'auth_plugin': 'mysql_native_password'
    }

def conectar_banco():
    conn = mysql.connector.connect(**db_config)
    return conn