class Parent:
    def __init__(self,num):
        self.__num=num
    def get_num(self):
        return self.__num

class Child(Parent):

    def show(self):
        print("hye you are in child")

c1=Child(10)
c1.show()
print(c1.get_num())



#super_keyword

class Phone:

    def __init__(self,price,brand,camera):
        print("inside parent")
        self.price=price
        self.brand=brand
        self.camera=camera

class Smartphone(Phone):

    def __init__(self,price,brand,camera,os,ram):
        super().__init__(price,brand,camera)
        self.os=os
        self.ram=ram
        print("inside child")

s1=Smartphone(2200,"samsung",2,"android","5gb")
print(s1.price)
    
