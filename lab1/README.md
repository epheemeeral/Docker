# Лабораторная работа 1. 1. Установка и настройка Docker. Работа с контейнерами в Docker

## Цель работы
Освоить процесс установки и настройки Docker, научиться работать с основными командами CLI, контейнерами и образами. Понять принципы контейнеризации для развертывания аналитических сред и сервисов.

## Ход работы
1. Проверка установки
<img width="574" height="447" alt="image" src="https://github.com/user-attachments/assets/284ff0c6-5556-4aa0-bc65-d4b48db3ac5a" />

2. Знакомство с командами Docker CLI
<img width="720" height="143" alt="image" src="https://github.com/user-attachments/assets/b89539f0-08db-4366-b9ae-c50436508e90" />

## Индивидуальное задание 
### Вариант 17
minio/minio	
S3 Хранилище (Data Lake). Запустить контейнер командой server /data. Настроить доступ в консоль, зайти в веб-интерфейс и создать "бакет" (bucket) для файлов.

1. Установка и запуск minio
<img width="564" height="310" alt="image" src="https://github.com/user-attachments/assets/52fc05c8-2ea8-497b-866e-840bbe85763f" />

<img width="1432" height="853" alt="image" src="https://github.com/user-attachments/assets/2035228b-d60a-40a0-9f9c-0b8416e54523" />


2. Создание бакета
<img width="744" height="219" alt="image" src="https://github.com/user-attachments/assets/6cd34851-81ab-47e1-9754-b1e000674941" />

<img width="1440" height="778" alt="image" src="https://github.com/user-attachments/assets/f0d79067-2488-48e5-8c85-4617fbd43f36" />

3. Остановка и повторный запуск контейнера (+ проверка)

<img width="1159" height="142" alt="image" src="https://github.com/user-attachments/assets/b964d77c-53b6-436b-bf47-b0bf2843a5fc" />

### Перечень использованных команд:
1) docker --version
2) docker run hello-world
3) docker images
4) docker ps
5) docker ps -a
6) docker run -d \
  --name minio-server \
  -p 9000:9000 \
  -p 9001:9001 \
  -e "MINIO_ROOT_USER=admin" \
  -e "MINIO_ROOT_PASSWORD=password123" \
  minio/minio server /data --console-address ":9001"
7) docker stop minio-server
8) docker start minio-server

  ## Вывод




