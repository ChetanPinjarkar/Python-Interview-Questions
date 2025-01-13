def simple_decorator(func):
    def wrapper():
        print("Before funcation call")
        func()
        print("After function call")
    return wrapper

@simple_decorator
def say_hello():
    print("Hello")

say_hello()
