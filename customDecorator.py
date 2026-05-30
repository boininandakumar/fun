import functools
import time
def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        print("started: ", start)
        print(f"sum : {func(*args, **kwargs)}")
        end = time.time()
        print(f"End : {end}")
        print("Time taken : ", end - start)
    return wrapper
@timer
def add(x,y):
    """ This is a Doc String"""
    su = 0
    for i in range(1, x + y + 1):
        su += i
    return su

add(10000,2000)