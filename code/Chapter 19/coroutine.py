import asyncio


# define a coroutine that simulates a time-consuming task
async def fetch_data(delay, task_id):
    print("Fetching data... id:", task_id)
    await asyncio.sleep(delay) # simulate an I/O operation with a sleep
    print("Data fetched, id:", task_id)
    return {"data": "some data", "id": task_id}

# define another coroutine that calls the first coroutine

async def main():
    print("Start of main coroutine")
    # Run both tasks concurrently using asyncio.gather()
    result1, result2 = await asyncio.gather(
        fetch_data(2, 1),
        fetch_data(2, 2)
    )
    print(f"Received result: {result1}")
    print(f"Received result: {result2}")
    print("End of main coroutine")

# Run the main coroutine
asyncio.run(main())
