#sequence pattern matching
#we have been given a str'a' and we have to check that if str'a' is subsequence in b or not
#or we can say that check a is present in b or not in same order

str1=["a","b","c"]
str2=["a","d","z","p","c","b"]

#hint-if we see that for str1 to be present in str2 then we have to see that abc present or not in same order
#or,we can say we can lcs subsequence that length of subsequence should be equal to str1

n=len(str1)
m=len(str2)
t=[]
for i in range(n+1):
  col=[]
  for j in range(m+1):
    col.append(0)
  t.append(col)

def patternMatching(str1,str2,n,m,t):
  #initialization
  for i in range(n+1):
    for j in range(m+1):
      if i==0 or j==0:
        t[i][j] = 0
  
  for i in range(1,n+1):
    for j in range(1,m+1):
      if str1[i-1]==str2[j-1]:
        t[i][j] = 1+t[i-1][j-1]
      else:
        t[i][j] = max(t[i-1][j],t[i][j-1])
  value =t[n][m]

  if value==n:
    return True
  else:
    return False

print(patternMatching(str1,str2,n,m,t))
