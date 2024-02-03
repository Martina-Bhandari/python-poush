# name = """Hello World"""

# print(len(name))

# print(name.upper())
# print(name.lower())
# print(name.strip())#agadi ko space hatauxa
# print(name.split())

fruits=[
    'apple',
    'banana',
    'orange',
    'kiwi'
]
vegs=[
    'sag',
    'tomatos'
]
fruits.append("pineapple")
print(fruits)
fruits.extend(vegs)
print(fruits)

fruits.insert(2,'tomatos')
print(fruits)

fruits.remove('apple')
print(fruits)

fruits.pop(1)
print(fruits)

fruits.index('banana')
print(fruits)
fruits.sort()
print(fruits)

fruits.reverse()
print(fruits)

my_dict = {'a': 1, 'b': 2, 'c': 3}
keys = my_dict.keys()
print(keys)

my_dict = {'a': 1, 'b': 2, 'c': 3}
values = my_dict.values()
print(values)







