# python3 only
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
