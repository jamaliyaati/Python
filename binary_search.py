
List = [1,2,3,4,5,6,7]
item = int(input("Enter a number to search: "))

found=False
lb = 0
ub = (len(List)-1)
mb = 0

while lb<=ub and  found == False :
    mb = (ub + lb)//2
    if List[mb] == item:
        print("Item found at position:", mb+1)
        found = True
    elif List[mb] < item:
        lb = mb + 1
    else:
        ub = mb - 1
if found == False:
    print("Item not found")



