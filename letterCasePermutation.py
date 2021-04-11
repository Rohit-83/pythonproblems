#input-->a1B2  output-->(a1B2,A1B2,a1b2,A1b2)
def convert(input,output):
  if len(input)==0:
    print(output)
    return
  first = output
  second = output 
  if input[0].isnumeric():
    first+=input[0]
    if len(input) == 1:
      input = ""
    else:
      input=input[1:]
    convert(input,first)
  else:
    first = first+input[0].upper()
    second = second+input[0].lower()
    if len(input) == 1:
      input = ""
    else:
      input=input[1:]
    convert(input,first)
    convert(input,second)
  return

input = "a1B2"
output = ""
print(convert(input,output))
