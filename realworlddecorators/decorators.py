import functools
import time

def timer(f):
    @functools.wraps()
    def wrapper(*args,**kwargs):
        start_time = time.perf_counter()
        value = f(*args,**kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"the function: {f.__name__!r} executed in : {run_time} ")
        return value
    return wrapper






