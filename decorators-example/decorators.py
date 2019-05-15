import functools

def do_twice(func):
    @functools.wraps(func)
    def wrappers_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        #to return values of decorator
        return func(*args, **kwargs)
    return wrappers_do_twice

@do_twice
def say_wop():
    print("wopwop")

@do_twice
def greet(name):
    print(f"Hello {name}")

say_wop()
greet("Fermin")

@do_twice
def return_greetings(name):
    print("Creating greeting")
    return f"Hi {name}"

hi_adam = return_greetings("Adam")
print(hi_adam)


