from fastapi import FastAPI, Request
import uvicorn
from fastapi.responses import FileResponse
from contextlib import asynccontextmanager
import time

from database.base import Base, engine


from routers import user as UserRouter

Base.metadata.create_all(bind=engine)


# Экземпляр FactAPI.
app = FastAPI()
# Маршрутизация пользователя.
app.include_router(UserRouter.router, prefix='/user')



@app.get('/')
async def page_main():
    """
    Главная страница.
    """
    return FileResponse('templates/base/index.html')


@app.get('/about')
async def page_about():
    """
    Страница о проекте.
    """
    return {'message': 'Информационная страница'}


@app.get('/stats')
async def page_stats():
    """
    Страница статистики.
    """
    simply_time = int(time.time())
    return {'message': f'Проведено времени на трансляции {simply_time}! секунд'}


@app.post('/send_event')
async def page_event(event_id: int):
    """
    Страница отправки события игроку.
    """
    return {'message': f'Создано событие {event_id}'}

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port='8080')