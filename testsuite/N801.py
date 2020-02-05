#: N801
class notok(object):
    pass
#: Okay(--ignore-names=notok)
class notok(object):
    pass
#: Okay(--ignore-names=*ok)
class notok(object):
    pass
#: N801
class Good(object):
    class notok(object):
        pass
    pass
#: Okay
class VeryGood(object):
    pass
#: N801:1:7
class _:
    pass
#: N801:1:7
class BAD_NAME:
    pass
#: Okay
class Fine_:
    pass
#: Okay
class Fine__:
    pass
#: Okay
class G_:
    pass
#: N801:1:7
class Not_Good:
    pass
#: Okay
class __Fine:
    pass
# The following cases are currently OK, but perhaps could be errors.
#: Okay
class MEHHHH:
    pass
#: Okay
class __Meh__:
    pass
#: Okay
class __MEH:
    pass
#: Okay
class MEH__:
    pass
#: Okay
class __MEH__:
    pass
