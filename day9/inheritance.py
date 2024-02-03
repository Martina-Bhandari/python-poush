class Human:
    age=0

class GrandFather(Human):
    def __init__ (self):
       print('I am mother')
       self.house = 13
       print(f'I have {self.house}')
    
class Mother(GrandFather):
    age=22
    def __init__ (self):
       print('I am Mother')
    jewlary="gold"
    
class Father(GrandFather):
    age=22
    def __init__ (self):
        super().__init__()
        self.house=10
        print(f"I have {self.house}")
    car = "lambo"
    
    def __eq__(self,object):
      return self.age==object.age

class Son(Father,Mother) :
    
    gaming_console="PSS"   
    
binit = Father()
binita = Mother()
print(binit==(binita))
# print(binit.gaming_console)
# print(binit.house)
# print(binit.car)
# print(binit.jewlary)

