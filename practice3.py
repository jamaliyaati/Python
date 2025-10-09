#reverse the order of the array
numbers=[10,32,24,56,75,86]
reverse=[]
y=5

for x in range(len(numbers)):
    reverse.append(numbers[y])
    y=y-1
print(reverse)
