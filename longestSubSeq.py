#count no. of longest common subsequence
#given two array [a,b,c,d,e,f] and [a,c,e,f,b]
#recursive approach 

arr1 = ["a","b","c","d","g","h"]
arr2 = ["a","e","d","f","h","r"]
n = len(arr1)
m = len(arr2)
def countsubseq(arr1,arr2,n,m):
  #base case
  if n==0 or m==0:
    return 0 
  if arr1[n-1] == arr2[m-1]:
    return 1+countsubseq(arr1,arr2,n-1,m-1)
  else:
    return max(countsubseq(arr1,arr2,n-1,m),countsubseq(arr1,arr2,n,m-1))

print(countsubseq(arr1,arr2,n,m))


#count no. of longest common subset subsequence using dp
#we have been given two array 
arr1 = ["a","b","c","d","g","h"]
arr2 = ["a","e","d","f","h","r"] 

n = len(arr1)
m = len(arr2)

t = []
for i in range(n+1):
  col=[]
  for j in range(m+1):
    col.append(0)
  t.append(col) 

def longestCommon(arr1,arr2,n,m,t):
  #initialization
  for i in range(n+1):
    for j in range(m+1):
      if (i==0 or j==0):
        t[i][j] = 0
  for i in range(1,n+1):
    for j in range(1,m+1):
      if arr1[i-1]==arr2[j-1]:
        t[i][j] = 1+t[i-1][j-1]
      else :
        t[i][j] = max(t[i-1][j],t[i][j-1])
  return t[n][m]

print(longestCommon(arr1,arr2,n,m,t))
