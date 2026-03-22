def Display(intLoop):
    if(intLoop > 0 ):
        print(intLoop, end=" ")
        intLoop = intLoop - 1
        Display(intLoop)

def main():
    intLoop = int( input("Enter Number which you want to display range in reverse order : ") )
    Display(intLoop )
    
if __name__ =="__main__":
    main()