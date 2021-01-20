#iterable-->list,set,tuple
#iterator-->map,filter
my_list=[1,2,3,4]
for i in my_list:
    print(i)
square=map(lambda i:i*i , my_list)
#print(square) --> here we only get the address of map object
'''
beacuse iteartor can only iterate one time for iterating more
than one time we convert the map object into list or tuple
'''
square=list(square)
print(square)
for i in square:
    print (i)
