def knapsack(weights,profit,capacity,n):
  if n == 0 or capacity ==0:
    return 0
  if weights[n-1]<= capacity:
    capacity = capacity-weights[n-1]
    return max(profit[n-1] + knapsack(weights,profit,capacity-weights[n-1],n-1),knapsack(weights,profit,capacity,n-1))
  elif (weights[n-1]>capacity):
    return knapsack(weights,profit,capacity,n-1)
weights = [10,20,30]
profit = [60,100,120]
capacity = 50
n = len(weights)
print(knapsack(weights,profit,capacity,n))
