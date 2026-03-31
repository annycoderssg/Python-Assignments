import os.path

def main():
    print("Enter the name of file that you want to create: ")
    strFileName = input()

    if True == os.path.exists( strFileName):
        print( "Unable to create file as file is already exists:" )
    else:
        current_working_directory = os.getcwd()
        print("Your file is going to create in: ", current_working_directory )
        objFile = open( strFileName, "x" )

if __name__ == "__main__":
    main()