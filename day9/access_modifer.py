class Person:
    def __init__(self,name,age,password):
        self.name = name
        self.age = age
        self.__password = password  #(__) private store data
    @property
    def password(self):
        return self.__password
        
    @password.setter
    def password(self,password) :
       self.__password = password     
    
     
    # def set_password(self,password) :
    #     self.__password = password
        
    # password=property(get_password,set_password)
        
binit=Person("binit",23,"binita@123")
# binit.name= "test"
print(binit.name)
print(binit.age)
# binit.password="martina@123"
print(binit.password)


