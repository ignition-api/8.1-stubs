from typing import Any, Optional

from java.lang import Object, String
from java.util import EventObject

class AWTEvent(EventObject):
    def __init__(self, source: Object, id: int) -> None: ...
    def getID(self) -> int: ...
    def paramString(self) -> String: ...
    def setSource(self, newSource: Object) -> None: ...

class Color(Object):
    def __init__(self, *args: Any) -> None: ...

class Component(Object):
    def imageUpdate(
        self, img: Image, infoflags: int, x: int, y: int, width: int, height: int
    ) -> bool: ...

class Container(Component):
    def add(self, *args: Any) -> Optional[Component]: ...

class Image(Object):
    def flush(self) -> None: ...
    def getAccelerationPriority(self) -> float: ...
    def setAccelerationPriority(self, priority: float) -> None: ...

class Toolkit(Object):
    def __init__(self) -> None: ...
    def beep(self) -> None: ...
    @staticmethod
    def getDefaultToolkit() -> Toolkit: ...

class Window(Container):
    def __init__(self, *args: Any) -> None: ...

class Frame(Window):
    def __init__(self, *args: Any) -> None: ...

class Graphics(Object):
    def create(self) -> Graphics: ...
