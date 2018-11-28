# python_version >= '3'
#: Okay
VAR1, *VAR2, VAR3 = 1, 2, 3
#: Okay
Α, *Β, Γ = 1, 2, 3
#: Okay
[VAR1, *VAR2, VAR3] = (1, 2, 3)
#: N806
def extended_unpacking_not_ok():
    Var1, *Var2, Var3 = 1, 2, 3
#: N806
def extended_unpacking_not_ok():
    [Var1, *Var2, Var3] = (1, 2, 3)
#: Okay
def assing_to_unpack_ok():
    a, *[b] = 1, 2
#: N806
def assing_to_unpack_not_ok():
    a, *[bB] = 1, 2
#: Okay
Γ = 1
#: N806
def f():
    Δ = 1
#: N806
def f():
    _Δ = 1
#: Okay
def f():
    γ = 1
#: Okay
def f():
    _γ = 1
#: Okay
def f():
    h, _, γ = s.partition('sep')
