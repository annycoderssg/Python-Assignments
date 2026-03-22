def main():
    BatchName = ["PPA", "Paython", "LSP", "Angular", "LB", "C#"]
    BatchFee = [11000, 15000, 13500, 19000, 15000, 20000]

    for i in range(len(BatchName)):
        print("Batch Name", BatchName[i])
        print("Batch Fee is ", BatchFee[i])
        print()

    DisctionayList = {"PPA" = 11000, "Python" = 15000, "LSP" = 13500, "Angular" = 19000, "LB" = 15000, "C#" = 20000}
    for i in DisctionayList:
        print("Batch Name is", i , " Fee is : ", DisctionayList[i])

if __name__ == "__main__":
    main()