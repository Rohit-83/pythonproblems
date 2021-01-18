def arms(num):
    length1=len(str(num))
    num1=num
    sum=0
    while num1>0:
        rem=num1%10
        sum=sum+(rem**length1)
        num1=num1//10
    if sum==num:
        return "Armstrong"
    else:
        return "wrong"


a=arms(54749)
print(a)
