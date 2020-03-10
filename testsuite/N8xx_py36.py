# python_version >= '3.6'
#: Okay
var1: int = 1
var2: int
def some():
    variable: int = 1
class Test(object):
    variable: int = 1
#: N816:1:1
mixedCase: int = 1
#: N806:2:5
def some():
    mixedCase: int = 1
#: N815:2:5
class Test(object):
    mixedCase: int = 1
