class MyClass:
    """A simple example Class"""
    i = 1234

    def f(self):
        return 'Hello World'
    
    def __init__(self):
        self.data = []
        print(self.data)


x = MyClass()

print(x.data)

class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(3.0, -4.5)

print(x.r, x.i)