#print shortest common supersequence (lcss) 
#given two str and we have to print the shortest string that has both x and y as subsequence

str1=["h","e","l","l","o"]
str2=["g","e","e","k"]

#for printing first we have to form the matrix with the help of lcs
#for printing this problem is similar to lcs printing 

n=len(str1)
m=len(str2)

t=[]
for i in range(n+1):
  col=[]
  for j in range(m+1):
    col.append(0)
  t.append(col)

def printLcss(str1,str2,n,m,t):
  #intialization
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
  #now till here we have created the matrix by the help of this matrix we would print the value
  s = "" #empty string for storing the value
  n=i
  m=j
  while i>0 and j>0: #keep in mind if i and j greater than 0 then this loop will run
    if str1[i-1]==str2[j-1]:
      s=s+str1[i-1]
      i=i-1
      j=j-1
    else:
      if(t[i][j-1]>t[i-1][j]):
        s=s+str2[j-1]
        j=j-1
      else:
        s=s+str1[i-1]
        i=i-1
  #now here we see if any i or j is remaining then we will print whole i or j
  while i>0:
    s=s+str1[i-1]
    i=i-1
  while j>0:
    s=s+str2[j-1]
    j=j-1
  #now for getting result we will reverse the value bcz we traverse from backside 
  return s[::-1]

print(printLcss(str1,str2,n,m,t))
