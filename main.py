#Section1: DECORATORS

print("="*60)
print("Section 1:DECORATOR")
print("="*60)


def my_decorator(func):
    def wrapper():
        print("wrapper function executed")
        func()
        print("wrapper function executed")

    return wrapper

@my_decorator
def hello_world():
    print("hello world")
hello_world()
