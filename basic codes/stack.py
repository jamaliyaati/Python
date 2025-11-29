List = [""] * 5
StackPointer = - 1
Length = len(List)
def push(value):
    global StackPointer, Length
    if StackPointer == Length:
        print("full")
        return False

    else:
        List[StackPointer] = value
        StackPointer = StackPointer + 1
        return True

def pop():
    global StackPointer
    if StackPointer == 0:
        return False
    else:
        StackPointer = StackPointer - 1
        return True
pop()
pop()
pop()
print(List)
print(StackPointer)

