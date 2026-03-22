import threading

def EvenList( intValue ):
    intSum = 0
    for i in range(intValue):
        if 0 == ( i % 2 ):
            intSum = intSum + i
            print("Addition of Even List: ", intSum)

def OddList( intValue ):
    intSum = 0
    for i in range(intValue):
        if 0 != ( i % 2 ):
            intSum = intSum + i
            print("Addition of Odd List: ", intSum)


def main():
    intNo = int( input( "Enter Number: " ) )
    t1 = threading.Thread( target = EvenList, args = (intNo,) )
    t2 = threading.Thread( target = OddList, args = (intNo,) )

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()