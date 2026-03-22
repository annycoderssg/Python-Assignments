from functools import reduce

def Add( intSum, intNumber):
    intSum = intSum + intNumber
    return intSum

def main():
    arrintNumbers = []
    
    intNumber = int(input("Number of Elements : "))
    
    print("Enter Numbers that you want to add: ")
    for i in range(intNumber):
        intValue = int(input())
        arrintNumbers.append(intValue)

    print("List of Elements are : ", arrintNumbers )
    
    intTotal = reduce(Add, arrintNumbers)
    print("Addition of all List Elements is : ", intTotal)

if __name__ == "__main__":
    main()