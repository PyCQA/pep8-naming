from abc import ABCMeta

#: N804:7:13
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
#: Okay(--ignore-names=klass)
class SpecialConventionCase(object):
    @classmethod
    def prepare_meta(klass, root):
        pass
#: Okay(--ignore-names=_*)
class SpecialConventionCase(object):
    @classmethod
    def prepare_meta(_class, root):
        pass
#: N804:3:14(--classmethod-decorators=clazzy,cool)
class NewClassIsRequired(object):
    @cool
    def test(self, sy):
        pass
#: N804
class Meta(type):
    def __new__(self, name, bases, attrs):
        pass
#: Okay
class MetaMethod(type):
    def test(cls):
        pass
class MetaMethod(ABCMeta):
    def test(cls):
        pass
#: Okay
class NotMeta(object):
    otherclass = Foo
class AttributeParent(NotMeta.otherclass):
    pass
class CallParent(type('_tmp', (), {})):
    pass
