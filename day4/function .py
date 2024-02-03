# def person(f_name,m_name,l_name,num=1):
#    print(f"hello{f_name}{m_name}{l_name}\n"*num)
# person (f_name="Ram", m_name="Raj" ,l_name="Kc", num=3)

# def person(*args):
#     print(args[0], args[1], args[-1])
# person("name", "age", 12, 123, 1234, 1267, "test")

# def sum (*numbers):
#     total=0
#     for number in numbers:
#      total= total+ number
#     print(total)
# sum(1,2)
# def hello():
#    print('Ram , shyam')
# hello()
def hello(first_Person,second_person, Third_person, fourth_person):
    print(f'hello,{first_Person}')
    print(f'hello,{second_person}')
    print(f'hello,{Third_person}')
    print(f'hello,{fourth_person}')
hello('Anisha','Nikita','Rebika','Ruksana')

#keyword argument
def person(f_name,m_name,l_name,age,country,hobbies):
    print(f'hello,{f_name},{m_name},{l_name},{age},{country},{hobbies}')
person('Anisha','Bhandari','Chhetri',22,'Nepal','Reading')

#multiplication of 2
def generate_Multiplication_table(number,range_limit):
        for i in range(1, range_limit + 1):
         result = number * i
         print(f"{number} * {i} = {result}")
user= input("Enter the range for the multiplication table: ")
range_limit = int(user)
generate_Multiplication_table(2, range_limit)

#calculator 
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
     return x / y
def power(x, y):
    return x**y

def calculator():
    print("Simple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exponentiate")



    choice = input("Enter choice (1/2/3/4/5): ")

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if choice == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif choice == '4':
        print(f"{num1} / {num2} = {divide(num1, num2)}")
    elif choice == '5':
        print(f"{num1} ** {num2} = {power(num1, num2)}")
        
    else:
        print("Invalid input. Please enter a valid choice.")

calculator()






    


    


    