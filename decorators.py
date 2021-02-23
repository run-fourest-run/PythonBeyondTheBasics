import functools

def do_two_times(f):
    def wrapper_do_twice(*args,**kwargs):
        f(*args,**kwargs)
        return f(*args,**kwargs)
    return wrapper_do_twice




def do_ten_times(f):
    @functools.wrap(f)
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
