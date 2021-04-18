#input = "ABC"
#wap to print all permutation
#output--> "ABC","BAC","CAB","ACB","BCA","CBA"

string = "ABC"
#we convert this into list bcz string object does not supporr changing and assignment
output = list(string)
n=len(string)
l=0
r=n-1
def permutation(string,output,l,r):
  if l==r:
    print("".join(output),end = " ")
  else:
    for i in range(l,r+1):
      output[l],output[i] = output[i],output[l]
      permutation(string,output,l+1,r)
      #backtrack
      output[l],output[i] = output[i],output[l]
  return ""
print(permutation(string,output,l,r))

  
