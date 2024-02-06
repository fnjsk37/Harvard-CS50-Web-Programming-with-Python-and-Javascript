<<<<<<< HEAD
# A decorators is a function that takes a function as an input to be modified into something else
def announce(f):
    def wrapper():
        print("About to run the function.")
        f()
        print("Done with the function.")
    return wrapper

@announce
def hello():
    print("Hello, world!")
=======
# A decorators is a function that takes a function as an input to be modified into something else
def announce(f):
    def wrapper():
        print("About to run the function.")
        f()
        print("Done with the function.")
    return wrapper

@announce
def hello():
    print("Hello, world!")
>>>>>>> 311c41f4981f8eae31b7e7dce0bbaa6c0c4caddb
hello()