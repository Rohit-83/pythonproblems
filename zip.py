#application of zip function
#if we have to add two arr with their respective elements
#then we use zip
a = [1,2,3]
b = [3,4,5]
#now we use list comprehension
value = [x+y for x,y in zip(a,b)]
print(value)


