#: Okay
def ok():
    pass
#: N802
def __bad():
    pass
#: N802
def bad__():
    pass
#: N802
def __bad__():
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
#: N802
def NotOK():
    pass
#: Okay
def _():
    pass
#: Okay
class Foo(object):
    def __method(self):
        pass
#: Okay
class Foo(object):
    def __method__(self):
        pass
#: Okay
class ClassName(object):
    def __method__(self):
        pass
#: N802
class ClassName(object):
    def notOk(self):
        pass
#: N802
class ClassName(object):
    def method(self):
        def __bad():
            pass
