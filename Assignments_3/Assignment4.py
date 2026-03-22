def main():
    arrintNumbers = []
    
    intNumber = int(input("Number of Elements : "))
    
    print("Input Numbers: ")
    for i in range(intNumber):
        intValue = int(input())
        arrintNumbers.append(intValue)

    intSearch = int(input("Enter elements to search in list : "))   

    intFrequncy = 0
    for i in range(len(arrintNumbers)):
        if intSearch == arrintNumbers[i]:
            intFrequncy = intFrequncy + 1

    print("Number of occurances : ", intFrequncy )

if __name__ == "__main__":
    main()