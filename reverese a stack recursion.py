#wap to reverse an stack using recursion without using extra space

def insert(stack,last_element):
    #base condition
    if len(stack) == 0:
        stack.append(last_element)
        return
    value = stack[-1]
    stack.pop()
    insert(stack,last_element)
    stack.append(value)
    return stack
    


def reversed(stack):
    #base condition if len of stack is 1 then it will we reversed already
    if len(stack) == 1:
        return stack
    last_element = stack[-1]
    stack.pop()
    reversed(stack)
    x = insert(stack,last_element)
    return x


stack = [1,2,3,4,5]
print(reversed(stack))
