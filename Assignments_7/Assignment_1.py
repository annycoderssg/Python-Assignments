import threading

def Even( intValue ):
    for i in range(intValue):
        if 0 == ( i % 2 ):
            print("Even Number: ", i)

def Odd( intValue ):
    for i in range(intValue):
        if 0 != ( i % 2 ):
            print("Odd Number: ", i)

def main():
    intNo = 20
    t1 = threading.Thread( target = Even, args = (intNo,) )
    t2 = threading.Thread( target = Odd, args = (intNo,) )

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()