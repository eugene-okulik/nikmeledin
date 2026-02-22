import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()


def connect():
    try:
        db = mysql.connector.connect(
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSW'),
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT'),
            database=os.getenv('DB_NAME')
        )
        print("Подключились к базе")
        return db
    except Exception:  # Не просто except:
        print("Ошибка подключения")
        return None
