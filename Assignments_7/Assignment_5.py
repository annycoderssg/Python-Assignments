import threading

def Thread1( intValue ):
    intSum = 0
    for i in range(1, intValue+1, 1):
        print("Order List: ", i )

def Thread2( intValue ):
    for i in range(intValue+1, 0, -1 ):
        print("Reversed List: ", i )


def main():
    intNo = 50
    t1 = threading.Thread( target = Thread1, args = (intNo,) )
    t2 = threading.Thread( target = Thread2, args = (intNo,) )

    t1.start()
    t1.join()
    
    t2.start()
    t2.join()

if __name__ == "__main__":
    main()