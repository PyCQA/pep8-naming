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
class Test:
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

#: Okay
def compare(a, b, *, key=None):
    pass
#: N803
def compare(a, b, *, BAD=None):
    pass
#: N803
def compare(a, b, *VERY, bad=None):
    pass
#: N803
def compare(a, b, *ok, fine=None, **BAD):
    pass
#: Okay
def foo(α, ß, γ):
    pass
#: Okay
def foo(α, ß=''):
    pass
#: Okay
def foo(**κ):
    pass
#: Okay
def foo(*α):
    pass
#: Okay
def foo(**κ2):
    pass
#: Okay
def foo(*α2):
    pass

#: Okay
async def compare(a, b, *, key=None):
    pass
#: N803
async def compare(a, b, *, BAD=None):
    pass
