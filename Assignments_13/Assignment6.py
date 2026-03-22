# Shared Memory and Process Synchronization
#
# Concepts demonstrated:
#   multiprocessing.Value   : single shared variable between processes
#   multiprocessing.Array   : shared array between processes
#   multiprocessing.Lock    : prevent race conditions across processes
#   Race condition          : shown without lock, fixed with lock
#   Shared state            : processes modifying the same memory

import multiprocessing
import time

# -----------------------------------------------------------------------
# PART 1: Race condition on shared Value WITHOUT lock
# -----------------------------------------------------------------------
def IncrementUnsafe(objSharedVal, intIterations):
    for _ in range(intIterations):
        objSharedVal.value += 1         # not atomic across processes

# -----------------------------------------------------------------------
# PART 2: Safe increment on shared Value WITH lock
# -----------------------------------------------------------------------
def IncrementSafe(objSharedVal, objLock, intIterations):
    for _ in range(intIterations):
        with objLock:
            objSharedVal.value += 1

# -----------------------------------------------------------------------
# PART 3: Shared Array — each process fills its portion
# -----------------------------------------------------------------------
def FillArraySlice(objSharedArr, intStart, intEnd, intMultiplier):
    for i in range(intStart, intEnd):
        objSharedArr[i] = i * intMultiplier

# -----------------------------------------------------------------------
# PART 4: Combined example — parallel sum using shared Value + Lock
# -----------------------------------------------------------------------
def PartialSum(arrData, intStart, intEnd, objSharedTotal, objLock):
    intLocalSum = sum(arrData[intStart:intEnd])
    with objLock:
        objSharedTotal.value += intLocalSum

# -----------------------------------------------------------------------
# main
# -----------------------------------------------------------------------
def main():
    intIterations = 50000

    print("=== PART 1: Shared Value WITHOUT lock (race condition) ===")
    objUnsafeVal = multiprocessing.Value('i', 0)    # 'i' = signed int
    p1 = multiprocessing.Process(target=IncrementUnsafe, args=(objUnsafeVal, intIterations))
    p2 = multiprocessing.Process(target=IncrementUnsafe, args=(objUnsafeVal, intIterations))
    p1.start(); p2.start()
    p1.join();  p2.join()
    print("Expected : %d" % (intIterations * 2))
    print("Got      : %d  <-- may be wrong (race condition)" % objUnsafeVal.value)

    print()
    print("=== PART 2: Shared Value WITH Lock (safe) ===")
    objSafeVal = multiprocessing.Value('i', 0)
    objLock    = multiprocessing.Lock()
    p3 = multiprocessing.Process(target=IncrementSafe, args=(objSafeVal, objLock, intIterations))
    p4 = multiprocessing.Process(target=IncrementSafe, args=(objSafeVal, objLock, intIterations))
    p3.start(); p4.start()
    p3.join();  p4.join()
    print("Expected : %d" % (intIterations * 2))
    print("Got      : %d  <-- always correct with Lock" % objSafeVal.value)

    print()
    print("=== PART 3: Shared Array — parallel fill ===")
    intArraySize  = 10
    objSharedArr  = multiprocessing.Array('i', intArraySize)    # shared int array
    p5 = multiprocessing.Process(target=FillArraySlice, args=(objSharedArr, 0, 5, 2))
    p6 = multiprocessing.Process(target=FillArraySlice, args=(objSharedArr, 5, 10, 3))
    p5.start(); p6.start()
    p5.join();  p6.join()
    print("Shared array:", list(objSharedArr))

    print()
    print("=== PART 4: Parallel Sum using shared Value + Lock ===")
    arrData        = list(range(1, 101))        # 1 to 100
    objTotal       = multiprocessing.Value('i', 0)
    objSumLock     = multiprocessing.Lock()
    intMid         = len(arrData) // 2
    p7 = multiprocessing.Process(target=PartialSum, args=(arrData, 0,      intMid,       objTotal, objSumLock))
    p8 = multiprocessing.Process(target=PartialSum, args=(arrData, intMid, len(arrData), objTotal, objSumLock))
    p7.start(); p8.start()
    p7.join();  p8.join()
    print("Sum of 1..100 (parallel) :", objTotal.value)
    print("Sum of 1..100 (expected) :", sum(arrData))

if __name__ == "__main__":
    main()
