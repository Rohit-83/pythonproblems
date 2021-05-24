#longest palindromic subsequence
#given a sequence we have to find the length of longest common subsequence
a = ["a","g","b","c","b","a"]
#for finding the longesst palindromic we use lcs
#but lcs have 2 string so for getting second string we reverse the first
b = ["a","b","c","b","g","a"]

n = len(a)
m = len(b)

t =[]
for i in range(n+1):
  col=[]
  for j in range(m+1):
    col.append(0)
  t.append(col)

def lps(a,b,n,m,t):
  #initialization
  for i in range(n+1):
    for j in range(m+1):
      if i==0 or j==0:
        t[i][j] = 0
  
  for i in range(1,n+1):
    for j in range(1,m+1):
      if a[i-1] == b[j-1]:
        t[i][j] = 1+t[i-1][j-1]
      else:
        t[i][j] = max(t[i-1][j],t[i][j-1])
  return t[n][m]

print(lps(a,b,n,m,t))
