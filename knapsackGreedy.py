#wap to solve fractional knapsack problem
#given -->weights of every item
#profit per items
#max weight that can be taken
#find the maximum weight
weights = [10,20,30]
profit = [60,100,120]
w = 50
def knapsack(weights,profit,w):
    n = len(weights)
    ratios = [p/w for p,w in zip(profit,weights)]
    index = list(range(n))
    index.sort(key = lambda i : ratios[i],reverse = True)
    max_value = 0
    for i in index:
        if weights [i] <= w:
            max_value += profit[i]
            w = w-weights[i]
        else:
            max_value += w*(profit[i]/weights[i])
            break;
    return max_value

print(knapsack(weights,profit,w))
