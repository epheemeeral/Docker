# Лабораторная работа 4.1
## Создание и развертывание полнофункционального приложения
### Вариант 17: Shift Schedule (График смен сотрудников)

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

---

<img width="1435" height="850" alt="image" src="https://github.com/user-attachments/assets/6d3d4cce-584c-4e0c-962f-ba1d6f70ded4" />
<img width="1432" height="854" alt="image" src="https://github.com/user-attachments/assets/474f486f-be15-4f1b-9ae9-c990866051ae" />
<img width="1434" height="560" alt="image" src="https://github.com/user-attachments/assets/886be477-d352-4724-b014-292e77ddbad9" />

<img width="732" height="900" alt="image" src="https://github.com/user-attachments/assets/d7feab9a-5aa2-47d9-a790-e4fc9ca8ceaf" />
<img width="1110" height="632" alt="image" src="https://github.com/user-attachments/assets/0f4bc4e3-6f47-48ef-8c7c-d9fa66027cba" />

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
```


## Вывод

В ходе выполнения лабораторной работы было успешно разработано и развернуто полнофункциональное трехзвенное приложение «Shift Schedule Management System» для управления графиком смен сотрудников.
