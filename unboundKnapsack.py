#unbound knapsack
#unbound knapsack without memoization
#basic approach
wt = [5,10,15]
W = 100
n = len(wt)
total = 0
value = [10,30,20]
ratio = [v/w for v,w in zip(value,wt)]
index = list(range(n)) 
index.sort(key = lambda i: ratio[i],reverse=True)
for i in index:
  flag = True
  while flag == True:
    if wt[i]<=W:
      total+=value[i]
      W=W-wt[i] 
    else:
      flag = False 
print(total)


#unbound knapsack 
#given an wt array  and value array and a knapsack we have to find the maximum profit and W i.e. max weight of knapsack
#here we can repeat the item i.e we can store the item more than one time 

wt = [1,3,4,5]
W = 8
value = [10,40,50,70]
t = []#creation of matrix 
n = len(wt)
for i in range(n+1):
  col = []
  for j in range(W+1):
    col.append(0)
  t.append(col)

def unbound_knapsack(arr,n,W,value,t):
  #initialization
  for i in range(n+1):
    for j in range(W+1):
      if i == 0:
        t[i][j] = 0
      if j == 0:
        t[i][j] = 0 
  for i in range(1,n+1):
    for j in range(1,W+1):
      if arr[i-1] <= j:
        t[i][j] = max(value[i-1]+t[i][j-arr[i-1]],t[i-1][j])
      else:
        t[i][j] = t[i-1][j]

  return t[n][W] 

print(unbound_knapsack(wt,n,W,value,t))
