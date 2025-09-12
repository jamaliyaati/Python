List = [15, 21, 13, 16]

search = int(input("Enter a number to search: "))
index = 0
found = False

while not found and index < len(List):
    if search == List[index]:
        found = True
        print("Number found at index: ", index + 1)
    else:
        index += 1

if not found:
    print("Number not found in arrray")
