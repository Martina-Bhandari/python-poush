# def star(function):
#     def wrapper():
#         print('*'*10)
#         function()
#         print('*'*10)
#     return wrapper
    
# @star
# def hello():
#         print("hello")
# hello()

# def hash(function):
#     def wrapper():
#         print('#'*10)
#         function()
#         print('#'*10)
#     return wrapper
    
# @star
# def hello():
#         print("hello")
# hello()


# def star(function):
#     def wrapper():
#         print('*'*10)
#         function()
#         print('*'*10)
#     return wrapper
    

# def hello():
#         print("hello")
# star(hello)()
def star(function):
    def wrapper():
        print('*'*10)
        function()
        print('*'*10)
    return wrapper
    
def hash(function):
    def wrapper():
        print('#'*10)
        function()
        print('#'*10)
    return wrapper






        