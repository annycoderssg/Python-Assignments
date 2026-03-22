# Multiprocessing: Process, Queue, and Pipe
#
# Concepts demonstrated:
#   multiprocessing.Process : spawn a separate OS process (true parallelism)
#   Process.start/join      : start and wait for a process
#   multiprocessing.Queue   : thread+process-safe FIFO for inter-process communication
#   multiprocessing.Pipe    : two-way communication channel between two processes
#   os.getpid()             : verify each process has its own PID

import multiprocessing
import os
import time

# -----------------------------------------------------------------------
# PART 1: Basic Process — each runs in its own OS process
# -----------------------------------------------------------------------
def WorkerTask(strName, intCount):
    print("[%s] PID: %d | Parent PID: %d" % (strName, os.getpid(), os.getppid()))
    for i in range(1, intCount + 1):
        print("[%s] Step %d" % (strName, i))
        time.sleep(0.2)
    print("[%s] Done" % strName)

# -----------------------------------------------------------------------
# PART 2: Queue — inter-process communication
# -----------------------------------------------------------------------
def QueueProducer(objQueue, intItems):
    print("[Producer] PID:", os.getpid())
    for i in range(1, intItems + 1):
        objQueue.put(i)
        print("[Producer] Sent:", i)
        time.sleep(0.1)
    objQueue.put(None)              # sentinel to stop consumer

def QueueConsumer(objQueue):
    print("[Consumer] PID:", os.getpid())
    while True:
        intItem = objQueue.get()
        if intItem is None:
            print("[Consumer] No more items — stopping")
            break
        print("[Consumer] Received:", intItem)

# -----------------------------------------------------------------------
# PART 3: Pipe — bidirectional communication between two processes
# -----------------------------------------------------------------------
def PipeSender(objConn):
    arrMessages = ["Hello", "How are you?", "Goodbye"]
    for strMsg in arrMessages:
        objConn.send(strMsg)
        print("[Sender ] Sent    :", strMsg)
        time.sleep(0.3)
    objConn.send(None)              # sentinel
    objConn.close()

def PipeReceiver(objConn):
    while True:
        strMsg = objConn.recv()
        if strMsg is None:
            print("[Receiver] Connection closed")
            break
        print("[Receiver] Received:", strMsg)
        objConn.send("ACK: " + strMsg)  # send acknowledgement back

# -----------------------------------------------------------------------
# main — must be inside if __name__ == "__main__" on Windows
# -----------------------------------------------------------------------
def main():
    print("=== PART 1: Basic Processes ===")
    print("Main process PID:", os.getpid())
    p1 = multiprocessing.Process(target=WorkerTask, args=("Process-A", 3))
    p2 = multiprocessing.Process(target=WorkerTask, args=("Process-B", 3))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("Both processes finished")

    print()
    print("=== PART 2: Queue (inter-process communication) ===")
    objQueue = multiprocessing.Queue()
    pProd = multiprocessing.Process(target=QueueProducer, args=(objQueue, 5))
    pCons = multiprocessing.Process(target=QueueConsumer, args=(objQueue,))
    pProd.start()
    pCons.start()
    pProd.join()
    pCons.join()

    print()
    print("=== PART 3: Pipe (bidirectional communication) ===")
    objConnSend, objConnRecv = multiprocessing.Pipe(duplex=True)
    pSender   = multiprocessing.Process(target=PipeSender,   args=(objConnSend,))
    pReceiver = multiprocessing.Process(target=PipeReceiver, args=(objConnRecv,))
    pSender.start()
    pReceiver.start()
    pSender.join()
    pReceiver.join()

if __name__ == "__main__":
    main()
