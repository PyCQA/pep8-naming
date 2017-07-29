#: N805
class Foo(object):
    def good(self, ads):
        pass

    def bad(ads, self):
        pass
#: Okay
class Foo(object):
    def __new__(cls):
        return object.__new__(Foo)
#: Okay
class Foo(object):
    @classmethod
    def __prepare__(cls):
        pass

#: Okay
class Foo(object):
    def __init_subclass__(cls):
        pass
