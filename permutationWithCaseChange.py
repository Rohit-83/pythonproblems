#wap to do permutation with case change
#input --> ab
#output --. ("ab","Ab","AB","aB")

def solve(inputs,output):
    if len(inputs) == 0:
        print(output)
        return
    first = output
    second = output
    first = first+inputs[0].upper()
    second  = second+inputs[0].lower()
    if len(inputs) == 1:
        inputs = ""
    else:
        inputs = inputs[1:]
    solve(inputs,first)
    solve(inputs,second)
    return

inputs = "ab"
output = ""
print(solve(inputs,output))
