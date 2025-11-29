#create a function that finds
#the largets value in a list
number=[45,34,23,87,96,23]

def largest(array):
    largenum = 0
    for x in range(len(array)):
        if array[x] > largenum:
            largenum = array[x]
    return largenum

temp = largest(number)
print(temp)

