from fastapi import FastAPI, Request
import uvicorn
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from contextlib import asynccontextmanager
import time
import os

from database.base import Base, engine


from routers import user as UserRouter

Base.metadata.create_all(bind=engine)


# Экземпляр FactAPI.
app = FastAPI(debug=True)
# Маршрутизация пользователя.
app.include_router(UserRouter.router, prefix='/user')
# Статические файлы.
app.mount('/static', StaticFiles(directory='static'), name='static')
# Директория с шаблонами.
templates = Jinja2Templates(directory='templates')


@app.get('/', tags=['page'], response_class=HTMLResponse)
async def page_main(request: Request):
    """
    Главная страница.
    """
    test = 1
    context = {
        'title': 'Название страницы',
    }
    return templates.TemplateResponse(
        request=request, name='main_menu/main.html', context=context
    )


@app.get('/about', tags=['page'])
async def page_about():
    """
    Страница о проекте.
    """
    return {'message': 'Информационная страница'}


@app.get('/stats', tags=['page'])
async def page_stats():
    """
    Страница статистики.
    """
    simply_time = int(time.time())
    return {'message': f'Проведено времени на трансляции {simply_time}! секунд'}


@app.post('/send_event', tags=['page'])
async def page_event(event_id: int):
    """
    Страница отправки события игроку.
    """
    return {'message': f'Создано событие {event_id}'}


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port='8080')