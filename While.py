import time

def main():
    No = 0
    while( No < 5):
        print( No )
        No = No + 1 #No += 1
        time.sleep(1)

if __name__ == "__main__":
    main()