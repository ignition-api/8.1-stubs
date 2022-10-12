from typing import Union

from com.inductiveautomation.ignition.common import Path as Path
from com.inductiveautomation.ignition.common.config import Property as Property
from java.lang import String as String

class TagPath(Path):
    def compareTo(self, o: TagPath) -> int: ...
    def getChildPath(self, arg: Union[Property, String]) -> TagPath: ...
    def getItemName(self) -> String: ...
    def getLastPathComponent(self) -> str: ...
    def getParentPath(self) -> Path: ...
    def getPathComponent(self, i: int) -> String: ...
    def getPathLength(self) -> int: ...
    def getProperty(self) -> Property: ...
    def getSource(self) -> String: ...
    def isAncestorOf(self, path: Path) -> bool: ...
    def toStringFull(self) -> String: ...
    def toStringPartial(self) -> String: ...
