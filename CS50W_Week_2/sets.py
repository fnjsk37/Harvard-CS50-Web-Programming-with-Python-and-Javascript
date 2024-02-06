# Create an empty set sequence for unique values
s = set()

# Add elements to set
s.add(1)
s.add(2)
s.add(3)
s.add(4)

# Adding the same value again does not print out
s.add(1)
# You can also remove a value
s.remove(1)
print(s)

# The len function tells you how many values are in the set
print(f"The set has {len(s)} elements.")