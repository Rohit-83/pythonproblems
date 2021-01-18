def palindrome(str):
    if len(str)<=1:
        return "palindrome"
    elif str[0]==str[-1]:
        return palindrome(str[1:-1])
    else:
        return "Not Palindrome"
a=palindrome("amma")
print(a)
