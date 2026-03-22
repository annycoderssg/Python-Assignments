# Thread Synchronization: Lock and RLock
#
# Concepts demonstrated:
#   Race condition  : two threads modifying shared data simultaneously -> corrupted result
#   threading.Lock  : mutual exclusion — only one thread enters the critical section at a time
#   threading.RLock : reentrant lock — same thread can acquire it multiple times without deadlock
#   acquire/release : explicit lock management (also shown with 'with' statement)

import threading
import time

# -----------------------------------------------------------------------
# PART 1: Demonstrate Race Condition (no lock)
# -----------------------------------------------------------------------
intSharedCounter = 0

def IncrementWithoutLock(intIterations):
    global intSharedCounter
    for _ in range(intIterations):
        intTemp = intSharedCounter
        intTemp = intTemp + 1
        intSharedCounter = intTemp   # not atomic — race condition possible

# -----------------------------------------------------------------------
# PART 2: Fix with Lock
# -----------------------------------------------------------------------
intSafeCounter = 0
objLock = threading.Lock()

def IncrementWithLock(intIterations):
    global intSafeCounter
    for _ in range(intIterations):
        with objLock:                # acquire on entry, release on exit
            intSafeCounter += 1

# -----------------------------------------------------------------------
# PART 3: RLock — reentrant lock (same thread can lock it multiple times)
# -----------------------------------------------------------------------
intBankBalance = 1000
objRLock = threading.RLock()

def Deposit(fltAmount):
    with objRLock:
        global intBankBalance
        intBankBalance += fltAmount
        print("  Deposited %.0f | Balance: %d" % (fltAmount, intBankBalance))
        Audit()             # calls Audit() which also acquires the same RLock

def Audit():
    with objRLock:          # same thread re-acquires — works with RLock, deadlocks with Lock
        print("  Audit   : Balance verified = %d" % intBankBalance)

def BankWorker(fltAmount):
    Deposit(fltAmount)

# -----------------------------------------------------------------------
# main
# -----------------------------------------------------------------------
def main():
    global intSharedCounter, intSafeCounter

    intIterations = 100000

    # --- Race condition demo ---
    print("=== PART 1: Race Condition (no lock) ===")
    intSharedCounter = 0
    t1 = threading.Thread(target=IncrementWithoutLock, args=(intIterations,))
    t2 = threading.Thread(target=IncrementWithoutLock, args=(intIterations,))
    t1.start(); t2.start()
    t1.join();  t2.join()
    print("Expected : %d" % (intIterations * 2))
    print("Got      : %d  <-- may differ due to race condition" % intSharedCounter)

    print()

    # --- Lock fix demo ---
    print("=== PART 2: Thread-safe Counter (with Lock) ===")
    intSafeCounter = 0
    t3 = threading.Thread(target=IncrementWithLock, args=(intIterations,))
    t4 = threading.Thread(target=IncrementWithLock, args=(intIterations,))
    t3.start(); t4.start()
    t3.join();  t4.join()
    print("Expected : %d" % (intIterations * 2))
    print("Got      : %d  <-- always correct with Lock" % intSafeCounter)

    print()

    # --- RLock demo ---
    print("=== PART 3: Reentrant Lock (RLock) ===")
    t5 = threading.Thread(target=BankWorker, args=(500,))
    t6 = threading.Thread(target=BankWorker, args=(300,))
    t5.start(); t5.join()
    t6.start(); t6.join()

if __name__ == "__main__":
    main()
