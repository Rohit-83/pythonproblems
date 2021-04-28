#subset sum problem
arr= [2,4,7,8,10]
sum = 11
#it is similar to knapsack bcz here also a arr is given and we have to choose item from that
#kept in knapsack
n = len(arr)
#create a matrix
dp = []
for i in range(n+1):
  col = []
  for j in range(sum+1):
    col.append(False)
  dp.append(col)
def subset(arr,sum,dp,n):
  #initialization
  for i in range(n+1):
    for j in range(sum+1):
      if i==0:
        dp[i][j] = False
      if j==0:
        dp[i][j] = True

  for i in range(n+1):
    for j in range(sum+1):
      if arr[i-1]<=j:
        dp[i][j] = dp[i-1][j-arr[i-1]] or dp[i-1][j]
      else:
        dp[i][j] = dp[i-1][j]

  return dp[n][sum]
print(subset(arr,sum,dp,n))
