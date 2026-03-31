def main():
    print("Demonstration of List:")

    List1 = [10,"Hello",67.90,True]
    print(List1)

    print(List1[0])

    List2 = [11, 78, 11, 54, 25, 78]

    print(List2)

    List2[1] = 79

    print(List2)

    List2.append(101)

    print(List2)

    List2.remove(11)

    print(List2)

if __name__ == "__main__":
    main()