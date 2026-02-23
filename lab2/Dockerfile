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
