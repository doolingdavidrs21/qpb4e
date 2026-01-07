import asyncio


# define a coroutine that simulates a time-consuming task
async def fetch_data(delay):
    print("Fetching data...")
    await asyncio.sleep(delay) # simulate an I/O operation with a sleep
    print("Data fetched")
    return {"data": "some data"}

# dfeine another coroutine that calls the first coroutine

async def main():
    print("Start of main coroutine")
    task = fetch_data(2)
    # Await the fetch_data coroutine, pausing execution of main until
    # fetch_data completes
    result = await task
    print(f"Received result: {result}")
    print("End of main coroutine")

# Run the main coroutine
asyncio.run(main())

#print(main())
