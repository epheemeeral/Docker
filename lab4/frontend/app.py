import streamlit as st
import requests
import pandas as pd
import os
from datetime import date

# Адрес бэкенда из переменной окружения
BACKEND_URL = os.getenv("BACKEND_URL", "http://backend-service:8000")

st.set_page_config(page_title="Shift Schedule Manager", layout="wide")

st.title("📅 Shift Schedule Management System")
st.markdown("### Управление графиком смен сотрудников")

# Sidebar для навигации
menu = st.sidebar.selectbox("Меню", ["Просмотр смен", "Добавить смену", "Удалить смену"])

# Функция для получения всех смен
def get_all_shifts():
    try:
        response = requests.get(f"{BACKEND_URL}/shifts", timeout=5)
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Ошибка API: {response.status_code}")
            return []
    except Exception as e:
        st.error(f"Не удается подключиться к бэкенду: {BACKEND_URL}")
        st.error(f"Детали: {e}")
        return []

# Функция для добавления смены
def add_shift(employee_name, shift_date, shift_type):
    try:
        payload = {
            "employee_name": employee_name,
            "shift_date": shift_date.isoformat(),
            "shift_type": shift_type
        }
        response = requests.post(f"{BACKEND_URL}/shifts", json=payload, timeout=5)
        return response.status_code == 200, response.json() if response.status_code == 200 else None
    except Exception as e:
        return False, str(e)

# Функция для удаления смены
def delete_shift(shift_id):
    try:
        response = requests.delete(f"{BACKEND_URL}/shifts/{shift_id}", timeout=5)
        return response.status_code == 200
    except Exception as e:
        return False

# Просмотр смен
if menu == "Просмотр смен":
    st.subheader("📋 Все смены")
    
    col1, col2 = st.columns([1, 3])
    
    with col1:
        if st.button("🔄 Обновить данные", use_container_width=True):
            st.rerun()
    
    # Получаем данные
    shifts_data = get_all_shifts()
    
    if shifts_data:
        # Создаем список уникальных сотрудников для фильтра
        employees = list(set([s["employee_name"] for s in shifts_data]))
        employees.sort()
        employees.insert(0, "Все сотрудники")
        
        with col2:
            selected_employee = st.selectbox("Фильтр по сотруднику", employees)
        
        # Применяем фильтр
        if selected_employee != "Все сотрудники":
            shifts_data = [s for s in shifts_data if s["employee_name"] == selected_employee]
        
        # Конвертируем в DataFrame для отображения
        df = pd.DataFrame(shifts_data)
        
        # Преобразуем дату
        df["shift_date"] = pd.to_datetime(df["shift_date"]).dt.date
        
        # Создаем понятные названия для типов смен
        df["shift_type_display"] = df["shift_type"].map({"morning": "🌅 Утро", "evening": "🌙 Вечер"})
        
        # Переименовываем колонки для отображения
        df_display = df.rename(columns={
            "id": "ID",
            "employee_name": "Сотрудник",
            "shift_date": "Дата",
            "shift_type_display": "Тип смены"
        })
        
        # Выбираем только нужные колонки для отображения
        df_display = df_display[["ID", "Сотрудник", "Дата", "Тип смены"]]
        
        st.dataframe(df_display, use_container_width=True, hide_index=True)
        
        # Статистика
        st.subheader("📊 Статистика")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Всего смен", len(shifts_data))
        with col2:
            morning_count = len([s for s in shifts_data if s["shift_type"] == "morning"])
            st.metric("Утренние смены", morning_count)
        with col3:
            evening_count = len([s for s in shifts_data if s["shift_type"] == "evening"])
            st.metric("Вечерние смены", evening_count)
    else:
        st.info("Нет данных о сменах. Добавьте первую смену!")

# Добавление смены
elif menu == "Добавить смену":
    st.subheader("➕ Добавить новую смену")
    
    with st.form("add_shift_form"):
        employee_name = st.text_input("ФИО сотрудника", placeholder="Иванов Иван Иванович")
        shift_date = st.date_input("Дата смены", value=date.today())
        shift_type = st.selectbox("Тип смены", options=["morning", "evening"], 
                                   format_func=lambda x: "🌅 Утренняя смена" if x == "morning" else "🌙 Вечерняя смена")
        
        submitted = st.form_submit_button("✅ Добавить смену", use_container_width=True)
        
        if submitted:
            if not employee_name.strip():
                st.error("Пожалуйста, введите ФИО сотрудника")
            else:
                success, result = add_shift(employee_name.strip(), shift_date, shift_type)
                if success:
                    st.success(f"Смена для {employee_name} на {shift_date} успешно добавлена!")
                    st.rerun()
                else:
                    st.error(f"Ошибка при добавлении: {result}")

# Удаление смены
elif menu == "Удалить смену":
    st.subheader("🗑️ Удалить смену")
    
    shifts_data = get_all_shifts()
    
    if shifts_data:
        # Сортируем по дате
        shifts_data.sort(key=lambda x: x["shift_date"])
        
        # Создаем опции для выбора с понятным отображением
        shift_options = {}
        for s in shifts_data:
            shift_type_display = "Утро" if s["shift_type"] == "morning" else "Вечер"
            display_text = f"ID:{s['id']} | {s['employee_name']} | {s['shift_date']} | {shift_type_display}"
            shift_options[display_text] = s['id']
        
        selected_shift_display = st.selectbox("Выберите смену для удаления", list(shift_options.keys()))
        selected_shift_id = shift_options[selected_shift_display]
        
        if st.button("🗑️ Удалить выбранную смену", type="secondary", use_container_width=True):
            if delete_shift(selected_shift_id):
                st.success("Смена успешно удалена!")
                st.rerun()
            else:
                st.error("Ошибка при удалении смены")
    else:
        st.info("Нет смен для удаления")