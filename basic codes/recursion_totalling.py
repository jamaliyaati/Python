def total():
    num = int(input("enter a value:"))
    if num == -1:
        return 0
    else:
        return num+total()
        
print(total())