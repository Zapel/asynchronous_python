class Test:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def first(self, x, y):
        z = x + y
        return z

    def second(self, b, x, y):
        a = self.first(x, y)
        c = a + b
        return c

    def third(self, b):
        a = self.first(self.x, self.y)
        c = a + b
        return c



if __name__ == '__main__':
    test = Test(1, 2)

    x = test.second(4, 3, 2)
    print(x)

    y = test.third(3)
    print(y)



