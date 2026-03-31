def main():
    print("Demonstration of Set")

    Set1 = {11, 78.89, "Hello", True}
    print(Set1)

    Set2 = {11, 78.89, "Hello", True, 11}
    print(Set2)

    for value in Set2:
        print(value)

    Set3 = {11, 78.89, "Hello", True, 11, 78.89, 11, "Hello"}
    print(Set3)

    Set2.add(101)
    print(Set2)

    Set2.remove(101)
    print(Set2)

    Number = int(input("Enter value to search in set:"))

    for val in Set2:
        if( val == Number ):
            print("Value is available")
            break

    # print(Set2[1])    Not Applicable

if __name__ == "__main__":
    main()