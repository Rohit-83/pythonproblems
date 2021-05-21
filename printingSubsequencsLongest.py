#print longest common subsequence
#given two array and we have to print longest common subsequence

#for this first we have to find the length of longest common subsequence and after that we have to print 
arr1 = ["a","b","c","d","g","h"]
arr2 = ["a","e","d","f","h","r"] 
n = len(arr1)
m = len(arr2)

t = []
for i in range(n+1):
  col = []
  for j in range(m+1):
    col.append(0)
  t.append(col)

def longest(arr1,arr2,n,m,t):
  #initialization
  for i in range(n+1):
    for j in range(m+1):
      if i==0 or j == 0:
        t[i][j] = 0
  
  for i in range(1,n+1):
    for j in range(1,m+1):
      if arr1[i-1] == arr2[j-1]:
        t[i][j] = 1+t[i-1][j-1]
      else:
        t[i][j] = max(t[i-1][j],t[i][j-1])
  #return t[n][m]

  i = n
  j= m
  value = ""
  while i>0 and j>0:
    if arr1[i-1] == arr2[j-1]:
      value+=arr1[i-1]
      i= i-1
      j= j-1
      #value =value+arr1[i]
    else:
      if t[i][j-1]>t[i-1][j]:
        j= j-1
      else:
        i=i-1
  return value[::-1]

print (longest(arr1,arr2,n,m,t))
