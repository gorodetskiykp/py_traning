from aiohttp import web
import aiohttp_jinja2
import jinja2

from settings import config, BASE_DIR
from routes import setup_routes
from db import pg_context
from middlewares import setup_middlewares


app = web.Application()
app['config'] = config
aiohttp_jinja2.setup(app,
    loader=jinja2.FileSystemLoader(str(BASE_DIR / 'aiohttpdemo_polls' / 'templates')))

setup_routes(app)
setup_middlewares(app)
app.cleanup_ctx.append(pg_context)
web.run_app(app)