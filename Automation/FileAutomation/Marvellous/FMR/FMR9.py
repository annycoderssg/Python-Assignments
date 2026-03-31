#Unnamed Function or ( Lambda/Anonymous Function )
#Name = lambda Parameter_Lists : Function_Logic
from MarvellousFMR import FilterX
from MarvellousFMR import MapX
from MarvellousFMR import ReduceX

Add = lambda intNo1, intNo2 : intNo1 + intNo2

CheckEven = lambda intNo : ( 0 == ( intNo % 2 ) )

Increase = lambda intNo : ( intNo + 2 )

def main():
    print("Demonstration of Filter Map Reduce")

    arrData = []

    intLoop = int(input("Enter Number of Elements : "))

    for i in range( intLoop ):
        intValue = int(input("Enter Your Number : "))
        arrData.append( intValue )

    print("Intput Data : ", arrData )

    intResult = list(FilterX(CheckEven, arrData))
    print("Filter Data : ", intResult )

    intResult = list(MapX(Increase, intResult) )
    print("Increase Data : ", intResult )

    intResult = ReduceX(Add, intResult)
    print("Addition is : ", intResult )

if __name__ == "__main__":
    main()