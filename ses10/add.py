# timer.py
import time

# decorator
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = (time.time()) - start
        print(f'Time elapsed: {end}')

    return wrapper 


@timer
def add(x):
    l = []
    for i in range(x):
        l.append(i)
    return l




# Generator function
@timer
def gen_add(x):
    for i in range(x):
        yield i
