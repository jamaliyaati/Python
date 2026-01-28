try:
    x = int(input("value1: "))
    y = int(input("value2: "))
    
    z = x//y

    j = len(z)

    
    print(j)

except NameError:
        print("variable n ot defined")

except TypeError:
        print("wrong data type")

except ZeroDivisionError:
        print("zero division error")

except ValueError:
       print("incorrect value")

try:
    f = open("test.txt", "r")
    line = f.readline()
    f.close()
except FileNotFoundError:
    print("file not found")

