import Module1
import Module2

def Starter():
    print("Special variable of starter.py is ", __name__)
    Module1.displayModule1()
    Module2.displayModule2()

if __name__ == "__main__":
    Starter()