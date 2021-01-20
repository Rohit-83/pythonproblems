#making function flexible
#using argument as *args which have type tuple
#and **kwargs which have type dictionary
def add(*args):
    sum1=0
    for i in args:
        sum1=sum1+i
    return sum1
print(add(1,2,3,4))

def detail(**kwargs):
    for i,j in kwargs.items():
        print(f"{i}:{j}")
my=detail(name="rohit",gender="male",age=20,)
print(my)

#priority of arguments
''' parameter
    *args
    default parametr
    **kwargs'''
def mult1(num,*args):
    product=1
    for i in args:
        product=product*i
    return product
print(mult1(4,2,3))
#here we get value 6 because num take one value i.e. 4 
