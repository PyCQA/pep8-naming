# python_version >= '3.5'
#: Okay
class C:
    async def __init__(*args, **kwargs):
        pass
#: N805:4:17
class C:
    @decorator(
        'a')
    async def m(cls, k='w'):  # noqa: N805
        pass
#: N805(--staticmethod-decorators=exstatik,stcmthd)
class ButWeLostTheOriginalStaticMethodLateDecorator(object):
    async def test(so, exciting):
        pass
    test = staticmethod(test)
