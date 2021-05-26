#shortest common supersequence find the length
#given two string str1 and str2 find the shortest string that have
#both str1 and str2 as subsequence

str1=["g","e","e","k"]
str2=["e","k","e"]

#in supersequence we have two case if all the character are differant then possible case is
#i.e. max length is len(str1)+len(str2) but if some character are same in both then 
#we write that character only ones that is supersequence 

#in this problem we will first find the length 

n= len(str1)
m=len(str2)
t=[]
for i in range(n+1):
  col=[]
  for j in range(m+1):
    col.append(0)
  t.append(col)

def lcss(str1,str2,n,m,t):
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
  #now we have to subtract the common part i.e lcs we know lcs is common between both
  #thats we have find lcs here
  value = t[n][m]
  return (n+m)-value

print(lcss(str1,str2,n,m,t))
