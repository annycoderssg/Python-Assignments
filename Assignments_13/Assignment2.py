# Thread Communication: Event, Semaphore, and Queue
#
# Concepts demonstrated:
#   threading.Event     : one thread signals another to proceed (flag-based)
#   threading.Semaphore : limits how many threads run concurrently
#   queue.Queue         : thread-safe producer-consumer pipeline

import threading
import queue
import time

# -----------------------------------------------------------------------
# PART 1: threading.Event — signal between threads
# -----------------------------------------------------------------------
objDataReadyEvent = threading.Event()
strSharedData     = ""

def DataProducer():
    global strSharedData
    print("Producer: Preparing data...")
    time.sleep(2)                       # simulate work
    strSharedData = "Hello from Producer!"
    print("Producer: Data ready — signalling consumer")
    objDataReadyEvent.set()             # signal the consumer

def DataConsumer():
    print("Consumer: Waiting for data...")
    objDataReadyEvent.wait()            # block until event is set
    print("Consumer: Received ->", strSharedData)

# -----------------------------------------------------------------------
# PART 2: threading.Semaphore — limit concurrent access (e.g. DB connections)
# -----------------------------------------------------------------------
intMaxConnections = 3
objSemaphore      = threading.Semaphore(intMaxConnections)

def DatabaseWorker(intWorkerId):
    print("Worker %d: Waiting for DB connection..." % intWorkerId)
    with objSemaphore:                  # only 3 workers inside at a time
        print("Worker %d: Connected to DB — processing" % intWorkerId)
        time.sleep(1)
        print("Worker %d: Done — releasing connection" % intWorkerId)

# -----------------------------------------------------------------------
# PART 3: queue.Queue — producer-consumer with thread-safe queue
# -----------------------------------------------------------------------
objTaskQueue = queue.Queue(maxsize=5)
intSentinel  = None                     # poison pill to stop consumers

def Producer(intItems):
    for i in range(1, intItems + 1):
        objTaskQueue.put(i)             # blocks if queue is full
        print("Produced item:", i)
        time.sleep(0.1)
    objTaskQueue.put(intSentinel)       # signal consumer to stop

def Consumer(strName):
    while True:
        intItem = objTaskQueue.get()    # blocks if queue is empty
        if intItem is intSentinel:
            objTaskQueue.put(intSentinel)   # pass sentinel to next consumer
            print("%s: No more items — stopping" % strName)
            break
        print("%s: Consumed item %d" % (strName, intItem))
        objTaskQueue.task_done()

# -----------------------------------------------------------------------
# main
# -----------------------------------------------------------------------
def main():
    print("=== PART 1: threading.Event ===")
    tProducer = threading.Thread(target=DataProducer)
    tConsumer = threading.Thread(target=DataConsumer)
    tConsumer.start()
    tProducer.start()
    tProducer.join()
    tConsumer.join()

    print()
    print("=== PART 2: threading.Semaphore (max 3 concurrent DB connections) ===")
    arrWorkers = []
    for i in range(1, 8):               # 7 workers, only 3 allowed in at once
        t = threading.Thread(target=DatabaseWorker, args=(i,))
        arrWorkers.append(t)
        t.start()
    for t in arrWorkers:
        t.join()

    print()
    print("=== PART 3: queue.Queue (Producer-Consumer) ===")
    tProd  = threading.Thread(target=Producer,  args=(6,))
    tCons1 = threading.Thread(target=Consumer, args=("ConsumerA",))
    tCons2 = threading.Thread(target=Consumer, args=("ConsumerB",))
    tProd.start()
    tCons1.start()
    tCons2.start()
    tProd.join()
    tCons1.join()
    tCons2.join()
    print("All items processed")

if __name__ == "__main__":
    main()
