# Python Decorator
import time

# returns a new function that delays the passed in function by 2 seconds before calling it


def delay_decorator(func):
    def wrapper_func():
        time.sleep(2)
        func()
    return wrapper_func

@delay_decorator
def say_hello():
    # time.sleep(2)
    print("Hello!")

@delay_decorator
def say_bye():
    print("Bye")

@delay_decorator
def say_greeting():
    print("How are you?")


# Test it by only uncommenting one of the select delayed functions
# delayed_func = delay_decorator(say_hello)
# delayed_func = delay_decorator(say_bye)
# delayed_func = delay_decorator(say_greeting)
# delayed_func()

say_hello()
say_bye()
say_greeting()