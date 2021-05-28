#recursive approach
import sys
def solve(arr,i,j):
  #base case
  if i>=j:
    return 0
  mn = sys.maxsize
  for k in range(i,j):
    temp = solve(arr,i,k)+solve(arr,k+1,j)+(arr[i-1]*arr[k]*arr[j])
    if (temp < mn):
      mn=temp
  return mn

i=1
arr=[10,20,30]
n=len(arr)
j=n-1
print(solve(arr,1,n-1))


#bottom up approach memoization tabulization (overlapping subsproblem)
import sys
def solve1(arr,i,j,t):
  #base case
  if i>=j:
    return 0
  if t[i][j]!=-1:
    return t[i][j]
  mn=sys.maxsize
  for k in range(i,j):
    temp=solve1(arr,i,k,t)+solve1(arr,k+1,j,t)+arr[i-1]*arr[k]*arr[j]

    if temp<mn:
      mn=temp
  t[i][j] = mn
  return mn

t=[]
arr=[10,20,30,40,50,60,70,80,90,100]
n=len(arr)
for i in range(100):
  col=[]
  for j in range(100):
    col.append(-1)
  t.append(col)
print(solve1(arr,1,n-1,t))
