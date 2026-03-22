#Unnamed Function or ( Lambda/Anonymous Function )
#Name = lambda Parameter_Lists : Function_Logic
Add = lambda intNo1, intNo2 : intNo1 + intNo2

CheckEven = lambda intNo : ( 0 == ( intNo % 2 ) )

Increase = lambda intNo : ( intNo + 2 )

# Task: Function Name
# Elements : List of data elements
def FilterX( Task, Elements ):
    arrResult = []
    for no in Elements: 
        if( True == Task(no) ):
            arrResult.append(no)
    return arrResult

def MapX( Task, Elements):
    arrResult = []
    for no in Elements:
        arrResult.append(Task(no))

    return arrResult

def ReduceX( Task, Elements):
    intResult = 0
    for no in Elements:
        intResult = Task(no,intResult)

    return intResult

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