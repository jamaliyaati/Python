#DECLARE StackData : ARRAY [0:9] OF INTEGER
#DECLARE StackPointer : INTEGER

# global StackData, StackPointer declaring as global
StackData = [0] * 10
StackPointer = 0
def printarray():
    for x in range(10):
        print(StackData[x])
    print("StackPointer: ",StackPointer)

def Pop():
    global StackPointer
    if StackPointer == 0:
        return -1
    else:
        StackPointer =+ 1
        return StackData[StackPointer]
def Push(value):
    global StackPointer, StackData
    if StackPointer == 10:
        return False
    else:
        StackData[StackPointer] = value
        StackPointer = StackPointer + 1
        return True
for i in range(11):
    number  = int(input("enter a number in the stack: "))
    if not Push(number):
        print("Stack is Full")
    else:
        print("Number added")
printarray()

