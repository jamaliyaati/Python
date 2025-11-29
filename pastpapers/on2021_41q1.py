def Unknown(X, Y):
    if X < Y:
        print(str(X + Y))
        return Unknown(X + 1, Y) * 2
    elif X == Y:
        print(1)
        return 1
    else:
        print(str(X + Y))
        return int(Unknown(X - 1, Y) / 2)
    
print("10 and 15")
Unknown(10,15)
print("10 and 10")
Unknown(10,10)
print("15 and 10")
Unknown(15,10)


