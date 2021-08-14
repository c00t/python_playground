class Foo:
    pass

x = Foo()
print(x.__class__)
print(type(x))
print(x.__class__ is type(x))

# Type of Foo
print(type(Foo))
# Type of `type`
print(type(type))

# Dynamically define a class using `type`
FooDy = type('FooDy', (), {})
x = FooDy()
print(type(x))

Bar = type('Bar', (Foo, ), dict(attr = 100))
y = Bar()
print(type(y))
print(y.attr)

Example3 = type('Example3', (), {
    'attr':100,
    'attr_val':lambda x : x.attr
})
z = Example3()
print(type(z))
print(z.attr)
print(z.attr_val())

def f(obj):
    print('attr = ',obj.attr)
    return obj.attr
Example4 = type('Example4', (), {
    'attr' : 100,
    'attr_val' : f
})
a = Example4()
print(type(a))
print(a.attr)
print(a.attr_val())

def new(cls):
    x = object.__new__(cls)
    x.attr = 100
    return x

Foo.__new__ = new
b = Foo()
print(b.attr)

# define customed metaclass
class NewMetaClass(type):
    def __new__(cls, name, bases, dct):
        x = super().__new__(cls, name, bases, dct)
        x.attr = 100
        return x

class FooWithNewMeta(metaclass=NewMetaClass):
    pass

print(FooWithNewMeta.attr)