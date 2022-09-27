import aiohttp
from demo.app import create_app


app = create_app()


if __name__ == '__main__':
    aiohttp.web.run_app(app, host='127.0.0.1')
