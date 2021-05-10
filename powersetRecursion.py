#power set or subset both are same 

def powerset(input,output):
  if len(input) == 0:
    print(output,end="")
    return
  first = output
  second = output
  second=second+input[0]
  if len(input) == 1:
    input = ""
  else:
    input = input[1:]
  powerset(input,first)
  powerset(input,second)
  return ""

input = "abcde"
output = " "
a = powerset(input,output)
print(a)
