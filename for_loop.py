largest = 0
for x in range(5): #runs from 0 to 4 so runs 5 times.
    number = float(input("enter a number: "))
    if number > largest:
        largest = number
print(largest)