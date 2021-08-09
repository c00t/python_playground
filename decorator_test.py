def do_twice(func):
    def wrapper():
        func()
        func()
    return wrapper


@do_twice
def print_wee():
    print('wee')


print_wee()


def do_twice_args(func):
    def wrapper(*args,**kwargs):
        func(*args,**kwargs)
        func(*args,**kwargs)
    return wrapper


@do_twice_args
def print_wee_with_args(ss):
    print('Wee',ss)


print_wee_with_args('123')


def do_twice_args_rets(func):
    def wrapper(*args,**kwargs):
        func(*args,**kwargs)
        return func(*args,**kwargs)
    return wrapper


@do_twice_args_rets
def print_name(name):
    print('Wee',name)
    return f'Hi {name}'


hi_name = print_name('456')
print(hi_name)