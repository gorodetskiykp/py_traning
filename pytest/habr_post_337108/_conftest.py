# tests/conftest.py

import asyncio
import pytest


@pytest.yield_fixture
def loop():
    # Настройка
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    yield loop

    # Очистка
    loop.close()


# tests/test_coros.py

def test_coro(loop):
    @asyncio.coroutine
    def do_test():
        yield from asyncio.sleep(0.1, loop=loop)
        assert 0  # onoes!

    loop.run_until_complete(do_test())