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

Создадим структуру проекта:

<img width="254" height="284" alt="image" src="https://github.com/user-attachments/assets/2a00020b-e5a8-41a6-bbff-855b5d257e37" />

Сборка образа, запуск и проверка:

Сборка:

<img width="907" height="566" alt="image" src="https://github.com/user-attachments/assets/11f089a1-6db1-4f16-92e1-d99a001246fe" />

Запуск:

<img width="901" height="117" alt="image" src="https://github.com/user-attachments/assets/b0ed0075-61b4-4de4-93c0-bc0cee9bd7c5" />

Проверка:

<img width="901" height="144" alt="image" src="https://github.com/user-attachments/assets/bf9766d0-4078-4cd2-a0b5-91c0e2f3a50f" />

Переходим на http://localhost:9000/ 

<img width="1440" height="854" alt="image" src="https://github.com/user-attachments/assets/2397c468-6ef9-4b28-9948-c7eaed45bd3b" />

Переходим на http://localhost:8501/

<img width="1440" height="853" alt="image" src="https://github.com/user-attachments/assets/9efeba73-8915-44ef-8845-fba78a00b8b6" />

<img width="1440" height="851" alt="image" src="https://github.com/user-attachments/assets/9d85cd83-0974-41ed-89fb-9b972785ccb9" />


## Для запуска
docker compose build
docker compose up -d
docker compose ps
http://localhost:9000/
http://localhost:8501/


## Выводы 
