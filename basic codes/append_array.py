#Input a number from the user
# if that number is in the array
# then print it is already there
# and if not in the array
# then add it into the array
numbers = [15, 21, 13, 16, 18, 20, 10, 10, 50]

num = int(input("enter a number to search: "))
x = 0
flag = False
while x < len(numbers) and flag == False:
    if numbers[x] == num:
        print(num,"is already in the array")
        flag = True
    x = x + 1
if not flag:
    numbers.append(num)
print(numbers)


