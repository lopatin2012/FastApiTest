from sqlalchemy import create_engine, Column, Integer, String, DATETIME
from database.base import Base
from datetime import datetime


class User(Base):
    """
    Таблица пользователя.
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, unique=True)
    datetime_create = Column(DATETIME, default=datetime.now)
    value = Column(Integer, default=0)
    total_time = Column(Integer, default=0)