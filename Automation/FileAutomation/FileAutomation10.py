from sys import *
import os
import time

# def SortFilesBySize( dict1 ):
#     results = list( filter(lambda x: os.path.getsize(x) > 1, dict1.values() ) )

def DirectoryTravel(DirName ):
    print("We are going to Scan the Directory : ",DirName)

    maxSize = 0
    maxSizeFileName = 0

    flag = os.path.isabs(DirName)

    if flag == False:
        DirName = os.path.abspath(DirName)

    exist = os.path.isdir(DirName)

    if exist:
        for foldername, subfoldername, filename in os.walk(DirName):
            for fname in filename:
                fname = os.path.join(foldername, fname)
                if maxSize < os.path.getsize( fname ):
                    maxSize = os.path.getsize( fname )
                    maxSizeFileName = fname

        print("File name is: ", maxSizeFileName)
        print("Maximum size is : ", maxSize )

        os.remove( maxSizeFileName )

    else:
        print("Invalid path")

def main():
    print("-------------- Automation Script --------------")

    print("Automation Script Name : ",argv[0])

    if(len(argv) != 2):
        print("Invalid number of arguments")
        exit()

    if(argv[1] == "-h" or argv[1] == "-H"):    # Flag for displaying help
        print("This automation script is used to perform File Automation")
        exit()
    
    elif(argv[1] == "-u" or argv[1] == "-U"):    # Flag for displaying the usage of script
        print("Usage : Name_Of_Script First_Argument Second_Argument")
        print("Example : Demo.py Marvellous List6.py")
        exit()

    else:
        starttime = time.time()
        DirectoryTravel(argv[1])
        endtime = time.time()

        print("The script took time to execute as : ",endtime-starttime)

if __name__ == "__main__":
    main()

# python FileAutomation.py Directory_Name File_name