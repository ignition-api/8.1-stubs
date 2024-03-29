from typing import Any

from dev.coatl.helper.types import AnyStr
from java.lang import Object

class Aggregate:
    def getDesc(self) -> AnyStr: ...
    def getId(self) -> int: ...
    def getName(self) -> AnyStr: ...

class AggregateInfo(Object, Aggregate):
    def __init__(self, *args: Any) -> None: ...
    def getDesc(self) -> AnyStr: ...
    def getId(self) -> int: ...
    def getName(self) -> AnyStr: ...
