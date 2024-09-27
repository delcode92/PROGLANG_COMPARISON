import asyncio
import logging

async def simple_coroutine(number: int):
    print(f"Starting coroutine {number}")
    await asyncio.sleep(1)
    print(f"Coroutine {number} has finished executing")

async def main():
    await asyncio.gather(
        simple_coroutine(1),
        simple_coroutine(2),
        simple_coroutine(3)
    )

# Run the main coroutine
asyncio.run(main())

