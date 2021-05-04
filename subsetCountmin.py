#count the number of subset with the given sum differance
#given an array and subset differance we have to find no. of possible subset
arr = [1,2,5,3]
diff = 1
sum1 = sum(arr)
#we have been given s1-s2 = diff
#and we know that s1+s2 = sum1
#from above equation we have s1=diff+sum1//2
#sum of the arr always came odd
s1 = diff+sum1//2 
#now this problem is similar to  count subset sum 
t = []
n = len(arr)
for i in range(n+1):
  col = []
  for j in range(s1+1):
    col.append(0)
  t.append(col)
def count_subset(arr,s1,n,t):
  #initilization
  for i in range(n+1):
    for j in range(s1+1):
      if i == 0:
        t[i][j] = 0
      if j == 0:
        t[i][j] = 1
  
  for i in range(1,n+1):
    for j in range(1,s1+1):
      if arr[i-1]<=j:
        t[i][j] = t[i-1][j-arr[i-1]] + t[i-1][j]
      else:
        t[i][j] = t[i-1][j]
  return t[n][s1]

print(count_subset(arr,s1,n,t))
