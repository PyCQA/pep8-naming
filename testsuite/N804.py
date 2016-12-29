#: N804
class Foo(object):
    @classmethod
    def mmm(cls, ads):
        pass

    @classmethod
    def bad(self, ads):
        pass

    @calling()
    def test(self, ads):
        pass

    def __init_subclass(self, ads):
        pass
#: N804(--classmethod-decorators=clazzy,cool)
class NewClassIsRequired(object):
    @cool
    def test(self, sy):
        pass
