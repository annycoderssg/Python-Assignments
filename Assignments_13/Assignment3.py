# Thread Pool and Daemon Threads
#
# Concepts demonstrated:
#   ThreadPoolExecutor  : manages a pool of worker threads automatically
#   submit()            : schedule a single callable, returns a Future
#   map()               : apply a function to a list of inputs concurrently
#   Future.result()     : get the return value of a submitted task
#   as_completed()      : process results as each thread finishes
#   Daemon thread       : background thread that dies when the main program exits

import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

# -----------------------------------------------------------------------
# PART 1: Daemon Thread
# -----------------------------------------------------------------------
def BackgroundMonitor():
    while True:
        print("  [Monitor] System running... (daemon thread)")
        time.sleep(1)

# -----------------------------------------------------------------------
# PART 2: ThreadPoolExecutor with submit() and Future
# -----------------------------------------------------------------------
def DownloadFile(strFileName):
    print("Downloading:", strFileName)
    time.sleep(1)                       # simulate download delay
    return "Done: " + strFileName

# -----------------------------------------------------------------------
# PART 3: ThreadPoolExecutor with map()
# -----------------------------------------------------------------------
def SquareNumber(intN):
    time.sleep(0.1)
    return intN * intN

# -----------------------------------------------------------------------
# PART 4: as_completed() — process fastest results first
# -----------------------------------------------------------------------
def FetchData(intTaskId, intDelay):
    time.sleep(intDelay)
    return "Task %d completed (delay=%ds)" % (intTaskId, intDelay)

# -----------------------------------------------------------------------
# main
# -----------------------------------------------------------------------
def main():
    # --- Daemon thread ---
    print("=== PART 1: Daemon Thread ===")
    tMonitor = threading.Thread(target=BackgroundMonitor, daemon=True)
    tMonitor.start()
    print("Main: Daemon thread started — it will stop when main exits")
    time.sleep(2)
    print("Main: Continuing (daemon still running in background)")

    print()

    # --- ThreadPoolExecutor: submit ---
    print("=== PART 2: ThreadPoolExecutor — submit() with Future ===")
    arrFiles = ["report.pdf", "image.png", "data.csv", "video.mp4"]
    with ThreadPoolExecutor(max_workers=2) as objPool:
        arrFutures = [objPool.submit(DownloadFile, f) for f in arrFiles]
        for objFuture in arrFutures:
            print(" Result:", objFuture.result())

    print()

    # --- ThreadPoolExecutor: map ---
    print("=== PART 3: ThreadPoolExecutor — map() ===")
    arrNumbers = [1, 2, 3, 4, 5, 6, 7, 8]
    with ThreadPoolExecutor(max_workers=4) as objPool:
        arrResults = list(objPool.map(SquareNumber, arrNumbers))
    print("Squares:", arrResults)

    print()

    # --- as_completed: fastest first ---
    print("=== PART 4: as_completed() — results as they finish ===")
    arrTasks = [(1, 3), (2, 1), (3, 2), (4, 1)]   # (task_id, delay)
    with ThreadPoolExecutor(max_workers=4) as objPool:
        arrFutures = {
            objPool.submit(FetchData, tid, delay): tid
            for tid, delay in arrTasks
        }
        for objFuture in as_completed(arrFutures):
            print(" Received:", objFuture.result())

    print()
    print("Main: All tasks done — daemon thread will now stop automatically")

if __name__ == "__main__":
    main()
