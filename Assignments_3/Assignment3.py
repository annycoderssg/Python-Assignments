def main():
    arrintNumbers = []
    
    intNumber = int(input("Number of Elements : "))
    
    print("Enter Numbers that you want to check minimum: ")
    for i in range(intNumber):
        intValue = int(input())
        arrintNumbers.append(intValue)

    print("List of Elements are : ", arrintNumbers )
    
    print("Minimum Number from list : ", min(arrintNumbers))

if __name__ == "__main__":
    main()