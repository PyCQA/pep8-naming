#: Okay
GLOBAL_UPPER_CASE = 0
#: N816
mixedCase = 0
#: N816:1:1
mixed_Case = 0
#: Okay
_C = 0
#: Okay
__D = 0
#: N816
__mC = 0
#: N816
__mC__ = 0
#: Okay
__C6__ = 0
#: Okay
C6 = 0
#: Okay
C_6 = 0.
#: Okay(--ignore-names=mixedCase)
mixedCase = 0
#: Okay(--ignore-names=*Case)
mixedCase = 0
#: Okay
Γ = 1
#: N816
γΓ = 1
#: Okay
Γ1 = 1
#: Okay
Γ_ = 1
#: Okay
Γ_1 = 1
#: Okay
Γ1_ = 1
#: N816
γΓ1 = 1
#: N816
_γ1Γ = 1

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
