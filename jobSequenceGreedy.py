#job sequencing with deadline greedy problem
#this is related to greedy because in this problem we have select max and min and work on that
#we have profit per job
#deadlines of each job
#we have to find the sequence of job to be done and max profit
job = ["j1","j2","j3","j4","j5"]
deadline = [3,4,4,2,3,1,2]
m = len(deadline)
profit = [35,30,25,20,15,12,5]
index = list(range(m))
index.sort(key=lambda i : profit[i],reverse = True)
profit_m = 0
max_time = max(deadline)
min_m = -1
total_work = max_time 
arr = [0]*max_time
flag = False
for i in index:
  value = deadline[i]-1
  flag = False
  #here we use flag because if a object have max time at index [0] it will get repeated
  for j in range(value,min_m,-1):
    if arr[j] == 0 and flag == False:
      arr[j] = job[i]
      profit_m+= profit[i]
      total_work = total_work-1
      flag = True
  if total_work == 0:
    print(arr)
    print(profit_m)
    #print(index)
    break    


