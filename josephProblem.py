def joseph(index,arr,k,ans):
    if len(arr) == 1:
        ans = arr[0]
        print(ans)
        return
    index = (index+k)%len(arr)
    arr.pop(index)
    joseph(index,arr,k,ans)
    return

index = 0
arr = []
n = 40
k = 7
k=k-1
ans = -1
for i in range(1,n+1):
    arr.append(i)
print(joseph(index,arr,k,ans))
    
