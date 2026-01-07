import asyncio


# define a coroutine that simulates a time-consuming task
async def fetch_data(delay, id):
    print("Fetching data... id:", id)
    await asyncio.sleep(delay) # simulate an I/O operation with a sleep
    print("Data fetched, id:", id)
    return {"data": "some data", "id": id}

# dfeine another coroutine that calls the first coroutine

async def main():
    print("Start of main coroutine")
    task1 = fetch_data(2, 1)
    task2 = fetch_data(2, 2)
    # Await the fetch_data coroutine, pausing execution of main until
    # fetch_data completes
    result1 = await task1
    print(f"Received result: {result1}")
    result2 = await task2
    print(f"Received result: {result2}")


    print("End of main coroutine")

# Run the main coroutine
asyncio.run(main())

#print(main())
