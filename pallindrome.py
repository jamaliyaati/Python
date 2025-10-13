flag = False
x = 1235321
string = str(x)
length = len(string)


part1 = []
part2 = []
half = length // 2

if length % 2 == 0:
    for i in range(half):
        part1.append(int(string[i]))
    for j in range(length-1,half-1,-1):
        part2.append(int(string[j]))

else:
    start = length -1
    for k in range(int(half)):
        part1.append(int(string[k]))
    for l in range(start,half,-1):
        part2.append(int(string[l]))

if part1 == part2:
    flag = True
print(flag)


