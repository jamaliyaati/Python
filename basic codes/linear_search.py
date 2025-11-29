numbers = [15, 21, 13, 16, 18, 20, 10, 10, 50]

search = int(input("Enter a number to search: "))

for x in range(len(numbers)):
    if numbers[x] == search:
        print("found at index:",x)