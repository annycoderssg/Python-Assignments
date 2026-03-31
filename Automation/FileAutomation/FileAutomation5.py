from sys import *
import os
import time

def DirectoryTraves( strDirectoryName ):
    print( "We are going to traverse dir: ", strDirectoryName )

    # listDir = os.listdir( strDirectoryName )
    # print( listDir )

    boolFlag = os.path.isabs( strDirectoryName )

    if False == boolFlag:
        strDirectoryName = os.path.abspath( strDirectoryName )

    isDirExists = os.path.isdir( strDirectoryName )

    print( strDirectoryName )

    if isDirExists:
        for folderName, subFolderName, fileName in os.walk( strDirectoryName ):
            print( "Current Directory name : ", folderName )
            
            for subName in subFolderName:
                print("Subfolder name is: ", subName )
            
            for fname in fileName:
                fname = os.path.abspath(strDirectoryName+"/"+fname)
                print( "File Name is : ", fname, " => File Size is : ", os.path.getsize(fname), " bytes" )
    else:
        print( "Invalid Path" )

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
        startTime = time.time()
        DirectoryTraves( argv[1] )
        endTime = time.time()

        print( "The script took to execute as : ", endTime - startTime )

if __name__ == "__main__":
    main()

# python FileAutomation.py DirectoryName