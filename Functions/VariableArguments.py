def Display( *Values ):
    print(type(Values))
    print(len(Values))
    print(Values)

    for i in range(len(Values)):
        print("Argument Values is :", Values[i])

def main():
    print("Demonstration of Default Arguments: ")
    Display(10, 20, 30, 40, 50)
    Display("Anand", 10, 30)

if __name__ == "__main__":
    main()