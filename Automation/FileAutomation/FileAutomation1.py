from sys import *
import os

def DirectoryTraves( strDirectoryName ):
    print( "We are going to traverse dir: ", strDirectoryName )

    # listDir = os.listdir( strDirectoryName )
    # print( listDir )

    for foldername, subfoldername, filename in os.walk( strDirectoryName ):
        for fname in filename:
            print( fname )

def main():
    print( "=============== Automation Script ===============" )

    print( "Automation script Name: ", argv[0] )    

    if( len(argv) != 2 ):
        print( "Invalid number of arguments" )
        exit()

    if( argv[1] == "-h" or argv[1] == "-H" ):       # Flag for displaying usage of help
        print("This automation is used to perform file automation")
        exit()
    
    elif( argv[1] == "-u" or argv[1] == "-U" ):       # Flag for displaying usage of script
        print( "Usage: Name_of_script first_argument Second_argument")
        print( "Example: Demo.py Automation")
        exit()

    else:
        # Logic
        DirectoryTraves( argv[1] )

if __name__ == "__main__":
    main()

# python FileAutomation.py DirectoryName