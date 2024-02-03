# person= {
#     'name': 'Ram',
#     'age' : 20,
#     'percentage' : 9.9,
#     'family_member' : [
#         'mom',
#         'dad',
#         'sister'
#     ],
#     'hobby' : (
#         'Reading',
#         'Watching anime'
#     )
# }
# print (person)
# print(person['family_member'][1][0])
person = {
    'name': 'Ram',
    'age': 20,
    'percentage': 9.9,
    'family_member': [
        'mom',
        'dad',
        'sister'
    ],
    'hobby': (
        'Reading',
        'Watching anime'
    ),
    'Hometown': 'Kusma',
    'occupation': 'Student'
}

print(person)
print("First letter of dad's name:", person['family_member'][1][0])
print("Hometown:", person['Hometown'])
print("Occupation:", person['occupation'])
