n = int(input("enter a positive int: "))
print("Sequence in reverse order:", end=" ")
temp = n
count = 0
while  temp != 1:

    if temp % 2 == 0:
        temp //=2
    else:
        temp = (temp * 3) + 1
    count +=1

count2 = count

while count2 >=0:
    temp = n
    i = 0
    while i < count2:
        if temp % 2 == 0:
            temp //= 2
        else:
            temp = (temp * 3) + 1
        i +=1

    print(temp, end=" ")
    count2 -= 1
