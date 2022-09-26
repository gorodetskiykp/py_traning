# не стоит пытаться тестировать таким способом

import asyncio

def test_coro():
    loop = asyncio.get_event_loop()

    @asyncio.coroutine
    def do_test():
        yield from asyncio.sleep(0.1, loop=loop)
        assert 0  # onoes!

    loop.run_until_complete(do_test())