def Display(i, intLoop):
    if(i < intLoop):
        i+=1
        print(i, end=" ")
        Display(i, intLoop)

def main():
    intLoop = int( input("Enter Number which you want to display range: ") )
    Display(0, intLoop )
    
if __name__ =="__main__":
    main()