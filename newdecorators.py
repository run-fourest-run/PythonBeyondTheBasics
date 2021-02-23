import functools


def do_ten_times(f):

    def wrapper(*args,**kwargs):
        f(*args)
        f(*args)
        f(*args)
        f(*args)
        f(*args)
        f(*args)
        f(*args)
        f(*args)
        f(*args)
        f(*args)
    return wrapper


@do_ten_times
def print_joe():
    print('joe')

'''

@do_two_times
def return_greeting(name):
    print("Creating Greeting")
    return f"Hi {name}"
'''




