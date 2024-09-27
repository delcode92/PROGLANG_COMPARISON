import asyncio

from coroutines import simple_coroutine

# asyncio.run(simple_coroutine(1))

asyncio.gather(
    simple_coroutine(1),
    simple_coroutine(2),
    simple_coroutine(3)
)
