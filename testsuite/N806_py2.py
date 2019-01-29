# python_version < '3'
#: Okay
def f():
    try:
        f()
    except (A, B) as (a, b):
        pass
#: N806
def f():
    try:
        f()
    except (A, B) as (good, BAD):
        pass
