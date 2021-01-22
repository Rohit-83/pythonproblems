class Customer:
    
    def __init__(self,name,gender,address):
	    self.name=name
	    self.gender=gender
	    self.address=address
    def edit_profile(self,new_name,new_city,new_pincode):
        self.name=new_name
        self.address.change_address(new_city,new_pincode)
        
class Address:

    def __init__(self,city,pincode,state):
        self.city=city
        self.pincode=pincode
        self.state=state

    def change_address(self,new_city,new_pincode):
        self.city=new_city
        self.pincode=new_pincode
        
        
    
        
    
ad=Address("gaya",823001,"bihar")
c2=Customer("rony","f",ad)
c2.edit_profile("rohit","goa",213141)
print(c2.name)
print(c2.address.pincode)
