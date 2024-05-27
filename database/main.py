from sqlalchemy import create_engine, Column, Integer, String, DATETIME
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database, database_exists
from datetime import datetime

class WorkDatabase:
    """
    Класс для работы с базой данных.
    """
    def __init__(self) -> None:
        SQLALCHEMY_DATABASE_URL = 'sqlite:///./database.db'
        Base = declarative_base()
        engine = create_engine(SQLALCHEMY_DATABASE_URL)
        SessionLocal = sessionmaker(autoflush=False, bind=engine)
        
        if not database_exists(engine.url):
            create_engine(engine.url)

        # TODO добавить проверку наличия таблицы перед созданием.
        
        class Users(Base):
            """
            Таблица пользователя.
            """
            __tablename__ = 'users'

            id = Column(Integer, primary_key=True, index=True)
            name = Column(String, index=True, unique=True)
            datetime_create = Column(DATETIME, default=datetime.now)
            value = Column(Integer, default=0)
            total_time = Column(Integer, default=0)
            
