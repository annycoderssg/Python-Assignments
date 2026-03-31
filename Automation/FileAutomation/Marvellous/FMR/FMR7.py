#Unnamed Function or ( Lambda/Anonymous Function )
#Name = lambda Parameter_Lists : Function_Logic
import functools

def main():
    print("Demonstration of Filter Map Reduce")

    arrData = []

    intLoop = int(input("Enter Number of Elements : "))

    for i in range( intLoop ):
        intValue = int(input("Enter Your Number : "))
        arrData.append( intValue )

    print("Intput Data : ", arrData )

    intResult = functools.reduce((lambda intNo1, intNo2 : intNo1 + intNo2), list(map((lambda intNo : ( intNo + 2 )), list(filter((lambda intNo : ( 0 == ( intNo % 2 ) )), arrData) )) ))
    print("Addition is : ", intResult )

if __name__ == "__main__":
    main()