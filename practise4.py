import functools
def Dec(func):
    @functools.wraps(func)
    def Inner():
        fun()
    return Inner
@Dec
def fun():
    """ This is Docstring"""
    print("Hello")
print(fun. __doc__)
print(fun. __name__)