# python_version >= '3.5'
#: Okay
async def compare(a, b, *, key=None):
    pass
#: N803
async def compare(a, b, *, BAD=None):
    pass
