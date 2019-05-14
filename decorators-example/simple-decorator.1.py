from datetime import datetime

def not_during_the_nigth(func):
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            func()
        else:
            pass # Hush, the neighbors are asleep

    return wrapper

def say_wop():
    print("wop!")

say_wop = not_during_the_nigth(say_wop)

say_wop()