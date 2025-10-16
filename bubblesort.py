#bubble sort algorithm in python
list = [32,45,12,78,1,0,3,0,13,89,90,11,67,67]
temp = 0
length = len(list)

for x in range(length):
    for j in range(x+1,length):
        if list[x] > list[j]:
            temp = list[j]
            list[j] = list[x]
            list[x] = temp

print(list)