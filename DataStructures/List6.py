def main():
    arrData = []
    intLength = int(input("Enter Number of Elements : "))

    i = 0
    for i in range(intLength):
        value = int(input("Enter Input Element : "))
        arrData.append(value)

    print("Elements from list are: ")
    j = 0
    while j < len(arrData):
        print(arrData[j])
        j = j + 1

if __name__ == "__main__":
    main()