# python_version < '3'
#: Okay
def f():
    try:
        f()
    except (A, B) as (a, b):
        pass
#: Okay
def f():
    try:
        f()
    except X, foo:
        pass
#: N806
def f():
    try:
        f()
    except (A, B) as (good, BAD):
        pass
#: Okay
def f():
    try:
        f()
    except X, foo.bar:
        pass
#: N806
def f():
    try:
        f()
    except mod.Timeout, mod.ConnectionError:
        pass
