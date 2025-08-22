List = [15,21,13,16]
max_index = 4

search = int(input("Enter a number to search: "))
index = 0
found = False

while not found and index <= max_index :
    if search == List[index-1]:
        found = True
        print("Number found at index: ", index)
    else:
        index += 1

if index-1 == max_index and not found:
    print("Number not found in array")

