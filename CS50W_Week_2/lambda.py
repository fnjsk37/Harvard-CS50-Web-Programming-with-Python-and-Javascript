<<<<<<< HEAD
people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]

def f(person):
    return person["name"]

# Alternatively you can use a one liner with lamda
people.sort(key=lambda person: person["house"])

people.sort(key=f)
=======
people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]

def f(person):
    return person["name"]

# Alternatively you can use a one liner with lamda
people.sort(key=lambda person: person["house"])

people.sort(key=f)
>>>>>>> 311c41f4981f8eae31b7e7dce0bbaa6c0c4caddb
print(people)