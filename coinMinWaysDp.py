#coin change problem min no of coins/ways
#we have been given an arr contain coin [1,2,5]
#and a sum = [10]
#we have to return minimum no. of ways 
#unbound knapsack bcz repetation of element happen 
import sys
arr = [25,10,5]
sum = 30
t = []
n = len(arr)
for i in range(n+1):
  col = []
  for j in range(sum+1):
    col.append(0)
  t.append(col)

def minWay(arr,sum,n,t):
  #initialize 
  for i in range(n+1):
    for j in range(sum+1):
      if i == 0:
        t[i][j] = sys.maxsize
      if j == 0:
        t[i][j] = 0
  #initialize i ==1 because i==0 is not initialized bcz it does not get proper value and
  #value are set to maximum
  for i in range(1,n+1):
    for j in range(1,sum+1):
      if j == 1:
        if i%j == 0:
          t[i][j] = i//j
        else:
          t[i][j] = sys.maxsize 
  #unbound knapsack
  for i in range(1,n+1):
    for j in range(2,sum+1):
      if arr[i-1]<=j:
        t[i][j] = min(t[i][j-arr[i-1]]+1,t[i-1][j])
      else:
        t[i][j] = t[i-1][j]
  return t[n][sum]

print(minWay(arr,sum,n,t))

