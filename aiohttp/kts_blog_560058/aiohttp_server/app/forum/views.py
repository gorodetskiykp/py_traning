import aiohttp_jinja2
from aiohttp import web
from app.forum.models import Message


# создаем функцию, которая будет отдавать html-файл
@aiohttp_jinja2.template("index.html")
async def index(request):
    return {'title': 'Пишем первое приложение на aiohttp'}


class ListMessageView(web.View):
    async def get(self):
        messages = await Message.query.order_by(Message.id.desc()).gino.all()
        messages_data = []
        for message in messages:
            messages_data.append({
                "id": message.id,
                "text": message.text,
                "created": str(message.created),
            })

        return web.json_response(data={'messages': messages_data})