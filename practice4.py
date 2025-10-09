flag = False
count = 0
total = 0

while not flag:
    num = float(input("enter a number: "))
    if num == 0:
        flag = True
    else:
        count = count+1
        total = total + num
if count ==0:
    print("you entered 0")
else:
    print("the avg is: ",total/count)
