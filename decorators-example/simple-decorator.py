def my_decorator(func):
    def wrapper():
        print("init")
        func()
        print("end")

    return wrapper

def say_wop():
    print("wop wop!")

say_wop = my_decorator(say_wop)

say_wop()