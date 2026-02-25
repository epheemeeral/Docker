import pandas as pd
from sqlalchemy import create_engine
import os
import time

# Собираем URL, используя значения из .env или дефолтные значения
user = os.getenv('POSTGRES_USER', 'admin')
password = os.getenv('POSTGRES_PASSWORD', 'password123')
host = os.getenv('DB_HOST', 'db')
port = os.getenv('DB_PORT', '5432')
db_name = os.getenv('POSTGRES_DB', 'social_analytics')

db_url = f"postgresql://{user}:{password}@{host}:{port}/{db_name}"

def load_data():
    print(f"Попытка подключения к: postgresql://{user}:***@{host}:{port}/{db_name}")
    try:
        engine = create_engine(db_url)
        # Проверяем наличие файла перед чтением
        csv_path = '/data/social_media.csv'
        if not os.path.exists(csv_path):
            print(f"ОШИБКА: Файл {csv_path} не найден!")
            return

        df = pd.read_csv(csv_path)
        df.to_sql('social_metrics', engine, if_exists='replace', index=False)
        print(" Данные успешно загружены в PostgreSQL!")
    except Exception as e:
        print(f"Ошибка при загрузке: {e}")

if __name__ == "__main__":
    # Даем базе 5 секунд на окончательную инициализацию
    time.sleep(5)
    load_data()