# You can import functions that you have created as modules in other python files
from functions import square
for i in range(10):
    print(f"The square of {i} is {square(i)}.")