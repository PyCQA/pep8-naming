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
