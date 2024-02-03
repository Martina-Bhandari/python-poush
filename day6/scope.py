# a=10
# def hello():
#     global a
#     a=11
#     print(a)
# print(a)
# hello()

a=10
b=20
def Martina():
    global a
    a=11
    b=12
    print(a)
    print(b)
    
print(a)
print(b)
Martina()

a=15
def outer():
    a=12
    print('outer function sees a as',a)
    
    def inner():
        a=10
        print('inner function sees a as',a)
    inner() 
outer() 
   