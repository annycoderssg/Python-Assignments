class Arithmatic:
    def __init__(self,A,B):
        print("Inside constructor: ")
        self.No1 = A
        self.No2 = B

    def Addition(self):
        Ans = 0
        Ans = self.No1 + self.No2
        return Ans

    def Subtraction(self):
        Ans = 0
        Ans = self.No1 - self.No2
        return Ans

def main():
    intNo1 = int(input("Enter 1st Number: "))
    intNo2 = int(input("Enter 2nd Number: "))

    ob1 = Arithmatic( intNo1, intNo2 )
    intResult = ob1.Addition()
    print("Addition is : ", intResult )

    intResult = ob1.Subtraction()
    print("Subtraction is : ", intResult )


    intNo1 = int(input("Enter 1st Number: "))
    intNo2 = int(input("Enter 2nd Number: "))

    ob2 = Arithmatic( intNo1, intNo2 )
    intResult = ob2.Addition()
    print("Addition is : ", intResult )

    intResult = ob2.Subtraction()
    print("Subtraction is : ", intResult )

if __name__ == "__main__":
    main()