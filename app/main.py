from fastapi import FastAPI
from fastapi.responses import FileResponse
import time


# Экземпляр FactAPI.
app = FastAPI()



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