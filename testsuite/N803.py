#: Okay
def b1():
    pass
#: Okay
def b2(a):
    pass
#: Okay
def b3(a, b, c, d):
    pass
#: Okay
def b4(a, b, c, *fuck):
    pass
#: Okay
def b5(*fuck):
    pass
#: Okay
def b6(a, b, c, **kwargs):
    pass
#: Okay
def b7(**kwargs):
    pass
#: Okay
def b8(*args, **kwargs):
    pass
#: Okay
def b9(a, b, c, *args, **kwargs):
    pass
#: Okay
def b10(a, b, c=3, d=4, *args, **kwargs):
    pass
#: N803
def b11(**BAD):
    pass
#: N803
def b12(*BAD):
    pass
#: N803
def b13(BAD, *VERYBAD, **EXTRABAD):
    pass
#: Okay(--ignore-names=*BAD)
def b13(BAD, *VERYBAD, **EXTRABAD):
    pass
#: N803:1:9
def b14(BAD):
    pass
#: Okay
def b15(_):
    pass
#: Okay
def b16(_a):
    pass
#: Okay
def b17(a, _):
    pass
#: Okay
def b18(a, *_):
    pass
#: Okay
def b19(a, **_):
    pass
#: N803:2:24
class Test(object):
    def __init__(self, BAD):
        pass

    @classmethod
    def test(cls, BAD):
        pass
#: Okay(--ignore-names=I)
def f(I):
    I.think_therefore_i_am
#: Okay(--ignore-names=I)
def f(*I):
    I[0].think_therefore_i_am
#: Okay(--ignore-names=I)
def f(*I):
    I[''].think_therefore_i_am
