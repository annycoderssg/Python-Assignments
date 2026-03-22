def Display(i, intLoop):
    if(i < intLoop):
        print("*", end=" ")
        i+=1
        Display(i, intLoop)

def main():
    intLoop = int( input("Enter Number which you want to display *'s : ") )
    Display(0, intLoop )
    
if __name__ =="__main__":
    main()