import functools
import time


def timer(func):
    """print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args,**kwargs):
        start_time = time.perf_counter()
        value = func(*args,**kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs.")
    return wrapper_timer


@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])

# waste_some_time(1)
# waste_some_time(999)

def debug(func):
    """Print the function signature and return value"""
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ",".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__!r}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")
        return value
    return wrapper_debug

@debug
def make_greeting(name, age=None):
    if age is None:
        return f"Howdy {name}!"
    else:
        return f"Whoa {name}! {age} already, you are growing up!"

make_greeting("Benjamin")
make_greeting("Benjamin", age=123)

import math
math.factorial = debug(math.factorial)
def approximate_e(terms=18):
    return sum(1/math.factorial(n) for n in range(terms))

approximate_e(5)

def slow_down(func):
    """Sleep 1 secs before calling the fucntion"""
    @functools.wraps(func)
    def wrapper_slow_down(*args,**kwargs):
        time.sleep(1)
        return func(*args,**kwargs)
    return wrapper_slow_down

@slow_down
def countdown(from_number):
    if from_number < 1 :
        print("LiftOff!")
    else:
        print(from_number)
        countdown(from_number-1)

countdown(3)

import random
PLUGINS = dict()

def register(func):
    PLUGINS[func.__name__] = func
    return func

@register
def say_hello(name):
    return f"Hello {name}"

@register
def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"

def random_greet(name):
    greeter, greeter_func = random.choice(list(PLUGINS.items()))
    print(f"Using {greeter!r}")
    return greeter_func(name)

print(random_greet("LiMei"))
print(random_greet("SunLeiLei"))


class TimeWaster:
    @debug
    def __init__(self,max_num):
        self.max_num = max_num

    @timer
    def waste_time(self,num_times):
        for _ in range(num_times):
            sum([i**2 for i in range(self.max_num)])

tw = TimeWaster(1000)
tw.waste_time(999)