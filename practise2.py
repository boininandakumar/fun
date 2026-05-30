def repeat(x):
    def dec(func):
        def inner():
            for i in range(x):
                func()
        return inner
    return dec
@repeat(4)
def greet():
    print("Hello")
greet()
