from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from typing import List
import os
import time
from datetime import date

# Ожидание готовности БД
time.sleep(5)

# Подключение к БД через переменные окружения
DB_USER = os.getenv("DB_USER", "user")
DB_PASSWORD = os.getenv("DB_PASSWORD", "password")
DB_HOST = os.getenv("DB_HOST", "postgres-service")
DB_NAME = os.getenv("DB_NAME", "shift_db")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Модель для БД
class Shift(Base):
    __tablename__ = "shifts"
    id = Column(Integer, primary_key=True, index=True)
    employee_name = Column(String, nullable=False)
    shift_date = Column(Date, nullable=False)
    shift_type = Column(String, nullable=False)  # "morning" или "evening"

# Создание таблиц
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Shift Schedule API")

# Pydantic модели для запросов/ответов
class ShiftCreate(BaseModel):
    employee_name: str
    shift_date: date
    shift_type: str

class ShiftResponse(ShiftCreate):
    id: int

    class Config:
        from_attributes = True

# API Endpoints
@app.get("/shifts", response_model=List[ShiftResponse])
def get_shifts():
    db = SessionLocal()
    shifts = db.query(Shift).order_by(Shift.shift_date).all()
    db.close()
    return shifts

@app.get("/shifts/employee/{employee_name}", response_model=List[ShiftResponse])
def get_shifts_by_employee(employee_name: str):
    db = SessionLocal()
    shifts = db.query(Shift).filter(Shift.employee_name == employee_name).order_by(Shift.shift_date).all()
    db.close()
    return shifts

@app.post("/shifts", response_model=ShiftResponse)
def create_shift(shift: ShiftCreate):
    db = SessionLocal()
    
    # Валидация типа смены
    if shift.shift_type not in ["morning", "evening"]:
        db.close()
        raise HTTPException(status_code=400, detail="Shift type must be 'morning' or 'evening'")
    
    new_shift = Shift(
        employee_name=shift.employee_name,
        shift_date=shift.shift_date,
        shift_type=shift.shift_type
    )
    db.add(new_shift)
    db.commit()
    db.refresh(new_shift)
    db.close()
    return new_shift

@app.delete("/shifts/{shift_id}")
def delete_shift(shift_id: int):
    db = SessionLocal()
    shift = db.query(Shift).filter(Shift.id == shift_id).first()
    if not shift:
        db.close()
        raise HTTPException(status_code=404, detail="Shift not found")
    db.delete(shift)
    db.commit()
    db.close()
    return {"message": "Shift deleted successfully"}

@app.get("/health")
def health_check():
    return {"status": "ok"}