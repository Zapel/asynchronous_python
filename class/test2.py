class MyClass():
    def __init__(self):
        self.variable = "Oleg"
        self.__superprivate = "Hello"
        self._semiprivate = ", world!"



if __name__ == '__main__':
    mc = MyClass()

    # print(mc._superprivate)
    print(mc._semiprivate)
    print(mc.variable)
