#: Okay
def test():
    good = 1
#: Okay
def test():
    def test2():
        good = 1
#: Okay
GOOD = 1
#: Okay
class Test(object):
    GOOD = 1
#: N806
def test():
    Bad = 1
#: N806
def test():
    VERY = 2
#: N806
def test():
    def test2():
        class Foo(object):
            def test3(self):
                Bad = 3
#: Okay
def good():
    global Bad
    Bad = 1
#: N806
def bad():
    global Bad

    def foo():
        Bad = 1

#: Okay
def test():
    # namedtuples are often CamelCased since we treat them a bit like classes
    import collections
    Thing = collections.namedtuple('Thing', 'a b c')
    from collections import namedtuple
    ThingTwo = namedtuple('ThingTwo', 'a b c')

#: N806
def bad():
    # Currently don't support aliased imports of namedtuple
    from collections import namedtuple as nt
    Thing = nt('Thing', 'a b c')
