#: Okay
class ActionError(Exception):
    pass
#: N818
class ActionClass(Exception):
    pass
#: Okay
class ActionError(Exception):
    pass
class DeepActionError(ActionError):
    pass
#: N818
class ActionError(Exception):
    pass
class DeepActionClass(ActionError):
    pass
#: Okay
class MixinError(Exception):
    pass
class Mixin:
    pass
class MixinActionError(Mixin, MixinError):
    pass
#: N818
class MixinError(Exception):
    pass
class Mixin:
    pass
class MixinActionClass(Mixin, MixinError):
    pass
#: Okay
from decimal import Decimal
class Decimal(Decimal):
    pass
