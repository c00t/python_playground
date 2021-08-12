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