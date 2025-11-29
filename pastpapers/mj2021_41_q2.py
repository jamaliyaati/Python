arrayData = [10,5,6,7,1,12,13,15,21,8]

def linearsearch(value):
    global arrayData
    flag = False
    for i in range(len(arrayData)):
        if value == arrayData[i]:
            print("found at index: ",i+1)
            flag = True
    if not flag:
        print("not found")
        return False
    

search = int(input("enter a value to search: "))
linearsearch(search)

def bubbleSort():
    global arrayData
    length = len(arrayData)
    temp = 0


    for x in range(length):
        for y in range(x+1,length):

            if arrayData[x] < arrayData[y]:
                temp = arrayData[x]
                arrayData[x] = arrayData[y]
                arrayData[y] = temp

