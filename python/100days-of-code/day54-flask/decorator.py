import time
def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        function()
        print("I'm inside running the function one more time")
        time.sleep(2)
        function()
    return wrapper_function

@delay_decorator
def say_hello():
    print("hello")

@delay_decorator
def say_bye():
    print("bye")

def say_greeting():
    print("How are you?")

say_hello()
say_bye()
say_greeting()
