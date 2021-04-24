#wap to solve 0-1 knapsack problem with dynamic approach
#recursive function
#memoization

#first step is we we first make choice diagram after that recursive code and after that memoization
#normal recursion code
def knapsack(weights,profit,capacity,n):
  #base case
  if n == 0 or capacity ==0:
    return 0
  #choice diagram code
  if weights[n-1]<= capacity:
    #either we choose the element or not we have to select from 2 cases here
    return max(profit[n-1] + knapsack(weights,profit,capacity-weights[n-1],n-1),knapsack(weights,profit,capacity,n-1))
  elif (weights[n-1]>capacity):
    return knapsack(weights,profit,capacity,n-1)
weights = [10,20,30]
profit = [60,100,120]
capacity = 50
n = len(weights)
print(knapsack(weights,profit,capacity,n))



#now we convert the recursive code into meoization
#for memoization we have to make a matrix
#where row and columns are the changable parameters means
#we have to observ from recursion fucntion which parameter is changing
arr = []
row = 4 #we take this value with the help of contstrains
columns = 52 #this value also taken from constraints
for i in range(row):
  col = []
  for j in range(columns):
    col.append(-1)
  arr.append(col)

def knapsackm(weights,profit,capacity,n,arr):
  if n==0 or capacity == 0:
    return 0
  #here we write the memoization code for checking if the above value lies in the matrix or not
  #here n and capcaity are row and column
  if arr[n][capacity] != -1:
    return arr[n][capacity]
  if weights[n-1] <= capacity:
    #first we store the value in list which help in future if ask for same then we don't calculate
    arr[n][capacity] = max(profit[n-1]+knapsackm(weights,profit,capacity-weights[n-1],n-1,arr),knapsackm(weights,profit,capacity,n-1,arr))
    return max(profit[n-1]+knapsackm(weights,profit,capacity-weights[n-1],n-1,arr),knapsackm(weights,profit,capacity,n-1,arr))
  elif weights[n-1] > capacity:
    arr[n][capacity] = knapsackm(weights,profit,capacity,n-1,arr)
    return knapsackm(weights,profit,capacity,n-1,arr)

print(knapsackm(weights,profit,capacity,n,arr))

