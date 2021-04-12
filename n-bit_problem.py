#wap to print n-bit binary number having 1's than 0's for any prefix
#input n = 5  output-->10110,11010,10101


def solve(zero,one,output,n):
    if n == 0:
        print(output)
        return
    #we create two variables for two nodes
    first = output
    second = output
    first += ("1")
    solve(zero,one+1,first,n-1)
    if zero<one:
        second+= ("0")
        solve(zero+1,one,second,n-1)
    return


n = 3
zero = 0
one = 0
output = ""
result = solve(zero,one,output,n)
print(result)
