class Customer:
	def __init__(self,name,gender):
		self.name=name
		self.gender=gender
	def greet(self):
		if self.gender=="male":
			print("hye",self.name,"sir")
		else:
			print("hye",self.name,"mam")
	def intro(self):
		print("hi i am",self.name,"and i am",self.gender)

#collections of object done as we do for list
c1=Customer("rohit","male")
c2=Customer("rony","female")
l=[c1,c2]
for i in l:
    i.intro()
