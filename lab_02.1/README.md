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

Внутри папки app:

- .dockerignore

```
__pycache__/
*.pyc
.git
venv/
.env
.DS_Store
data/
```

- dashboard.py
  
```
#!/usr/bin/env python3
"""
Streamlit-приложение: Аналитика вовлеченности в социальных сетях.
Вариант 17 — Анализ метрик постов (SMM / Social Media Analytics).
"""

import os
import pandas as pd
import plotly.express as px
import streamlit as st
from sqlalchemy import create_engine

# --- Настройки подключения к БД (берем из окружения) ---
DB_HOST = os.getenv("DB_HOST", "db")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("POSTGRES_DB", "social_analytics")
DB_USER = os.getenv("POSTGRES_USER", "admin")
DB_PASS = os.getenv("POSTGRES_PASSWORD", "password123")

@st.cache_data(ttl=300)
def load_data() -> pd.DataFrame:
    """Загрузка данных из PostgreSQL через SQLAlchemy."""
    conn_str = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    engine = create_engine(conn_str)
    df = pd.read_sql("SELECT * FROM social_metrics;", engine)
    return df

# --- Интерфейс ---
st.set_page_config(page_title="SMM Analytics: Вариант 17", layout="wide")
st.title("📊 Аналитика социальных сетей")
st.markdown("Визуализация вовлеченности пользователей по платформам и типам контента.")

try:
    df = load_data()
except Exception as e:
    st.error(f"Не удалось подключиться к БД: {e}")
    st.info("Проверьте, запущен ли контейнер db и прошел ли ETL-процесс (loader).")
    st.stop()

# --- Боковая панель (Фильтры) ---
st.sidebar.header("Фильтры")
platforms = st.sidebar.multiselect(
    "Выберите платформы", 
    options=sorted(df["platform"].unique()), 
    default=sorted(df["platform"].unique())
)
df_filtered = df[df["platform"].isin(platforms)]

# --- Основные метрики ---
col1, col2, col3, col4 = st.columns(4)
col1.metric("Всего постов", f"{len(df_filtered):,}")
col2.metric("Сумма лайков", f"{df_filtered['likes'].sum():,}")
col3.metric("Всего просмотров", f"{df_filtered['views'].sum():,}")
col4.metric("Ср. репостов", f"{df_filtered['reposts'].mean():.1f}")

# --- Визуализация 1: Heatmap (День недели × Час) ---
st.subheader("🔥 Карта активности: Когда пользователи ставят лайки?")

day_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
day_labels = {
    "Monday": "Пн", "Tuesday": "Вт", "Wednesday": "Ср",
    "Thursday": "Чт", "Friday": "Пт", "Saturday": "Сб", "Sunday": "Вс",
}

# Агрегируем лайки для тепловой карты
pivot_data = (
    df_filtered.groupby(["day_of_week", "hour"])["likes"]
    .mean()
    .reset_index()
)
pivot_data["day_of_week"] = pd.Categorical(pivot_data["day_of_week"], categories=day_order, ordered=True)
pivot_data = pivot_data.sort_values("day_of_week")
pivot_data["day_label"] = pivot_data["day_of_week"].map(day_labels)

heatmap = pivot_data.pivot(index="day_label", columns="hour", values="likes").fillna(0)
heatmap = heatmap.reindex([day_labels[d] for d in day_order])

fig_heat = px.imshow(
    heatmap,
    labels=dict(x="Час публикации", y="День недели", color="Средние лайки"),
    color_continuous_scale="Viridis",
    aspect="auto",
)
st.plotly_chart(fig_heat, use_container_width=True)

# --- Визуализация 2: Платформы vs Тип контента ---
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("Просмотры по платформам")
    fig_views = px.box(df_filtered, x="platform", y="views", color="platform",
                        labels={"platform": "Платформа", "views": "Просмотры"})
    st.plotly_chart(fig_views, use_container_width=True)

with col_right:
    st.subheader("Типы контента по популярности")
    content_types = df_filtered.groupby("post_type")["likes"].sum().reset_index()
    fig_pie = px.pie(content_types, values="likes", names="post_type", hole=0.4,
                     color_discrete_sequence=px.colors.qualitative.Pastel)
    st.plotly_chart(fig_pie, use_container_width=True)

# --- Финальная таблица ---
with st.expander("Посмотреть сырые данные"):
    st.dataframe(df_filtered.head(100), use_container_width=True)

st.caption("Данные: PostgreSQL (social_metrics) • Streamlit + Plotly")
```

