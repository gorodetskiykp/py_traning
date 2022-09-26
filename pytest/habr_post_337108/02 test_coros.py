import asyncio


@asyncio.coroutine  # DeprecationWarning: "@coroutine" decorator is deprecated since Python 3.8, use "async def" instead
def test_coro(loop):
    yield from asyncio.sleep(0.1, loop=loop)
    assert 0