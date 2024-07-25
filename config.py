import os


class DB_Config():
    db_config = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_DATABASE'),
    'auth_plugin': os.getenv('DB_AUTH_PLUGIN')
    }
