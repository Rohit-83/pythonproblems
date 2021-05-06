#rod cutting problem (unbound knapsack)
#this probem is same as unbounded knapsack
#given the length of rod and assosiate price per lenth
#find the max price 
length = [1,2,3,4,5,6,7,8] 
price = [3,5,8,9,10,17,17,20]
N = 8 #length of rod 
t = []
n = len(length)
for i in range(n+1):
  col=[]
  for j in range(N+1):
    col.append(0)
  t.append(col)

def rod_cut(length,price,N,t):
  #initialize
  for i in range(n+1):
    for j in range(N+1):
      if i==0 or j==0:
        t[i][j] = 0 
  for i in range(1,n+1):
    for j in range(1,N+1):
      if length[i-1]<=j:
        t[i][j] = max(price[i-1]+t[i][j-length[i-1]],t[i-1][j])
      else:
        t[i][j] = t[i-1][j] 
  return t[n][N] 

print(rod_cut(length,price,N,t))
