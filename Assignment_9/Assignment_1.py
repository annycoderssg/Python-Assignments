import os.path

def main():
    strFileName = input( "Enter File name which you want to check : " )
    current_working_directory = os.getcwd()
    if True == os.path.exists( strFileName ):
        print("File is exist on path : ", current_working_directory )
    else:
        print("File is not exist on path : ", current_working_directory )

if __name__ == "__main__":
    main()