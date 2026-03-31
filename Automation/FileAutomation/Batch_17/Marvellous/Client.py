import Marvellous

def main():
    Value1 = int(input("Enter First Number: "))
    Value2 = int(input("Enter Second Number: "))

    Answer = 0
    Answer = Marvellous.Addition(Value1, Value2)
    print("Addition of two number is: ", Answer)

    Answer = Marvellous.Substraction(Value1, Value2)
    print("Substraction of two number is: ", Answer)

    Answer = Marvellous.Multiplication(Value1, Value2)
    print("Multiplication of two number is: ", Answer)

if __name__ == "__main__":
    main()
