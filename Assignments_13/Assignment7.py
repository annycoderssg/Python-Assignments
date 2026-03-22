# Multitasking with asyncio (Asynchronous I/O)
#
# Concepts demonstrated:
#   async def           : defines a coroutine function
#   await               : suspends coroutine and yields control to event loop
#   asyncio.run()       : entry point — runs the top-level coroutine
#   asyncio.sleep()     : non-blocking delay (simulates I/O wait)
#   asyncio.gather()    : run multiple coroutines concurrently, wait for all
#   asyncio.create_task(): schedule a coroutine without immediately awaiting it
#   asyncio.Queue       : async-safe producer-consumer queue
#
# Key difference from threads:
#   - asyncio is COOPERATIVE: a task must await to let others run
#   - Threads are PREEMPTIVE: the OS can switch them at any time
#   - asyncio is ideal for I/O-bound work (network, file); threads for CPU-bound

import asyncio
import time

# -----------------------------------------------------------------------
# PART 1: Basic coroutines and await
# -----------------------------------------------------------------------
async def GreetSlowly(strName, fltDelay):
    print("Hello,", strName, "— will respond in %.1fs" % fltDelay)
    await asyncio.sleep(fltDelay)       # non-blocking sleep
    print("Nice to meet you,", strName)

# -----------------------------------------------------------------------
# PART 2: asyncio.gather() — run coroutines concurrently
# -----------------------------------------------------------------------
async def FetchWebPage(strUrl, fltDelay):
    print("Fetching:", strUrl)
    await asyncio.sleep(fltDelay)       # simulate network I/O
    return "Response from " + strUrl

async def FetchAllPages():
    arrUrls = [
        ("https://example.com",   1.5),
        ("https://python.org",    0.5),
        ("https://github.com",    1.0),
        ("https://docs.python.org", 0.8),
    ]
    # All fetches run concurrently — total time ≈ max delay, not sum
    arrResults = await asyncio.gather(
        *[FetchWebPage(url, delay) for url, delay in arrUrls]
    )
    for strResult in arrResults:
        print(" ", strResult)

# -----------------------------------------------------------------------
# PART 3: asyncio.create_task() — fire-and-forget scheduling
# -----------------------------------------------------------------------
async def BackgroundJob(strName, intSteps):
    for i in range(1, intSteps + 1):
        await asyncio.sleep(0.3)
        print("  [%s] step %d/%d" % (strName, i, intSteps))

async def RunWithTasks():
    print("Scheduling background tasks...")
    objTaskA = asyncio.create_task(BackgroundJob("JobA", 3))
    objTaskB = asyncio.create_task(BackgroundJob("JobB", 4))

    print("Main coroutine doing other work while tasks run...")
    await asyncio.sleep(0.5)
    print("Main: still here, tasks running in background")

    await objTaskA          # wait for JobA to complete
    await objTaskB          # wait for JobB to complete
    print("Both background tasks finished")

# -----------------------------------------------------------------------
# PART 4: asyncio.Queue — async producer-consumer
# -----------------------------------------------------------------------
async def AsyncProducer(objQueue, intItems):
    for i in range(1, intItems + 1):
        await asyncio.sleep(0.2)        # simulate producing data
        await objQueue.put(i)
        print("Produced:", i)
    await objQueue.put(None)            # sentinel

async def AsyncConsumer(objQueue, strName):
    while True:
        intItem = await objQueue.get()
        if intItem is None:
            await objQueue.put(None)    # pass sentinel along
            print("%s: Done" % strName)
            break
        print("%s: Consumed %d" % (strName, intItem))
        objQueue.task_done()
        await asyncio.sleep(0.3)

# -----------------------------------------------------------------------
# Main async entry point
# -----------------------------------------------------------------------
async def main():
    print("=== PART 1: Basic coroutines with await ===")
    dblStart = time.perf_counter()
    # Sequential — each waits for the other
    await GreetSlowly("Alice", 1.0)
    await GreetSlowly("Bob",   0.5)
    print("Sequential time: %.2fs" % (time.perf_counter() - dblStart))

    print()
    print("=== PART 2: gather() — concurrent execution ===")
    dblStart = time.perf_counter()
    await FetchAllPages()
    print("Concurrent fetch time: %.2fs" % (time.perf_counter() - dblStart))

    print()
    print("=== PART 3: create_task() — background scheduling ===")
    await RunWithTasks()

    print()
    print("=== PART 4: asyncio.Queue — async producer-consumer ===")
    objQueue   = asyncio.Queue(maxsize=3)
    await asyncio.gather(
        AsyncProducer(objQueue, 5),
        AsyncConsumer(objQueue, "ConsumerA"),
        AsyncConsumer(objQueue, "ConsumerB"),
    )

if __name__ == "__main__":
    asyncio.run(main())
