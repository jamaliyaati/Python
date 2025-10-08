#Find the sum of all the numbers
#in the list that are greater than 10
numbers = [10, 56, 34, 9, 4, 13, 78, 2]

sum = 0
for x in range(len(numbers)):
    if numbers[x] > 10:
        sum = sum + numbers[x]
print("the sum of numbers greater then 10 is: ",sum)
