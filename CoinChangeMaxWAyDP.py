#coin change problem - maximum no. of ways 
#given an packet of change coins and a sum which we have to get
coin = [2,1,3]
value = 4
#we have to find the max. no. of ways we can make value 10 by using given coin 
#we can use coin more than one time so this is unbound knapsack 
#this problem is similar to max. subset sum

t = []
n =len(coin)
for i in range(n+1):
  col = []
  for j in range(value+1):
    col.append(0)
  t.append(col)

def maxway(coin,value,n,t):
  #initialize 
  for i in range(n+1):
    for j in range(value+1):
      if i == 0:
        t[i][j] = False 
      if j == 0:
        t[i][j] = True 
  for i in range(1,n+1):
    for j in range(1,value+1):
      if coin[i-1]<= j:
        t[i][j] = t[i][j-coin[i-1]]+t[i-1][j] 
      else:
        t[i][j] = t[i-1][j]
  return t[n][value]

print(maxway(coin,value,n,t))
