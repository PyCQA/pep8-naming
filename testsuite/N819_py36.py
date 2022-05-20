# python_version >= '3.6'
#: Okay
class MyDict(TypedDict):
    snake_case: str
#: N819
class MyDict(TypedDict):
    mixedCase: str
#: N819
class MyDict(TypedDict):
    snake_case: str
class MyOtherDict(MyDict):
    more_Mixed_Case: str
#: Okay(--ignore-names=mixedCase)
class MyDict(TypedDict):
    mixedCase: str
#: Okay(--ignore-names=*Case)
class MyDict(TypedDict):
    mixedCase: str
