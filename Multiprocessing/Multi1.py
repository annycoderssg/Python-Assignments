import multiprocessing
import os

def Task1():
    print("Executing the 1st Task...")
    print("PID of running process for task1 : ", os.getpid())

def Task2():
    print("Executing the 2nd Task...")
    print("PID of running process for task2 : ", os.getpid())

def main():
    print("Demonstration of Multiprocessing")

    print("PID of running process is : ", os.getpid())

    Task1()
    Task2()

if __name__ == "__main__":
    main()