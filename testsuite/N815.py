#: Okay
class C:
    a = 0
#: Okay
class C:
    lowercase = 0
#: Okay
class C:
    v1 = 0
#: Okay
class C:
    _1 = 0
#: Okay
class C:
    maxDiff = None
#: N815:2:5
class C:
    mixedCase = 0
#: N815
class C:
    mixed_Case = 0
#: Okay(--ignore-names=mixed_Case)
class C:
    mixed_Case = 0
#: Okay(--ignore-names=*Case)
class C:
    mixed_Case = 0
#: N815(--ignore-names=*case)
class C:
    mixed_Case = 0

#: Okay
class C:
    a = (someVar1 == 8 for someVar1 in [])
    b = [someVar2 == 8 for someVar2 in []]
    c = {someVar3 == 8 for someVar3 in []}
    d = {someVar4: 8 for someVar4 in []}
