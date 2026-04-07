# Лабораторная работа 4.1
## Создание и развертывание полнофункционального приложения
### Вариант 17: Shift Schedule (График смен сотрудников)

**Студент:** [Введите ФИО]  
**Группа:** [Введите группу]  
**Дата:** Апрель 2026  
**Платформа:** MacBook Air M1 + Docker Desktop + Kubernetes

---

## 📌 Цель работы

Применить полученные знания по созданию и развертыванию трехзвенного приложения (Frontend + Backend + Database) в кластере Kubernetes. Научиться организовывать взаимодействие между микросервисами.

---

## 🏗 Архитектура приложения

Приложение построено по трехзвенной архитектуре:

| Компонент | Технология | Порт | Тип доступа |
|-----------|------------|------|-------------|
| Frontend | Streamlit | 8501 | NodePort:30080 |
| Backend | FastAPI | 8000 | ClusterIP |
| Database | PostgreSQL 15 | 5432 | ClusterIP |

**Схема взаимодействия:**
- Пользователь → Frontend (через порт 30080)
- Frontend → Backend API (HTTP запросы)
- Backend → PostgreSQL (CRUD операции)
- Данные сохраняются в Persistent Volume

**Модель данных (Shift):**
- ID — уникальный идентификатор
- Employee name — ФИО сотрудника
- Shift date — дата смены
- Shift type — тип смены (morning/evening)

---

## 🛠 Технологический стек

| Компонент | Технологии |
|-----------|------------|
| Backend | Python 3.11, FastAPI, SQLAlchemy, Pydantic, Uvicorn |
| Frontend | Python 3.11, Streamlit, Requests, Pandas |
| Database | PostgreSQL 15 |
| Оркестрация | Docker, Kubernetes, kubectl |

---

## 📝 Функциональность

### Backend API (5 эндпоинтов)

| Метод | Endpoint | Описание |
|-------|----------|----------|
| GET | /health | Проверка работоспособности |
| GET | /shifts | Получение всех смен |
| GET | /shifts/employee/{name} | Смены сотрудника |
| POST | /shifts | Добавление смены |
| DELETE | /shifts/{id} | Удаление смены |

### Frontend UI (3 раздела)

1. **Просмотр смен** — таблица, фильтр по сотруднику, статистика
2. **Добавление смены** — форма с валидацией
3. **Удаление смены** — выпадающий список с выбором

---

## 🐳 Контейнеризация

### Сборка образов

```bash
# Backend
cd src/backend
docker build --platform linux/arm64 -t shift-backend:latest .

# Frontend
cd src/frontend
docker build --platform linux/arm64 -t shift-frontend:latest .
