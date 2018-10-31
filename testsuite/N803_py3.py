# python_version >= '3'
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
