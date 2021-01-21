#map function
#syntax map(function(),iterable...)
list1=[1,2,3,4]
square1=map(lambda i:i*i,list1)
print(list(square1))

#passing multiple iterable
list2=[3,2,1,5]
ad=map(lambda list1,list2:list1+list2,list1,list2)
print(list(ad))

#filter function
#syntax filter(function(),iterable)

num=filter(lambda i:i%2==0,list1)
print(list(num))

#reduce
#for using this function we have to import functools
import functools
a=functools.reduce(lambda i,j:i+j+3 , list1)
print(a)


