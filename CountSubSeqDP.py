#count no. of longest common subsest subsequence 
#with dynamic approach
arr1 = ["a","b","c","d","g","h"]
arr2 = ["a","e","d","f","h","r"]
n = len(arr1)
m = len(arr2)
t = []
n = len(arr1)
m = len(arr2)
for i in range(n+1):
  col = []
  for j in range(m+1):
    col.append(-1)
  t.append(col)
def counting(arr1,arr2,n,m,t):
  if n==0 or m==0:
    return 0
  if t[n][m] != -1:
    return t[n][m] 
  if arr1[n-1] == arr2[m-1]:
    t[n][m] = (1+counting(arr1,arr2,n-1,m-1,t))
    return 1+counting(arr1,arr2,n-1,m-1,t)
  else:
    t[n][m] = max(counting(arr1,arr2,n-1,m,t),counting(arr1,arr2,n,m-1,t))
    return max(counting(arr1,arr2,n-1,m,t),counting(arr1,arr2,n,m-1,t))
  return t[n][m]
print(counting(arr1,arr2,n,m,t))
