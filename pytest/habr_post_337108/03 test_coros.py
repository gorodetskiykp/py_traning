import asyncio
import time

import pytest

@pytest.mark.asyncio
async def test_coro(event_loop):
    before = time.monotonic()
    await asyncio.sleep(0.1, loop=event_loop)
    after = time.monotonic()
    assert after - before >= 0.1