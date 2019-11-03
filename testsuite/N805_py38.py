# python_version >= '3.8'
#: Okay
class C:
    def __init__(self, a, /, b=None):
        pass
#: N805:2:18
class C:
    def __init__(this, a, /, b=None):
        pass
