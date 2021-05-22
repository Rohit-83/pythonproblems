#minimum number of insertion and deletion to transfrom one string into another
#Given two str and we have to delete and insert the charcter in such a way that it 
#convert into second string
str1 = ["h","a","v","e"]
str2 = ["e","a","v"]

n = len(str1)
m = len(str2)

t = []
for i in range(n+1):
  col = []
  for j in range(m+1):
    col.append(0)
  t.append(col)

def convertor(str1,str2,n,m,t):
  #initialization is done already

  for i in range(1,n+1):
    for j in range(1,m+1):
      if str1[i-1] == str2[j-1]:
        t[i][j] = 1+t[i-1][j-1]
      else:
        t[i][j] = max(t[i-1][j],t[i][j-1])
  val = t[n][m]
  
  #we have done this to eliminate the common item from both string
  deletion  = n - val
  insetion = m - val

  return (deletion , insetion)

print(convertor(str1,str2,n,m,t))

