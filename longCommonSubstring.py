#longest common substring 
#we have given two array and we have to find the length of longest common substring
arr1 = ["a","b","c","d"]
arr2 = ["a","b","c"] 

n = len(arr1)
m = len(arr2)
temp = 0
t = []
for i in range(n+1):
  col=[]
  for j in range(m+1):
    col.append(0)
  t.append(col) 

def longestSubstring(arr1,arr2,n,m,t,temp):
  #initialization
  for i in range(n+1):
    for j in range(m+1):
      if i==0 or j==0:
        t[i][j] = 0
  
  #now for rest row and column
  for i in range(1,n+1):
    for j in range(1,m+1):
      if arr1[i-1] == arr2[j-1]:
        t[i][j] = 1+t[i-1][j-1] 
        temp = max(temp,t[i][j])
      else:
        t[i][j] = 0
  return temp 

print(longestSubstring(arr1,arr2,n,m,t,temp))

