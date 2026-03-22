import math

class Circle:
    
    fltPI = 3.14

    def __init__( self, fltRadius, fltArea, fltCircumference ):
        self.fltRadius = fltRadius
        self.fltArea = fltArea
        self.fltCircumference = fltCircumference

    def Accept(self):
        self.fltRadius = float(input("Enter Radius Value: "))

    def CalculateArea(self):
        self.fltArea = ( Circle.fltPI * math.pow(self.fltRadius, 2) )

    def CalculateCircumference(self):
        self.fltCircumference = ( 2 * Circle.fltPI * self.fltRadius )   

    def Display(self):
        print()
        print("Radius of Circle is : ", self.fltRadius )
        print("Area of Circle is : ", self.fltArea )
        print("Circumference of Circle is : ", "%.2f" % self.fltCircumference )

def main():
    objCircle1 = Circle(0.0, 0.0, 0.0)
    objCircle2 = Circle(0.0, 0.0, 0.0)

    objCircle1.Accept()
    objCircle1.CalculateArea()
    objCircle1.CalculateCircumference()
    objCircle1.Display()

    objCircle2.Accept()
    objCircle2.CalculateArea()
    objCircle2.CalculateCircumference()
    objCircle2.Display()

if __name__ == "__main__":
    main()