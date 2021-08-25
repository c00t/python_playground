class WithoutParent():
    def call_super(self):
        return super().super_method()


x = WithoutParent()

print(type(x))

x.call_super()