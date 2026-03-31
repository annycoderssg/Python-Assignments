# Function accept one parameter and return nothing    
def Marvellous( strName ):
    print(type(strName))
    print("Inside Marvellous Function")
    print("Welcome", strName )

def main():
    Marvellous("Anand")
    Marvellous(90.90)

if __name__ == "__main__":
    main()