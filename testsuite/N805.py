import abc
from abc import ABCMeta

#: Okay
class C:
    def __init__(*args, **kwargs):
        pass
#: N805:4:11
class C:
    @decorator(
        'a')
    def m(cls, k='w'):  # noqa: N805
        pass
#: N805
class Foo(object):
    def good(self, ads):
        pass

    def bad(ads, self):
        pass
#: Okay(--ignore-names=a*)
class Foo(object):
    def bad(ads, self):
        pass
#: Okay(--ignore-names=source)
class GraphQLNode(object):
    def resolve_foo(source, info):
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

    @staticmethod
    def test(so, exciting):
        pass

    def test1(cls):
        pass
    test1 = classmethod(test1)

    def test2(so, exciting):
        pass
    test2 = staticmethod(test2)
#: Okay
class Foo(object):
    def __new__(cls):
        pass
#: Okay
class Foo(object):
    def __init_subclass__(cls):
        pass
#: Okay
class Foo(object):
    def __class_getitem__(cls, key):
        pass
#: Okay
class Meta(type):
    def __new__(cls, name, bases, attrs):
        pass
    def test(cls):
        pass
#: Okay
class Meta(ABCMeta):
    def __new__(cls, name, bases, attrs):
        pass
    def test(cls):
        pass
#: Okay
class Meta(abc.ABCMeta):
    def __new__(cls, name, bases, attrs):
        pass
    def test(cls):
        pass
#: Okay(--classmethod-decorators=clazzy,cool)
class NewClassmethodDecorators(object):
    @clazzy
    def test1(cls, sy):
        pass

    @cool
    def test2(cls, sy):
        pass

    def test3(cls, sy):
        pass
    test3 = clazzy(test3)

    def test4(cls, sy):
        pass
    test4 = cool(test4)
#: N805(--classmethod-decorators=clazzy,cool)
class ButWeLostTheOriginalClassMethodDecorator(object):
    @classmethod
    def test(cls, sy):
        pass
#: N805(--classmethod-decorators=clazzy,cool)
class ButWeLostTheOriginalClassMethodLateDecorator(object):
    def test(cls, sy):
        pass
    test = classmethod(test)
#: Okay(--classmethod-decorators=myclassmethod)
class C(object):
    @myclassmethod('foo')
    def bar(cls):
        return 42
#: Okay
class PropertySetter(object):
    @property
    def var(self):
        return True
    @var.setter
    def var(self, value):
        self.var = value
#: Okay
class CalledInstanceDecorator(object):
    @module.inner.decorator()
    def test(self):
        pass
#: Okay(--classmethod-decorators=decorator)
class CalledClassDecorator(object):
    @module.inner.decorator()
    def test(cls):
        pass
#: Okay(--staticmethod-decorators=decorator)
class CalledStaticDecorator(object):
    @module.inner.decorator()
    def test():
        pass
#: Okay(--staticmethod-decorators=ecstatik,stcmthd)
class NewStaticMethodDecorators(object):
    @ecstatik
    def test1(so, exciting):
        pass

    @stcmthd
    def test2(so, exciting):
        pass

    def test3(so, exciting):
        pass
    test3 = ecstatik(test3)

    def test4(so, exciting):
        pass
    test4 = stcmthd(test4)
#: N805(--staticmethod-decorators=exstatik,stcmthd)
class ButWeLostTheOriginalStaticMethodDecorator(object):
    @staticmethod
    def test(so, exciting):
        pass
#: N805(--staticmethod-decorators=exstatik,stcmthd)
class ButWeLostTheOriginalStaticMethodLateDecorator(object):
    def test(so, exciting):
        pass
    test = staticmethod(test)
