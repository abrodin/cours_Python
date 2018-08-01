class A:
    t = 0

    def __init__(self):
        self.colors = ['red', 'green', 'blue']


a = A()
b = A()
a.x = 1
print('a.colors == b.colors', a.colors == b.colors )
print('a.colors is b.colors', a.colors is b.colors )