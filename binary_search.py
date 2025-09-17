List = [1, 2, 3, 4, 5, 6, 7]
item = int(input("Enter a number to search: "))

found = False
lb = 0
ub = len(List) - 1
mb = 0

while lb <= ub and not found:
    mb = (ub + lb) // 2
    if List[mb] == item:
        print("Item found at address:", mb + 1)
        found = True
    elif List[mb] < item:
        lb = mb + 1
    else:
        ub = mb - 1
if not found:
    print("Item not found")
