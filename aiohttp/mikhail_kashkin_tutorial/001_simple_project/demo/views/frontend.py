import aiohttp
from aiohttp_jinja2 import template


@template('index.html')
async def index(request):
    return {}


# async def index(request):
#     return aiohttp.web.Response(text='OK')
