#minimal sum differance
#given an array we have to find the minimal sum diffrance of the subset partition
arr= [1,2,7]
#we can get minimal sub differance by partioning like abs(s2-s1) = min where s2 and s1 are sum of subsets
#s2-s1 = min can be written as range-s1-s1 = min. | range-2s1 = min 
t = []
n = len(arr)
sum1 = sum(arr)
for i in range(n+1):
  col = []
  for j in range(sum1+1):
    col.append(False)
  t.append(col)

def minimal_sum_diff(arr,n,sum1,t):
  #initialization
  for i in range(n+1):
    for j in range(sum1+1):
      if i ==0:
        t[i][j] = False
      if j ==0:
        t[i][j] = True
  for i in range(1,n+1):
    for j in range(1,sum1+1):
      if arr[i-1]<=j:
        t[i][j] = t[i-1][j-arr[i-1]] or t[i-1][j]
      else:
        t[i][j] = t[i-1][j] 
  final = []
  for i in range(n,n+1):
    for j in range(sum1//2+1):
      final.append(t[i][j])
  #print(final)
  mins = 100000000
  for i in range(len(final)):
    if final[i] == True:
      mins = min(mins,sum1-2*(i))
      #print(mins)

  return mins


print(minimal_sum_diff(arr,n,sum1,t))
 
