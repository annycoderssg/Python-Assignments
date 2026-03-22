class Arithmetic:
    def __init__( self, intValue1, intValue2 ):
        self.intNumber1 = intValue1
        self.intNumber2 = intValue2
        self.intAddition = 0
        self.intSubtraction = 0
        self.intMultiplication = 0
        self.intDivision = 0

    def Accept(self):
        self.intNumber1 = int(input("Enter 1st Number : "))
        self.intNumber2 = int(input("Enter 2nd Number : "))

    def Validate(self):
        if( self.intNumber2 > self.intNumber1 ):
            return True
        else:
            return False

    def Addition(self):
        self.intAddition = self.intNumber1 + self.intNumber2    

    def Subtraction(self):
        self.intSubtraction = self.intNumber1 - self.intNumber2 

    def Multiplication(self):
        self.intMultiplication = self.intNumber1 * self.intNumber2 

    def Division(self):
        self.intDivision = self.intNumber1 / self.intNumber2 

    def Display(self):
        print("We are performing Arithmetic operations on Numbers: ", self.intNumber1, self.intNumber2 )
        print("Addition is: ", self.intAddition)
        print("Subtraction is: ", self.intSubtraction)
        print("Multiplication is: ", self.intMultiplication)
        print("Division is: ", self.intDivision)

def main():
    objArithmetic1 = Arithmetic(0, 0)
    objArithmetic2 = Arithmetic(0, 0)

    objArithmetic1.Accept()
    if( objArithmetic1.Validate() ):
        print("To perform operation please enter Number1 > Number2")
        objArithmetic1.Accept()

    objArithmetic1.Addition()
    objArithmetic1.Subtraction()
    objArithmetic1.Multiplication()
    objArithmetic1.Division()
    objArithmetic1.Display()

    objArithmetic2.Accept()
    if( objArithmetic2.Validate() ):
        print("To perform operation please enter Number1 > Number2")
        objArithmetic2.Accept()

    objArithmetic2.Addition()
    objArithmetic2.Subtraction()
    objArithmetic2.Multiplication()
    objArithmetic2.Division()
    objArithmetic2.Display()    

if __name__ == "__main__":
    main()