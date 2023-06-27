# док-ция fsatapi users: https://fastapi-users.github.io/fastapi-users/11.0/configuration/authentication/strategies/jwt/

from typing import AsyncGenerator

from fastapi import Depends
from fastapi_users.db import SQLAlchemyBaseUserTableUUID, SQLAlchemyUserDatabase, SQLAlchemyBaseUserTable
from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey, Boolean
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
# from sqlalchemy.orm import DeclarativeBase#это нужно в случае если будем юзать класс Base вместо Base: DeclarativeMeta
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base

from config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER

# DATABASE_URL = "sqlite+aiosqlite:///./test.db"
DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
Base: DeclarativeMeta = declarative_base()#это типа как метаданнные для накопления инфы в базе



# class Base(DeclarativeBase):
#     pass


# class User(SQLAlchemyBaseUserTableUUID, Base):#SQLAlchemyBaseUserTableUUID это если нет ID. В нашем случае есть простой ID в базе
#     pass

class User(SQLAlchemyBaseUserTable[int], Base):#вместо SQLAlchemyBaseUserTableUUID юзаем SQLAlchemyBaseUserTable и он также импортируем из fastapi_users.db. В нем уже есть какие-то поля их лучше оставить, они пойдут в базу, и создаем класс который наследует все эти поля для таблицы базы. Нужно будет в файле models.py поменять поля как в видео
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=True)
    username = Column(String, nullable=True)
    registered_at = Column(TIMESTAMP, default=datetime.utcnow)
    role_id = Column(Integer, ForeignKey(role.c.id))
    hashed_password: str = Column(String(length=1024), nullable=False)
    is_active: bool = Column(Boolean, default=True, nullable=False)
    is_superuser: bool = Column(Boolean, default=False, nullable=False)
    is_verifies: bool = Column(Boolean, default=False, nullable=False)




engine = create_async_engine(DATABASE_URL)#engine это точка входа алхимии в наше приложение
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)#далее создаются сессии с помощью этого движка

#это функция для создания таблиц. По курсу не используем. Но берем на заметку
# async def create_db_and_tables():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)

#эта функция для получения сессии, типа генератор через менеджер конекста
async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session

#тут функция возвращает таблицу, тоже как генератор
async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)
# Depends это функция из фреймоворка фастапи, отвечает за инъекция зависимостей. ТО есть результат других функций мы тут используем. ТО есть параметр в Depends это функция get_async_session. То есть получается когда будет срабатывать функция get_user_db, то в ней будут указываться параметры из функции get_async_session, и их нужно будет передавать, это будет видно в документации фастапи




