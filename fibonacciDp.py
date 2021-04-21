#dynamic programing
#wap to find fibonaci of a given number n with the help of dp
#in dp we use to store the value and use that value


#noraml recursion method
def fib(n):
    if n == 1 or n==2:
        return 1
    return fib(n-1)+fib(n-2)


#through recursion time taken is more but with dp we can reduce the time
def fibDp(n):
    #we will create an to store prev. calculations
    arr = [None]*(n+2)
    arr[0] = 0
    arr[1] = 1
    arr[2] = 1
    for i in range(3,n+1):
        #now we store the value 
        arr[i] = arr[i-1]+arr[i-2]
    return arr[n]

print(fibDp(6))
