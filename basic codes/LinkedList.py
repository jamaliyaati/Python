
data = [27, 19, 36, 42, 16, None, None, None, None, None, None, None]
pointer = [-1, 0, 1, 2, 3 ,6 ,7 ,8 ,9 ,10 ,11, -1]

startpointer = 4

def search(item):
    global startpointer, data, pointer
    findpointer = startpointer
    found = False
    while found == False and findpointer != -1:
        if data[findpointer] == item:
            found = True
        else:
            findpointer = pointer[findpointer]
    return findpointer




