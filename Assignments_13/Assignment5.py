# Process Pool: multiprocessing.Pool and ProcessPoolExecutor
#
# Concepts demonstrated:
#   multiprocessing.Pool        : worker process pool
#   Pool.map()                  : apply function to list, collect ordered results
#   Pool.starmap()              : map with multiple arguments per call
#   Pool.apply_async()          : non-blocking submission, get result via AsyncResult
#   ProcessPoolExecutor         : concurrent.futures high-level API for processes
#   ProcessPoolExecutor.submit  : submit single task, returns Future
#   ProcessPoolExecutor.map     : map function over iterable concurrently

import multiprocessing
import os
import time
from concurrent.futures import ProcessPoolExecutor, as_completed

# -----------------------------------------------------------------------
# Worker functions (must be top-level for pickling on Windows)
# -----------------------------------------------------------------------
def ComputeSquare(intN):
    return intN * intN

def ComputePower(intBase, intExp):
    return intBase ** intExp

def HeavyTask(intTaskId):
    time.sleep(0.5)     # simulate CPU-bound work
    intResult = sum(range(intTaskId * 1000))
    return "Task %d | PID %d | Result %d" % (intTaskId, os.getpid(), intResult)

def IsPrime(intN):
    if intN < 2:
        return False
    for i in range(2, int(intN ** 0.5) + 1):
        if intN % i == 0:
            return False
    return True

# -----------------------------------------------------------------------
# main
# -----------------------------------------------------------------------
def main():
    intCores = multiprocessing.cpu_count()
    print("Available CPU cores:", intCores)

    print()
    print("=== PART 1: Pool.map() — square numbers ===")
    arrNumbers = list(range(1, 11))
    with multiprocessing.Pool(processes=4) as objPool:
        arrSquares = objPool.map(ComputeSquare, arrNumbers)
    print("Input  :", arrNumbers)
    print("Squares:", arrSquares)

    print()
    print("=== PART 2: Pool.starmap() — powers with multiple args ===")
    arrPairs = [(2, 10), (3, 5), (5, 4), (7, 3), (10, 2)]
    with multiprocessing.Pool(processes=4) as objPool:
        arrPowers = objPool.starmap(ComputePower, arrPairs)
    for (intBase, intExp), intResult in zip(arrPairs, arrPowers):
        print("  %d ^ %d = %d" % (intBase, intExp, intResult))

    print()
    print("=== PART 3: Pool.apply_async() — non-blocking tasks ===")
    with multiprocessing.Pool(processes=4) as objPool:
        arrAsync = [objPool.apply_async(HeavyTask, args=(i,)) for i in range(1, 6)]
        for objAsyncResult in arrAsync:
            print(" ", objAsyncResult.get())   # .get() blocks until result is ready

    print()
    print("=== PART 4: ProcessPoolExecutor — filter primes ===")
    arrCandidates = list(range(1, 51))
    with ProcessPoolExecutor(max_workers=4) as objExecutor:
        arrIsPrime = list(objExecutor.map(IsPrime, arrCandidates))
    arrPrimes = [n for n, prime in zip(arrCandidates, arrIsPrime) if prime]
    print("Primes from 1 to 50:", arrPrimes)

    print()
    print("=== PART 5: ProcessPoolExecutor with as_completed() ===")
    arrTaskIds = [5, 2, 8, 1, 4]
    with ProcessPoolExecutor(max_workers=4) as objExecutor:
        objFutureMap = {objExecutor.submit(HeavyTask, tid): tid for tid in arrTaskIds}
        for objFuture in as_completed(objFutureMap):
            print(" Completed:", objFuture.result())

if __name__ == "__main__":
    main()
