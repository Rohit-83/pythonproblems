#count no. of longest common subsequence
#given two array [a,b,c,d,e,f] and [a,c,e,f,b]
#recursive approach 

arr1 = ["a","b","c","d","g","h"]
arr2 = ["a","e","d","f","h","r"]
n = len(arr1)
m = len(arr2)
def countsubseq(arr1,arr2,n,m):
  #base case
  if n==0 or m==0:
    return 0 
  if arr1[n-1] == arr2[m-1]:
    return 1+countsubseq(arr1,arr2,n-1,m-1)
  else:
    return max(countsubseq(arr1,arr2,n-1,m),countsubseq(arr1,arr2,n,m-1))

print(countsubseq(arr1,arr2,n,m))

