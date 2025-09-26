#bubble sort algorithm in python
List = [32,45,12,78,1,0,3,0,13,89,90,11,67,67]

temp = 0

for i in range(0,len(List)):
    for j in range(i+1,len(List)):
        if List[i] > List[j]:
            temp = List[i]
            List[i] = List[j]
            List[j] = temp

for k in range(0,len(List)):
    print("num",k+1,"=", List[k])


