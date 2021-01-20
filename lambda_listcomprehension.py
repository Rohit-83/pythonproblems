#lambda function normal
#syntax lambda input:expression
#it can have more than one input but it can have only one expression.
func=lambda i,j : i*j
print(func(5,6))

#lambda function using if and else
func1=lambda i: (i*i if i%2==0 else -i)
print(func1(101))

#listcomprehension
#syntax l=[expression for item in list ]
list1=(1,2,3,4)
l=[i*i for i in list1]
print(l)

#list comprehension with if and else
#using if
#syntax l= [ expression for item in list if condition]
l1=[i+i for i in list1 if i>2]
print(l1)

#using if and else both
#syntax l=[expression if conditiion else expression for item in list]
l2=[i*i if i%2==0 else -i for i in list1]
print(l2)

#dictionary_comprehension
#syntax dict={key:value or expression for key,value in dictionary.items()}
# dict={key:value or expression for item in iterator}
dict1={"name":"rohit","age":20,"gender":"male"}
dict2={key:value for key,value in dict1.items()}
print(dict2)
dict3={key:key*key for key in range(10)}
print(dict3)

#dictionary comprehension when if and else is used
#syntax is same as list comprehension in expression or value we make changes
#value=expression if condition else expression
dict4={key:key*key if key%2==0 else -key for key in range(10)}
print(dict4)

