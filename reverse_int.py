x = int(input("enter value of x: "))
string = str(x)
reverse = string[::-1]
length = len(reverse)


if x < 0:
    minus ="-"+ reverse[0:length-1]
    ans = int(minus)
else:
    ans = int(reverse)

if ans <= 2^31 - 1 or ans >= -2^31:
    print(0)
else:
    print(ans)

