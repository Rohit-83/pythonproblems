#recursion
#wap to reverse a string using recursion.

def reverse(str1):
    if len(str1) == 0:
        return
    temp = str1[0]
    reverse(str1[1:])
    print(temp,end)
#print(reverse("123"))
*************************************************

#wap to check palindrome

def check_palindrome(str):
    if len(str)<=1:
        return True
    if str[0]==str[-1]:
        return check_palindrome(str[1:-1])
    return False
#print(check_palindrome("nuhfhn"))
*************************************************

#wap to to fibonacii of given number

def fibonaci(num):
    if num == 0 or num == 1:
        return num
    return fibonaci(num-1)+fibonaci(num-2)

print(fibonaci(4))
**************************************************



        
