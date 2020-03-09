# python_version >= '3.8'
#: Okay
def f1(values):
    total = 0
    partial_sums = [total := total + v for v in values]
    return partial_sums, total
#: Okay
GLOBAL_VAR = 0
def f2(values):
    global GLOBAL_VAR
    partial_sums = [GLOBAL_VAR := GLOBAL_VAR + v for v in values]
    return partial_sums, GLOBAL_VAR
#: N806:2:16
def f():
    return 1, (BaD_WalRuS := 1), BaD_WalRuS + 1
#: Okay
def f():
    (NamedTuple := namedtuple('NamedTuple', 'f1 f2'))
    return NamedTuple
