#input 5 numbers from the user and print how
# many are positive and how many are negative

c_pos = 0
c_neg = 0
for x in range(5):
    number = float(input("enter a num: "))
    if number >= 0:
        c_pos = c_pos + 1
    elif number < 0:
        c_neg = c_neg + 1

print("number of positive numbers: "+ str(c_pos))
print("number of negative numbers: "+ str(c_neg))