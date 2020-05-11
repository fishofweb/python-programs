def class_ (x):
    class Dog:
        def __init__(self, name):
            self.name = name

        def print_value(self):
            print(x)

    return Dog

cls_returned = class_(0)
d = cls_returned("tim")
print(d.name)

d.print_value()