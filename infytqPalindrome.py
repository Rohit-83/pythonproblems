#for a given positive num identify the palindrome by performning the operations
#add num and its reverse
#check whether it is palindrome or not if not then do that process again

def check(num):
  value = str(num)
  reversed = value[::-1]
  new_value = num+int(reversed)
  while True:
    if str(new_value) == (str(new_value))[::-1]:
      return new_value
    else:
      new_value = new_value+int(reversed)

print(check(1234))
