def main():

    Batches = {"PPA" : 11000, "Python" : 15000, "LSP" : 13500, "Angular" : 19000, "LB" : 15000, "C#" : 20000}

    print(Batches)

    print(type(Batches))

    print(len(Batches))

    print(Batches["Python"])

    for i in Batches:
        print("Batch Name is : ", i , " & Fee is : ", Batches[i])
    
    for key in Batches:
        print(key , Batches[key])

if __name__ == "__main__":
    main()