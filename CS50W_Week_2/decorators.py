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
hello()