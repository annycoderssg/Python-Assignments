class Demo:
    def __init__( self, intVal1, intVal2 ):
        print("inside init methods")
        self.intNo1 = intVal1
        self.intNo2 = intVal2

    def Display(self):
        print( "Value of one : ", self.intNo1)
        print( "Value of two : ", self.intNo2)

def main():
    print("Demonstration of OOP")

    obj1 = Demo( 10, 20 )
    obj1.Display()

    obj2 = Demo( 30, 40 )
    obj2.Display()

if __name__ == "__main__":
    main()