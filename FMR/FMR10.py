#Unnamed Function or ( Lambda/Anonymous Function )
#Name = lambda Parameter_Lists : Function_Logic
import MarvellousFMR

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

    intResult = list(MarvellousFMR.FilterX(CheckEven, arrData))
    print("Filter Data : ", intResult )

    intResult = list(MarvellousFMR.MapX(Increase, intResult) )
    print("Increase Data : ", intResult )

    intResult = MarvellousFMR.ReduceX(Add, intResult)
    print("Addition is : ", intResult )

if __name__ == "__main__":
    main()