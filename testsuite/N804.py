from abc import ABCMeta

#: N804:7:13
class Foo:
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
class SpecialConventionCase:
    @classmethod
    def prepare_meta(klass, root):
        pass
#: Okay(--ignore-names=_*)
class SpecialConventionCase:
    @classmethod
    def prepare_meta(_class, root):
        pass
#: N804:3:14(--classmethod-decorators=clazzy,cool)
class NewClassIsRequired:
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
class NotMeta:
    otherclass = Foo
class AttributeParent(NotMeta.otherclass):
    pass
class CallParent(type('_tmp', (), {})):
    pass

#: N804:7:19
class Foo:
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
class NewClassIsRequired:
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
class NotMeta:
    otherclass = Foo
class AttributeParent(NotMeta.otherclass):
    pass
class CallParent(type('_tmp', (), {})):
    pass
