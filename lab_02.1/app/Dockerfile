FROM python:3.10-slim

# Установка системных зависимостей
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Создаем пользователя и его домашнюю директорию
RUN useradd -m -u 1000 appuser

WORKDIR /app

# Даем права на рабочую директорию
RUN chown appuser:appuser /app

COPY requirements.txt .

RUN pip install --no-cache-dir --default-timeout=1000 -r requirements.txt

COPY . .
RUN chown -R appuser:appuser /app

# Переключаемся на пользователя
USER appuser

# Указываем домашнюю директорию как рабочую для Jupyter, 
# чтобы у него был доступ к .local папкам
ENV HOME=/home/appuser

EXPOSE 8501
EXPOSE 8888

CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--ServerApp.token=''", "--ServerApp.password=''"]
