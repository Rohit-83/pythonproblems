import ctypes

class MyList:

  def __init__(self):
    self.capacity=1
    self.n=0
    self.A= self.__make_array(self.capacity)

  def __len__(self):
    return self.n
  
  def append(self,item):
    if self.capacity==self.n:
      #we have to resize the array
      self.__resize(2*self.capacity)
    self.A[self.n]=item
    self.n+=1  

  def __getitem__(self,index):
    if 0<=index<self.n:
      return self.A[index]
    else:
      return "invalid index"

  def pop(self):
    if self.n==0:
      return "empty"
    else:
      print(self.A[self.n-1])
      self.n=self.n-1

  def insert(self,item,pos):
    if 0<=pos<self.n:
      if self.n==self.capacity:
        #resize the array
        self.__resize(2*self.capacity)
      #insert now
      for i in range(self.n,pos,-1):
        #shift the elemnts
        self.A[i]=self.A[i-1]
      #after shifting we have pos to insert the item
      self.A[pos]=item
      self.n+=1
    else:
      return "index error"

  def __delitem__(self,index):
    if 0<=index<self.n:
      for i in range(index,self.n-1):
        self.A[i]=self.A[i+1]

      self.n-=1
    else:
      return "invalid index"

  def remove(self,item):
    for i in range(self.n):
      if self.A[i]==item:
        #delete that item
        return self.__delitem__(i)
    return "error"

  def clear(self):
    #writing the initial state
    self.n=0
    self.capacity=1

  def find(self,item):
    for i in range(self.n):
      if self.A[i]==item:
        return i

    return "not found"


  def __str__(self):

    result=""
    for i in range(self.n):
      result=result+str(self.A[i])+","

    return "["+result[:-1]+"]"


  def __make_array(self,capacity):
    return (capacity*ctypes.py_object)()

  def __resize(self,capacity):
    #create new array of given size
    B= self.__make_array(capacity)
    self.capacity=capacity

    #copy the element of A into B
    for i in range(self.n):
      B[i]=self.A[i]

    #reasign it to A
    self.A= B 
