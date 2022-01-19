# python_version >= '3.8'
#: Okay
class MyDict(TypedDict):
    mixedCase: str
class MyOtherDict(MyDict):
    more_Mixed_Case: str
#: N815
class TypedDict:
    mixedCase: str
#: N815
class TypedDict:
    more_Mixed_Case: str
