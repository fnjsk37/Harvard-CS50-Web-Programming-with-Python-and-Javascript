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
print(people)