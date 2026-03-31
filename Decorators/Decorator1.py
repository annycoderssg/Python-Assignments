def Sub( A, B):
    if A < B:
        A, B = B, A             # Swapping of two numbers

    return A - B

def main():
    Ret = Sub(10, 7)
    print("Subtraction is : ", Ret)

    Ret = Sub(7, 10)
    print("Subtraction is : ", Ret)

if __name__ == "__main__":
    main()