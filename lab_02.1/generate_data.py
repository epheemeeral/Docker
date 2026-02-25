import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

def generate_social_data(num_rows=5000):
    np.random.seed(42)
    
    # Создаем временные метки за последние 30 дней
    start_date = datetime(2024, 1, 1)
    dates = [start_date + timedelta(minutes=np.random.randint(0, 43200)) for _ in range(num_rows)]
    
    data = {
        'post_id': range(1, num_rows + 1),
        'timestamp': dates,
        'hour': [d.hour for d in dates],
        'day_of_week': [d.strftime('%A') for d in dates],
        'platform': np.random.choice(['Instagram', 'VK', 'Telegram', 'TikTok'], num_rows),
        'post_type': np.random.choice(['Video', 'Image', 'Text', 'Story'], num_rows),
        'views': np.random.randint(100, 10000, num_rows),
        'likes': np.random.randint(10, 2000, num_rows),
        'reposts': np.random.randint(0, 500, num_rows)
    }
    
    df = pd.DataFrame(data)
    
    # Создаем папку data, если её нет
    os.makedirs('data', exist_ok=True)
    
    # Сохраняем
    file_path = 'data/social_media.csv'
    df.to_csv(file_path, index=False)
    print(f" Файл {file_path} успешно создан (строк: {num_rows})")

if __name__ == "__main__":
    generate_social_data()