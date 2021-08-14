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

# countdown(3)

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


def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                func(*args, **kwargs)
        return wrapper_repeat
    return decorator_repeat


@repeat(num_times = 4)
def greeting():
    print("hello from greeting.")


greeting()

def repeat_wo(_func = None, *, num_times = 2):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                func(*args, **kwargs)
        return wrapper_repeat
    if _func is None:
        return decorator_repeat
    else:
        return decorator_repeat(_func)


@repeat_wo
def greeting_name1():
    print("Hello 1.")


@repeat_wo(num_times = 4)
def greeting_name2():
    print("Hello 2.")


greeting_name1()
greeting_name2()

# use decorator to keep track of state (function attributes)
def count_calls(func):
    @functools.wraps(func)
    def wrapper_count_calls(*args,**kwargs):
        wrapper_count_calls.num_calls += 1
        print(f"Call {wrapper_count_calls.num_calls} of {func.__name__!r}")
        return func(*args,**kwargs)
    wrapper_count_calls.num_calls = 0
    return wrapper_count_calls

@repeat(num_times=2)
@count_calls
def say_count_calls():
    print("sayyy!")


say_count_calls()
# say_count_calls.num_calls = 2

# use class decorator to implement above example
class Counter:
    def __init__(self, func):
        # 这一行，注意
        functools.update_wrapper(self, func)
        #
        self.func = func
        self.count = 0

    def __call__(self,*args, **kwargs):
        self.count += 1
        print(f"Call {self.count} of {self.func.__name__!r}")
        self.func(*args, **kwargs)

@Counter
def say_count_calls_class():
    print("Sayyyy!")

say_count_calls_class()
say_count_calls_class()

# @slow_down with `rate` args
def slow_down_args(_func = None, *, rate = 1):
    def decorator_slow_down(func):
        @functools.wraps(func)
        def wrapper_slow_down(*args,**kwargs):
            time.sleep(rate)
            return func(*args,**kwargs)
        return  wrapper_slow_down
    if _func is None:
        return decorator_slow_down
    else:
        return decorator_slow_down(_func)


@slow_down_args
def count_down_2(from_number):
    if from_number < 1:
        print("LiftOff!")
    else:
        print(f"Counting {from_number}")
        count_down_2(from_number-1)

count_down_2(3)

# singleton decorator implemntation
def singleton(cls):
    """Make a class a singleton class (only one instance)"""
    @functools.wraps(cls)
    def wrapper_singleton(*args, **kwargs):
        if not wrapper_singleton.instance:
            wrapper_singleton.instance = cls(*args, **kwargs)
        return wrapper_singleton.instance
    wrapper_singleton.instance = None
    return wrapper_singleton

@singleton
class TheOne:
    pass

first_one = TheOne()
second_one = TheOne()

print(f"id of first_one is {id(first_one)},\nid of second_one is {id(second_one)}")

# cache return values
def cache(func):
    """Keep a cache of previous function call"""
    @functools.wraps(func)
    def wrapper_cache(*args, **kwargs):
        cache_key = args + tuple(kwargs.items())
        # cache_key here is a `tuple`,eg. (5,). because args is a tuple
        # print(cache_key)
        if cache_key not in wrapper_cache.cache:
            wrapper_cache.cache[cache_key] = func(*args, **kwargs)
        return wrapper_cache.cache[cache_key]
    wrapper_cache.cache = dict()
    return wrapper_cache

@cache
@count_calls
def fibonacci(num):
    if num < 2:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)

fibonacci(10)
