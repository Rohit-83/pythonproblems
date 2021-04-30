#count of subset 
#we have been given an array and sum and we have to return count that how many subset are possible
arr = [2,3,5,6,8,10]
sum = 10 
t = []
n = len(arr)
for i in range(n+1):
  col=[]
  for j in range(sum+1):
    col.append(0)
  t.append(col)

def count_subset(arr,sum,n,t):
  #intialization
  for i in range(n+1):
    for j in range(sum+1):
      if i == 0:
        t[i][j] = 0
      if j == 0:
        t[i][j] = 1

  for i in range(1,n+1):
    for j in range(1,sum+1):
      if arr[i-1]<=j:
        t[i][j] = t[i-1][j-arr[i-1]] + t[i-1][j]
      else:
        t[i][j] = t[i-1][j]
  return t[n][sum] 

print(count_subset(arr,sum,n,t))

