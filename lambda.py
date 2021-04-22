#lambda function normal
func=lambda i,j : i*j
print(func(5,6))
#lambda function using if and else
func1=lambda i: (i*i if i%2==0 else -i)
print(func1(101))



#application of lambda and sort function
#wap to sort an array according to another array
cars = ["Ford","Merccitiz","BMW","VW"]
#we create an array with value 1 to 4
index = list(range(4))
index.sort(key = lambda i:cars[i],reverse = True)
print(index)
