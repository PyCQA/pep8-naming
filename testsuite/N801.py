#: N801
class notok:
    pass
#: Okay(--ignore-names=notok)
class notok:
    pass
#: Okay(--ignore-names=*ok)
class notok:
    pass
#: N801
class Good:
    class notok:
        pass
    pass
#: Okay
class VeryGood:
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
#: Okay
class Γ:
    pass
#: Okay
class ΓγΓγ:
    pass
#: Okay
class ΓγΓ6:
    pass
#: Okay
class _Γ:
    pass
#: N801:1:7
class γ:
    pass
#: N801
class _γ:
    pass
