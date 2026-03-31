# inbuilt function ( we can not modify contains )
def Sub(A, B):              # ox100
    return A - B

# Decorator
def SmartSub(fptr):         # ox200
    def Inner(A, B):        # ox300
        if A < B:
            A, B = B, A
        return fptr(A, B)       # return ox100()
    return Inner                # return ox300

def main():
    SubX = SmartSub(Sub)        # ox200 (ox100)

    Ret = SubX( 10, 7 )         # ox300( 10, 7 )
    print("Subtraction is : ", Ret)

    Ret = SubX(7, 10)           # ox300( 7, 10)
    print("Subtraction is : ", Ret)

if __name__ == "__main__":
    main()