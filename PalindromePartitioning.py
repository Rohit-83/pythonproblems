#palindrome partioning using recursion --rem
#given a string ,a partioning of the string is palindrome partioning if every partition is a palindrome
#find the mininmun number of partition 
#maximum it would be len(string)-1 i.e. partition for every element
import sys
s="nama"
#first step-> we have to find i and j
#i=0
#=len(s)-1
def solve(s,i,j):
  #base case. #second step
  if i>=j:
    return 0
  if (partition(s,i,j)==True):#base case
    return 0
  mn=sys.maxsize
  #third step We have to iterate k
  for k in range(i,j):
    # value -->third step
    temp = solve(s,i,k)+solve(s,k+1,j)+1

    if temp<mn:
      mn=temp
  return mn
 
def partition(s,i,j):
  n=len(s)
  if i>=j:
    return True
  if (s[i]!=s[j]):
    return False
  return partition(s,i+1,j-1) 

print(solve(s,0,len(s)-1))
