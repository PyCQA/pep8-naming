#: Okay
def ok():
    pass
#: Okay
def _ok():
    pass
#: Okay
def ok_ok_ok_ok():
    pass
#: Okay
def _somehow_good():
    pass
#: Okay
def go_od_():
    pass
#: Okay
def _go_od_():
    pass
#: N802:1:5
def NotOK():
    pass
#: Okay(--ignore-names=NotOK)
def NotOK():
    pass
#: Okay(--ignore-names=*OK)
def NotOK():
    pass
#: Okay
def _():
    pass
#: Okay
class Foo:
    def __method(self):
        pass
#: Okay
class Foo:
    def __method__(self):
        pass
#: Okay
class ClassName:
    def __method__(self):
        pass
#: N802
class ClassName:
    def notOk(self):
        pass
#: Okay(--ignore-names=notOk)
class ClassName:
    def notOk(self):
        pass
#: Okay(--ignore-names=*Ok)
class ClassName:
    def notOk(self):
        pass
#: Okay
def setUp():
    pass

#: Okay
def tearDown():
    pass

#: Okay
def setUpModule():
    pass

#: Okay
def tearDownModule():
    pass

#: Okay
class TestCase:
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def setUpClass(self):
        pass
    def tearDownClass(self):
        pass
    def asyncSetUp(self):
        pass
    def asyncTearDown(self):
        pass
    def setUpTestData(self):
        pass

#: Okay
def γ(x):
    pass
#: Okay
def γ6(x):
    pass

#: Okay
async def func(param1, param2):
    do_stuff()
    await some_coroutine()
#: N802
async def Func(param1, param2):
    do_stuff()
    await some_coroutine()
