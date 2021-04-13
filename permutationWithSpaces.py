def generate(inputs,output):
    if len(inputs)==0:
        print(output)
        return
    first = output
    second = output
    first= first+("_")+inputs[0] 
    second = second+inputs[0]
    if len(inputs) == 1:
        inputs = ""
    else:
        inputs = inputs[1:]
    generate(inputs,first)
    generate(inputs,second)
    return

inputs = "abcd"
output = inputs[0]
inputs = inputs[1:]
print(generate(inputs,output))

    
