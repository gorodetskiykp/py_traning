from aiohttp import web  # основной модуль aiohttp
import jinja2  # шаблонизатор jinja2
import aiohttp_jinja2  # адаптация jinja2 к aiohttp

from app.store.database.accessor import PostgresAccessor
from app.settings import config, BASE_DIR


def setup_accessors(application):
    application['db'] = PostgresAccessor()
    application['db'].setup(application)


def setup_config(application):
    application["config"] = config


# в этой функции производится настройка url-путей для всего приложения
def setup_routes(application):
    from app.forum.routes import setup_routes as setup_forum_routes
    setup_forum_routes(application)  # настраиваем url-пути приложения forum


def setup_external_libraries(application: web.Application) -> None:
    # указываем шаблонизатору, что html-шаблоны надо искать в папке templates
    aiohttp_jinja2.setup(
        application,
        loader=jinja2.FileSystemLoader(BASE_DIR / "templates")
    )


def setup_app(application):
    # настройка всего приложения состоит из:
    setup_config(application)
    setup_accessors(application)
    setup_external_libraries(application)  # настройки внешних библиотек, например шаблонизатора
    setup_routes(application)  # настройки роутера приложения


app = web.Application()  # создаем наш веб-сервер

if __name__ == "__main__":  # эта строчка указывает, что данный файл можно запустить как скрипт
    setup_app(app)  # настраиваем приложение
    web.run_app(app, host=config['common']['host'], port=config['common']['port'])  # запускаем приложение
