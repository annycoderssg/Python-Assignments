# Operator Overloading
#
# Concepts demonstrated:
#   __str__  : controls print(obj) output
#   __repr__ : controls developer representation
#   __add__  : overloads the + operator
#   __sub__  : overloads the - operator
#   __mul__  : overloads the * operator
#   __eq__   : overloads the == operator
#   __lt__   : overloads the <  operator
#   __len__  : overloads len(obj)

class Vector:
    def __init__(self, intX, intY):
        self.intX = intX
        self.intY = intY

    # String representation for print()
    def __str__(self):
        return "Vector(%d, %d)" % (self.intX, self.intY)

    # Developer representation
    def __repr__(self):
        return "Vector(intX=%d, intY=%d)" % (self.intX, self.intY)

    # + operator: add two vectors
    def __add__(self, other):
        return Vector(self.intX + other.intX, self.intY + other.intY)

    # - operator: subtract two vectors
    def __sub__(self, other):
        return Vector(self.intX - other.intX, self.intY - other.intY)

    # * operator: scalar multiplication
    def __mul__(self, intScalar):
        return Vector(self.intX * intScalar, self.intY * intScalar)

    # == operator: equality check
    def __eq__(self, other):
        return self.intX == other.intX and self.intY == other.intY

    # < operator: compare magnitudes
    def __lt__(self, other):
        return self.Magnitude() < other.Magnitude()

    # len(): returns magnitude as integer
    def __len__(self):
        return int(self.Magnitude())

    def Magnitude(self):
        return (self.intX ** 2 + self.intY ** 2) ** 0.5

    def Display(self):
        print("Vector     :", self)
        print("Magnitude  : %.2f" % self.Magnitude())


class Matrix2x2:
    def __init__(self, arrValues):
        # arrValues = [[a, b], [c, d]]
        self.arrValues = arrValues

    def __str__(self):
        a, b = self.arrValues[0]
        c, d = self.arrValues[1]
        return "| %d  %d |\n| %d  %d |" % (a, b, c, d)

    # + operator: add two 2x2 matrices
    def __add__(self, other):
        arrResult = [
            [self.arrValues[0][0] + other.arrValues[0][0],
             self.arrValues[0][1] + other.arrValues[0][1]],
            [self.arrValues[1][0] + other.arrValues[1][0],
             self.arrValues[1][1] + other.arrValues[1][1]]
        ]
        return Matrix2x2(arrResult)

    # == operator
    def __eq__(self, other):
        return self.arrValues == other.arrValues


def main():
    print("=== Vector Operator Overloading ===")
    objV1 = Vector(3, 4)
    objV2 = Vector(1, 2)

    print("V1 :", objV1)
    print("V2 :", objV2)
    print("V1 + V2 =", objV1 + objV2)
    print("V1 - V2 =", objV1 - objV2)
    print("V1 * 3  =", objV1 * 3)
    print("V1 == V2:", objV1 == objV2)
    print("V1 == V1:", objV1 == Vector(3, 4))
    print("V1 < V2 :", objV1 < objV2)
    print("len(V1) :", len(objV1))

    print()
    objV1.Display()

    print()
    print("=== Matrix2x2 Operator Overloading ===")
    objM1 = Matrix2x2([[1, 2], [3, 4]])
    objM2 = Matrix2x2([[5, 6], [7, 8]])

    print("M1 :")
    print(objM1)
    print("M2 :")
    print(objM2)
    print("M1 + M2 :")
    print(objM1 + objM2)
    print("M1 == M2:", objM1 == objM2)
    print("M1 == M1:", objM1 == Matrix2x2([[1, 2], [3, 4]]))

if __name__ == "__main__":
    main()
