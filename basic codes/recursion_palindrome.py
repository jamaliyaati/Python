def palindrome(x):
    x = x.lower().replace(" ","")
    if len(x) == 1:
        return True
    elif x[0] != x[-1]:
        return False
    return palindrome(x[1:-1])


word = input("enter: ")
if palindrome(word):
    print(f"{word} is a palindrome!")
else:
    print(f"{word} is not a palindrome.")