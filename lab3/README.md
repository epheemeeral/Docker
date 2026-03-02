# Лабораторная работа 3.1. Развертывание приложения в Kubernetes

## Цель работы
Освоить процесс оркестрации контейнеров. Научиться разворачивать связки сервисов (аналитическое приложение + база данных/интерфейс) в кластере Kubernetes, управлять их масштабированием (Deployment) и сетевой доступностью (Service).

## Вариант	- 17

Основной сервис (App)	- Nginx (Custom)

Вспомогательный сервис (DB/Tool) - Static HTML

Задача - Развернуть Nginx, который отдает аналитический отчет (ConfigMap с HTML-файлом смонтировать в /usr/share/nginx/html).

## Ход работы

Шаг 1. Создание директории проекта

<img width="299" height="49" alt="image" src="https://github.com/user-attachments/assets/7212b8db-1bf5-4db9-815a-f0ce113328e2" />


Шаг 2. Проверка состояния кластера

<img width="1440" height="900" alt="image" src="https://github.com/user-attachments/assets/04d27a1f-a599-4d41-b0f9-da6035144ac0" />

<img width="661" height="214" alt="image" src="https://github.com/user-attachments/assets/dce5c5ba-e5aa-48e9-baf9-a45e07705669" />


Шаг 3. Создание ConfigMap

<img width="788" height="381" alt="image" src="https://github.com/user-attachments/assets/d025b806-8f8f-4ec2-9823-fcd768cc3917" />


Шаг 4. Создание Deployment

<img width="480" height="396" alt="image" src="https://github.com/user-attachments/assets/b01a58cb-5ee0-487c-a8cb-2d4fbf9f7985" />


Шаг 5. Создание Service

<img width="474" height="195" alt="image" src="https://github.com/user-attachments/assets/54e2914d-1fa5-4d58-9b38-c8676e3329ae" />


Шаг 6. Запуск сервисов

<img width="835" height="58" alt="image" src="https://github.com/user-attachments/assets/82e8d53e-bebc-44a4-b64f-09cb09fee6ff" />


Шаг 7. Проверка доступности

<img width="554" height="104" alt="image" src="https://github.com/user-attachments/assets/d4deecb0-1e0b-464f-a854-a0a7ca92dd6f" />


Переходим на http://localhost:30017

<img width="806" height="402" alt="image" src="https://github.com/user-attachments/assets/4200dad4-af6b-43c5-9c1f-7338e984e2e6" />


## Вывод

Kubernetes значительно упрощает развертывание аналитики, позволяя гибко управлять конфигурациями через декларативные манифесты и обеспечивая быструю публикацию сервисов во внешнюю сеть.
