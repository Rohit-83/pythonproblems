#equal sum partition problem
#we have been given an array we have to predict that the sum of the subset made from the array are equal or not
#the only way the subset are equal if the final sum of array is even if odd then not possible
arr = [1,15,11,5]
value=sum(arr)
def equal_sum(arr,value):
  if value%2!=0:
    return False
  else:
    return subset_sum(arr,value//2,n,db)

if value%2==0:
  db = []
  n=len(arr)
  row = n+1
  value1 = value//2
  column = value1+1
  for i in range(row):
    col=[]
    for j in range(column):
      col.append(False)
    db.append(col)
def subset_sum(arr,value1,n,db):
  #intialization
  for i in range(row):
    for j in range(column):
      if i==0:
        db[i][j] = False
      if j == 0:
        db[i][j] = True 
  for i in range(1,row):
    for j in range(1,column):
      if arr[i-1]<=j:
        db[i][j] = db[i-1][j-arr[i-1]] or db[i-1][j]
      else:
        db[i][j] = db[i-1][j]
  return db[n][value1]

print(equal_sum(arr,value))
