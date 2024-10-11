import asyncio
import time

def without_coroutine(number:int):
    print(f"Starting task {number}")
    time.sleep(number)
    print(f"task {number} has finished executing")

# coroutine
async def simple_coroutine(number: int):
    print(f"Starting coroutine {number}")
    

    await asyncio.sleep(number)
    
    print(f"Coroutine {number} has finished executing")


async def main():
    print("\n")


    #without async coroutine
    without_coroutine(5)
    without_coroutine(3)
    without_coroutine(1)

    # await asyncio.gather(
    #     
    #     simple_coroutine(5),
    #     
    #     simple_coroutine(3),
    #     
    #     simple_coroutine(1)
    # 
    # )



start_time = time.time()

# Run the main coroutine
asyncio.run(main())
print("--- %s seconds ---" % (time.time() - start_time))

