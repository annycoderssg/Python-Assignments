from functools import reduce

Add = lambda intNo1, intNo2 : intNo1 + intNo2

CheckEven = lambda intNo : ( 0 == ( intNo % 2 ) )

Square = lambda intNo : ( intNo * intNo * intNo )

def main():
    arrintData = []

    intLoop = int(input("Enter Number of Elements : "))

    print( "Enter Your Numbers : " )
    for i in range( intLoop ):
        intValue = int(input())
        arrintData.append( intValue )

    print("Intput Data List : ", arrintData )

    intResult = list(filter(CheckEven, arrintData))
    print("List After Filter : ", intResult )

    intResult = list(map(Square, intResult) )
    print("List After Map : ", intResult )

    intResult = reduce(Add, intResult)
    print("Output of reduce : ", intResult )

if __name__ == "__main__":
    main()