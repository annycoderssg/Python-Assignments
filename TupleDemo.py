def main():
    print("Demonstration of Tuple")

    Tuple1 = (1, "Hello", 99.89, False)

    print(Tuple1)

    print(type(Tuple1))

    print(len(Tuple1))

    Tuple2 = (11, "Hello", 99.89, False, 11)

    print(Tuple2)

    print(Tuple2[1])

    for value in Tuple2:
        print(value)

    for i in range(len(Tuple2)):
        print(Tuple2[i])
        print(i)
    
    #Tuple2[0] = 12     Not Applicable

    #print(Tuple2)

    # Tuple2.append(89)     Not Applicable

    # print(Tuple2)

if __name__ == "__main__":
    main()