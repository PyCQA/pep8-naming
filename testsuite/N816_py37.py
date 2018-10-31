# python_version >= '3.7'
#: Okay
async with expr as Γ:
    pass
#: N816
async with expr as γΓ:
    pass
#: Okay
async for Γ1 in iterator:
    pass
#: N816
async for γΓ1 in iterator:
    pass
