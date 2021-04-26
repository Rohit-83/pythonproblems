#wap to sum of the digits of the given array
#input = 12345
#output = 11

def getsum(n):
    sum = 0
    for digit in str(n):
        sum+=int(digit)
    return sum


n= 12345
print(getsum(n))
