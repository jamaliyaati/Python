
num1 = float(input("enter a number: "))
num2 = float(input("enter a number: "))
num3 = float(input("enter a number: "))

if num1 > num2 and num1 > num3:
    largest = num1
    print("largest number is: ", largest)
elif num2 > num3 and num2 > num1:
    largest = num2
    print("largest number is: ", largest)
elif num3 > num1 and num3 > num2:
    largest = num3
    print("largest number is: ",largest)



