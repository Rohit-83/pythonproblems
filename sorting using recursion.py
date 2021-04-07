#wap to sort an array using recursion 


def sorting(arr):
    #base case
    if len(arr) == 1:
        return
    last_item = arr[-1]
    arr.pop()
    sorting(arr)
    insert(arr,last_item)
    return arr
    
def insert(arr,last_item):
    if len(arr) == 0 or arr[-1]<=last_item:
        arr.append(last_item)
        return
    value = arr[-1]
    arr.pop()
    insert(arr,last_item)
    arr.append(value)
    
arr = [8,7,3,4,5,8]
print(sorting(arr))
