#Linear Search Function
#pass an array as parameter and string
#value which you have to find
letters = ["a","b","c","d","e","f","g"]
#           0   1   2   3   4   5   6

def linearsearch(array,search):
    for x in range(len(array)):
        if array[x] == search:
            return x
    else:
        return "not found"

user = input("enter the string to search: ")
temp = linearsearch(letters,user)
print(temp)
