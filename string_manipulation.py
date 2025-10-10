def name(fullname):
    length = len(fullname)
    firstlength = 0
    for x in range(length):
        if fullname[x] != " ":
            firstlength = firstlength + 1
        else:
            break
    firstname = fullname[0:firstlength]
    lastname = fullname[firstlength+1:length]

    return firstname,lastname

name_input = input("enter a name ")
first, last = name(name_input)
print("firstname: "+ first)
print("lastname: "+ last)


