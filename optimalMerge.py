#Problem:optimal merge pattern
#Input:Given n sorted/unsortded files
#Output:Merge n files in a minimum amount of time.
#always we should merge with the small pair

total_time = 0
arr = [6,5,2,3]
l = []
def optimal_merge(arr,total_time,l):
  arr.sort()
  if len(arr) == 1:
    return
  value1 = arr[0]
  value2 = arr[1]
  value3 = value1+value2
  l.append(value3)
  arr.pop(0)
  arr.pop(0)
  total_time += value3
  arr.insert(0,value3)
  optimal_merge(arr,total_time,l)
  return sum(l)

print(optimal_merge(arr,total_time,l))
