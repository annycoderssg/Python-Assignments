import threading

def EvenFactor( intValue ):
    intSum = 0
    for i in range(intValue):
        if 0 == ( i % 2 ):
            intSum = intSum + i
            print("Addition of Even Factors: ", intSum)

def OddFactor( intValue ):
    intSum = 0
    for i in range(intValue):
        if 0 != ( i % 2 ):
            intSum = intSum + i
            print("Addition of Odd Factors: ", intSum)


def main():
    intNo = int( input( "Enter Number: " ) )
    t1 = threading.Thread( target = EvenFactor, args = (intNo,) )
    t2 = threading.Thread( target = OddFactor, args = (intNo,) )

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()