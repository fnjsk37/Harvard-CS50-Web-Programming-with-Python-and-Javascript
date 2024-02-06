# Classes are templates for a type of object
# After creating a class you can use it to create other objects
class Point():
    # def __init__ makes every new instance of a class initialized
    def __init__(self, input1, input2): # A point needs two values for each coordinate
        self.x = input1
        self.y = input2

p = Point(2, 8)
print(p.x)
print(p.y)