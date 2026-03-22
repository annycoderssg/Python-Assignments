# Task: Function Name
# Elements : List of data elements
def FilterX( Task, Elements ):
    arrResult = []
    for no in Elements: 
        if( True == Task(no) ):
            arrResult.append(no)
    return arrResult

def MapX( Task, Elements):
    arrResult = []
    for no in Elements:
        arrResult.append(Task(no))

    return arrResult

def ReduceX( Task, Elements):
    intResult = 0
    for no in Elements:
        intResult = Task(no,intResult)

    return intResult