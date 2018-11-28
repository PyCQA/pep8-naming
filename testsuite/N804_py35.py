# python_version >= '3.5'
#: N804:7:19
class Foo(object):
    @classmethod
    async def mmm(cls, ads):
        pass

    @classmethod
    async def bad(self, ads):
        pass

    @calling()
    async def test(self, ads):
        pass

    async def __init_subclass(self, ads):
        pass
#: N804:3:20(--classmethod-decorators=clazzy,cool)
class NewClassIsRequired(object):
    @cool
    async def test(self, sy):
        pass
#: N804
class Meta(type):
    async def __new__(self, name, bases, attrs):
        pass
#: Okay
class MetaMethod(type):
    async def test(cls):
        pass
#: Okay
class NotMeta(object):
    otherclass = Foo
class AttributeParent(NotMeta.otherclass):
    pass
class CallParent(type('_tmp', (), {})):
    pass
