# Лабораторная работа 2.1. Создание Dockerfile и сборка образа

## Цель работы
Научиться разрабатывать воспроизводимые аналитические инструменты. Студенту необходимо пройти полный цикл: от написания Python-скрипта для обработки бизнес-данных до его упаковки в Docker-образ и запуска в изолированной среде.


## Индивидуальное задание 

### Тематика данных 

Вариант 7	

Social Media - ID поста, количество лайков, репостов, длина текста, тональность (positive/negative).


### Техническое задание

Вариант 17	

Jupyter Notebook - Собрать образ с предустановленным Jupyter и библиотеками (Pandas, Seaborn). CMD должен запускать Jupyter Lab без токена.


## Ход работы

### Этап 1. Написание аналитического сервиса

Создадим структуру проекта:

<img width="422" height="46" alt="image" src="https://github.com/user-attachments/assets/6e19b104-3b96-4c86-bec2-13518ae05875" />

<img width="492" height="31" alt="image" src="https://github.com/user-attachments/assets/8406bac5-d766-4f0f-8c68-9ed23b29e680" />

Файл main.py. Генерирует синтетический набор данных по активности в социальных сетях и рассчитывает метрику вовлеченности (likes + reposts) с помощью библиотеки Pandas. Используя Seaborn, строит и сохраняет график зависимости вовлеченности от тональности текста
```
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import random

# Генерация данных по теме Social Media
data = {
    'post_id': range(1, 101),
    'likes': [random.randint(0, 1000) for _ in range(100)],
    'reposts': [random.randint(0, 200) for _ in range(100)],
    'text_length': [random.randint(10, 500) for _ in range(100)],
    'sentiment': [random.choice(['positive', 'negative']) for _ in range(100)]
}
df = pd.DataFrame(data)
df['engagement'] = df['likes'] + df['reposts']

# Визуализация
plt.figure(figsize=(10, 6))
sns.barplot(x='sentiment', y='engagement', data=df, palette='viridis')
plt.title('Engagement Analysis (Variant 17)')
plt.savefig('/app/result.png')
print("Анализ выполнен, график сохранен как result.png")
```
<img width="554" height="317" alt="image" src="https://github.com/user-attachments/assets/e1ce1b4b-30d1-4b2a-b3e7-a8b909506673" />

<img width="551" height="355" alt="image" src="https://github.com/user-attachments/assets/1bf68a45-2001-4152-b79d-c484d29eb9c1" />

Файл requirements.txt:

<img width="200" height="98" alt="image" src="https://github.com/user-attachments/assets/c02dbc17-f4e3-4bdc-a908-22c32760e3a0" />

<img width="469" height="100" alt="image" src="https://github.com/user-attachments/assets/c2541e30-cd98-4db3-a777-8b07fdbb63aa" />


### Этап 2. Создание Dockerfile

```
# Используем официальный Python
FROM python:3.9-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем и устанавливаем зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем код в контейнер
COPY app/ /app/

# Открываем порт для Jupyter
EXPOSE 8888

# Запуск Jupyter Lab без токена и пароля (ТЗ вариант 17)
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--NotebookApp.token=''", "--NotebookApp.password=''"]
```

<img width="989" height="298" alt="image" src="https://github.com/user-attachments/assets/c313e952-63da-4080-b123-05f07a99fcda" />

<img width="602" height="284" alt="image" src="https://github.com/user-attachments/assets/05ac5219-afb3-4d7b-bb01-a9f433917f2c" />


### Этап 3. Сборка и проверка

Сборка образа:

<img width="1438" height="270" alt="image" src="https://github.com/user-attachments/assets/745be69d-e043-4de8-8dcf-453fedf936c3" />


Запуск контейнера:

<img width="699" height="47" alt="image" src="https://github.com/user-attachments/assets/a14403c9-8a50-49db-923d-f3dcc965da61" />


Проверка:

<img width="489" height="95" alt="image" src="https://github.com/user-attachments/assets/6fde12ed-6be5-42ec-838d-4be406ce74d9" />


Переходим по адресу http://localhost:8888:

<img width="1435" height="857" alt="image" src="https://github.com/user-attachments/assets/14ee3463-c6b1-4b93-8801-e6c1cfd31164" />


Запускаем скрипт main.py через терминал:

<img width="1440" height="233" alt="image" src="https://github.com/user-attachments/assets/23b6fdba-de59-4224-af22-ee9e58923e75" />


Получили график, на котором видно, что позитивные посты собирают больше лайков и репостов:

<img width="1440" height="656" alt="image" src="https://github.com/user-attachments/assets/5c777025-54e7-40b3-af7c-bb8e78abdd57" />






