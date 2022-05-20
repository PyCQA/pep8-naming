#: Okay
class C1:
    def __str__(self):
        return ''
#: Okay
class C2:
    if True:
        def __str__(self):
            return ''
#: N807
if True:
    def __bad__():
        pass
#: Okay
class C3:
    try:
        if True:
            while True:
                def __str__(self):
                    return ''
                break
    except:
        pass
#: Okay
def _bad():
    pass
#: Okay
def __bad():
    pass
#: Okay
def bad_():
    pass
#: Okay
def bad__():
    pass
#: N807
def __bad__():
    pass
#: Okay
class ClassName:
    def method(self):
        def __bad():
            pass
#: N807
class ClassName:
    def method(self):
        def __bad__():
            pass
#: Okay(--ignore-names=__bad)
def __bad():
    pass
#: Okay(--ignore-names=__*)
def __bad():
    pass
#: Okay
def __dir__():
    pass
#: Okay
def __getattr__(name):
    pass

#: Okay
class C:
    def γ(self):
        pass
#: Okay
def __β(self):
    pass
#: Okay
def β__(self):
    pass
#: N807
def __β__(self):
    pass
#: N807
def __β6__(self):
    pass
#: Okay
class C:
    def γ1(self):
        pass

#: Okay
class C:
    async def γ(self):
        pass
#: Okay
async def __β(self):
    pass
#: Okay
async def β__(self):
    pass
#: N807
async def __β__(self):
    pass
