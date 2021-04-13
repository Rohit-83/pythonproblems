#balance paranthesis generator
#input = 3 output-->("((()))","()(())","()()()"...

def balance(opens,close,output,l):
    if (opens == 0 and close == 0):
        l.append(output)
        return
    first = output
    second = output
    if opens!=0:    
        first = first+"("
        balance(opens-1,close,first,l)
    if close>opens:
        second = second+")"
        balance(opens,close-1,second,l)

    return l


n = 3
opens = n
close = n
output =""
l = []
print(balance(opens,close,output,l))
