# python_version >= '3.5'
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
