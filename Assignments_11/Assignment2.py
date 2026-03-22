import sys
import os
import hashlib

def DisplayDuplicates(dict1):
    results = list(filter(lambda x: len(x) > 1, dict1.values()))

    icount = 0
    iFound = 0
    if len(results) > 0:
        for result in results:
            for subresult in result:
                icount += 1
                if icount >= 2:
                    iFound += 1
                    print("Duplicate File: ", subresult)
            icount = 0

        print("Number of duplicate files found: ", iFound)
    else:
        print("No duplicate files found")

def hashfile(path, blocksize=1024):
    with open(path, 'rb') as afile:
        hasher = hashlib.sha256()
        buf = afile.read(blocksize)
        while len(buf) > 0:
            hasher.update(buf)
            buf = afile.read(blocksize)
    return hasher.hexdigest()

def searchDuplicates(path):
    if not os.path.isabs(path):
        path = os.path.abspath(path)

    arrDuplicates = {}
    if os.path.isdir(path):
        for dirName, subdirs, fileList in os.walk(path):
            print("Current folder is : " + dirName)
            for filen in fileList:
                filepath = os.path.join(dirName, filen)
                file_hash = hashfile(filepath)

                if file_hash in arrDuplicates:
                    arrDuplicates[file_hash].append(filepath)
                else:
                    arrDuplicates[file_hash] = [filepath]

        return arrDuplicates
    else:
        print("Invalid Path")
        return {}

def LogDuplicateFiles(dict1):
    results = list(filter(lambda x: len(x) > 1, dict1.values()))

    with open("Log.txt", "w") as objFile:
        if len(results) > 0:
            print("Duplicates Found:")
            print("The following files are duplicate — writing to Log.txt")
            for result in results:
                for subresult in result:
                    objFile.write(subresult)
                    objFile.write("\n")
                    print("\t%s" % subresult)
        else:
            print("No duplicate file found.")

def main():
    print("Application Name : " + sys.argv[0])

    if len(sys.argv) != 2:
        print("Error: Invalid number of arguments")
        sys.exit()

    if sys.argv[1] == "-h" or sys.argv[1] == "-H":
        print("Help: This script is used to traverse specific directory and find duplicate files")
        sys.exit()

    elif sys.argv[1] == "-u" or sys.argv[1] == "-U":
        print("Usage: Application_name AbsolutePath_of_directory")
        print("Example: Assignment2.py Demo")
        sys.exit()

    try:
        arr = searchDuplicates(sys.argv[1])
        LogDuplicateFiles(arr)

    except ValueError:
        print("Error: Invalid datatype of input")

    except Exception as E:
        print("Error: Invalid input", E)

if __name__ == "__main__":
    main()
