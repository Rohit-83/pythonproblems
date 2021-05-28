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
