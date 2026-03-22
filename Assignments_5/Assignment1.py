class Demo:
    def __init__( self, intValue1, intValue2 ):
        self.intNumber1 = intValue1
        self.intNumber2 = intValue2

    def Fun(self):
        print("In Function Fun Display Values :")
        print("Number 1 : ", self.intNumber1 )
        print("Number 2 : ", self.intNumber2 )

    def Gun(self):
        print("In Function Gun Display Values :")
        print("Number 1 : ", self.intNumber1 )
        print("Number 2 : ", self.intNumber2 )    

def main():
    obj1 = Demo(11, 21)
    obj2 = Demo(51, 101)

    obj1.Fun()
    obj2.Fun()
    obj1.Gun()
    obj2.Gun()    

if __name__ == "__main__":
    main()