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
