import asyncio

import logging


async def simple_coroutine(number:int):
   
    print("test 123")

    await asyncio.sleep(1)

    print(f"coroutine {number} has finished executing")
    # logging.info(f"coroutine {number} has finished executing")
