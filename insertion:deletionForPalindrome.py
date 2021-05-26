#minimum number of deletion/insertion to make a string palindrome

str1=["a","e","b","c","b","d","a"]
#for palindrome we have to reverse the given str for getting the second string 
#to make a liitle bit similar like lcs problem
str2=str1[::-1]
n=len(str1)
t=[]
for i in range(n+1):
  col=[]
  for j in range(n+1):
    col.append(0)
  t.append(col)

def mindeletion(str1,str2,n,t):
  #initialization done
  for i in range(1,n+1):
    for j in range(1,n+1):
      if str1[i-1]==str2[j-1]:
        t[i][j] = 1+t[i-1][j-1]
      else:
        t[i][j] = max(t[i-1][j],t[i][j-1])
  value =t[n][n]
  return n-value
print(mindeletion(str1,str2,n,t))
 
