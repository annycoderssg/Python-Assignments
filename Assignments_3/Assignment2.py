def main():
    arrintNumbers = []
    
    intNumber = int(input("Number of Elements : "))
    
    print("Enter Numbers that you want to check maximum: ")
    for i in range(intNumber):
        intValue = int(input())
        arrintNumbers.append(intValue)

    print("List of Elements are : ", arrintNumbers )
    
    print("Maximum Number from list : ", max(arrintNumbers))

if __name__ == "__main__":
    main()