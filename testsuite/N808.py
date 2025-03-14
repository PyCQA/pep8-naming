from typing import TypeVar

#: Okay
Ok = TypeVar("Ok")

#: N808
notok = TypeVar("notok")

#: N808
notok_co = TypeVar("notok_co")

#: Okay(--ignore-names=notok)
notok = TypeVar("notok")

#: N808:1:1(--ignore-names=*OK)
notok = TypeVar("notok")

#: Okay
Ok_co = TypeVar("Ok_co", covariant=True)

#: Okay
Ok_contra = TypeVar("Ok_contra", contravariant=True)

#: N808
Ok__contra = TypeVar("Ok__contra", contravariant=True)

#: N808
Var_contra = TypeVar("Var_contra", covariant=True)

#: N808
Var_co = TypeVar("Var_co", contravariant=True)

#: N808
Var = TypeVar("Var", covariant=True)

#: Okay
Ok_co = TypeVar("Ok_co")

#: Okay
Ok_contra = TypeVar("Ok_contra")

#: Okay
Good = TypeVar("Good")

#: N808
__NotGood = TypeVar("__NotGood")

#: N808
__NotGood__ = TypeVar("__NotGood__")

#: N808
NotGood__ = TypeVar("NotGood__")

#: Okay
A = TypeVar("A")

#: Okay
A_contra = TypeVar("A_contra")

#: N808
A = TypeVar("B")

#: N808
A_contra = TypeVar("B")

#: N808
A_contra = TypeVar("B_contra")

#: N808
A_contra = TypeVar("A_Contra")

#: N808
A_contra = TypeVar()


# Make sure other function calls do not get checked
#: Okay
t = str('something')
t = TypeVar

