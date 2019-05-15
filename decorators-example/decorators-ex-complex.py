import functools
import time
import math


def do_twice(func):
    @functools.wraps(func)
    def wrappers_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        #to return values of decorator
        return func(*args, **kwargs)
    return wrappers_do_twice


# Decorator template
def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        value = func(*args, **kwargs)
        # Do something after
        return value
    return wrapper_decorator


def timer(func):
    """Print the runtime of the decorated functio"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__!r} in {run_time:.4f} sec")
        return value
    return wrapper_timer



@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])

#waste_some_time(1000)


# Decorator template
def debug(func):
    """Print the function signature and return value"""
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        # Do something before
        args_reps = [repr(a) for a in args]
        kwargs_reps = [f"{k}= {v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_reps + kwargs_reps)
        print(f"Calling {func.__name__} ({signature})")
        value = func(*args, **kwargs)
        # Do something after
        print(f"{func.__name__!r} returned {value!r}")
        return value
    return wrapper_debug


@debug
def make_greetings(name, age=None):
    if age is None:
        return f"Howdy {name}!"
    else:
        return f"Whoa {name}! {age} already!"

#make_greetings("J", age=10)

# decorator with only function
math.factorial = debug(math.factorial)

def approximate_e(terms=18):
    return sum(1 / math.factorial(n) for n in range(terms))

# print(approximate_e(5))

# Decorator template
def slow_down(func):
    """Sleep 1 second before calling the function"""
    @functools.wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)
    return wrapper_slow_down


@slow_down
def countdown(from_number):
    if from_number < 1:
        print("Liftoff!")
    else:
        print(from_number)
        countdown(from_number - 1)

# countdown(10)