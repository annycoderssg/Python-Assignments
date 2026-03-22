# Method Overriding and Polymorphism
#
# Concepts demonstrated:
#   Method Overriding : child class redefines a parent method
#   Polymorphism      : same method name behaves differently per class
#   Runtime dispatch  : Python calls the correct version at runtime

class Shape:
    def __init__(self, strColor):
        self.strColor = strColor

    def Area(self):
        return 0.0

    def Display(self):
        print("Shape Color :", self.strColor)
        print("Area        : %.2f" % self.Area())


class Circle(Shape):
    fltPI = 3.14159

    def __init__(self, strColor, fltRadius):
        super().__init__(strColor)
        self.fltRadius = fltRadius

    # Override Area()
    def Area(self):
        return Circle.fltPI * self.fltRadius * self.fltRadius

    def Display(self):
        print("--- Circle ---")
        super().Display()
        print("Radius      :", self.fltRadius)


class Rectangle(Shape):
    def __init__(self, strColor, fltLength, fltWidth):
        super().__init__(strColor)
        self.fltLength = fltLength
        self.fltWidth  = fltWidth

    # Override Area()
    def Area(self):
        return self.fltLength * self.fltWidth

    def Display(self):
        print("--- Rectangle ---")
        super().Display()
        print("Length      :", self.fltLength)
        print("Width       :", self.fltWidth)


class Triangle(Shape):
    def __init__(self, strColor, fltBase, fltHeight):
        super().__init__(strColor)
        self.fltBase   = fltBase
        self.fltHeight = fltHeight

    # Override Area()
    def Area(self):
        return 0.5 * self.fltBase * self.fltHeight

    def Display(self):
        print("--- Triangle ---")
        super().Display()
        print("Base        :", self.fltBase)
        print("Height      :", self.fltHeight)


def PrintAllAreas(arrShapes):
    # Polymorphism: same call -> different Area() at runtime
    print("=== Polymorphic Area Calculation ===")
    for objShape in arrShapes:
        objShape.Display()
        print()


def main():
    objCircle    = Circle("Red", 7.0)
    objRectangle = Rectangle("Blue", 10.0, 5.0)
    objTriangle  = Triangle("Green", 8.0, 6.0)

    arrShapes = [objCircle, objRectangle, objTriangle]
    PrintAllAreas(arrShapes)

if __name__ == "__main__":
    main()
