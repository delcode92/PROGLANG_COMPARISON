import asyncio

async def task1():
    print("Task 1 started")
    await asyncio.sleep(2)  # Pause task1, and allow other tasks to run
    print("Task 1 finished")

async def task2():
    print("Task 2 started")
    await asyncio.sleep(1)  # Pause task2 for 1 second
    print("Task 2 finished")

async def main():
    await asyncio.gather(task1(), task2())  # Run both tasks concurrently

asyncio.run(main())

