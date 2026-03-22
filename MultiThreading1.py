import os
import threading

def Task1( intValue ):
    print("PID of Task1 : ", os.getpid())
    print("Thread Id Task1 : ", threading.get_ident())
    for i in range(intValue):
        print("Task1 : ", i)

def Task2( intValue ):
    print("PID of Task2 : ", os.getpid())
    print("Thread Id Task2 : ", threading.get_ident())
    for i in range(intValue):
        print("Task2 : ", i)

def main():
    print("Demonstration of Multi Threading")
    print("PID of parent function : ", os.getpid())
    print("Thread Id Main : ", threading.get_ident())

    intNo = 5
    intNo2 = 8
    t1 = threading.Thread( target = Task1, args = (intNo,) )
    t2 = threading.Thread( target = Task2, args = (intNo2,) )

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()