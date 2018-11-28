# python_version >= '3.5'
#: Okay
async def func(param1, param2):
    do_stuff()
    await some_coroutine()
#: N802
async def Func(param1, param2):
    do_stuff()
    await some_coroutine()
