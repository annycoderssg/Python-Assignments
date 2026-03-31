from sys import *
from Arithmetic import *

def main():
    print( "=============== Automation Script ===============" )

    print( "Automation script Name: ", argv[0] )    

    if( len(argv) == 2 ):
        if( argv[1] == "-h" or argv[1] == "-H" ):       # Flag for displaying usage of help
            print("This automation is used to perform addition of two numbers")
            exit()
        
        elif( argv[1] == "-u" or argv[1] == "-U" ):       # Flag for displaying usage of script
            print( "Usage: Name_of_script first_argument Second_argument")
            print( "Example: Demo.py 11 10")
            exit()
        
        else:
            print( "There is no such option to handle.." )
            exit()
            
    if( len(argv) != 3 ):
        print( "Invalid number of arguments" )
        exit()
    else:
        intResult = Addition( int( argv[1] ), int( argv[2] ) )
        print( "Addition of two numbers are: ", intResult )

if __name__ == "__main__":
    main()

# python Automation.py 11 10