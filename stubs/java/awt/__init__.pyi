from typing import Any, Optional

from dev.coatl.helper.types import AnyStr
from java.awt.geom import Dimension2D, Point2D
from java.lang import Object
from java.util import EventObject

class LayoutManager:
    def addLayoutComponent(self, name: AnyStr, comp: Component) -> None: ...
    def layoutContainer(self, parent: Container) -> None: ...
    def minimumLayoutSize(self, parent: Container) -> Dimension: ...
    def preferredLayoutSize(self, parent: Container) -> Dimension: ...
    def removeLayoutComponent(self, comp: Component) -> None: ...

class AWTEvent(EventObject):
    def __init__(self, source: Object, id: int) -> None: ...
    def getID(self) -> int: ...
    def paramString(self) -> AnyStr: ...
    def setSource(self, newSource: Object) -> None: ...

class Color(Object):
    def __init__(self, *args: Any) -> None: ...

class Component(Object):
    def imageUpdate(
        self, img: Image, infoflags: int, x: int, y: int, width: int, height: int
    ) -> bool: ...

class Container(Component):
    def add(self, *args: Any) -> Optional[Component]: ...

class Dimension(Dimension2D):
    height: int
    width: int
    def __init__(self, *args: Any) -> None: ...
    def getHeight(self) -> float: ...
    def getSize(self) -> Dimension: ...
    def getWidth(self) -> float: ...
    def setSize(self, *args: Any) -> None: ...

class Image(Object):
    def flush(self) -> None: ...
    def getAccelerationPriority(self) -> float: ...
    def setAccelerationPriority(self, priority: float) -> None: ...

class Point(Point2D):
    x: int
    y: int
    def __init__(self, *args: Any) -> None: ...
    def getLocation(self) -> Point: ...
    def getX(self) -> float: ...
    def getY(self) -> float: ...
    def move(self, x: int, y: int) -> None: ...
    def setLocation(self, *args: Any) -> None: ...
    def translate(self, dx: int, dy: int) -> None: ...

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

class GridLayout(Object, LayoutManager):
    def __init__(
        self,
        rows: Optional[int] = ...,
        cols: Optional[int] = ...,
        hgap: Optional[int] = ...,
        vgap: Optional[int] = ...,
    ) -> None: ...
    def addLayoutComponent(self, name: AnyStr, comp: Component) -> None: ...
    def getColumns(self) -> int: ...
    def getHgap(self) -> int: ...
    def getRows(self) -> int: ...
    def getVgap(self) -> int: ...
    def layoutContainer(self, parent: Container) -> None: ...
    def minimumLayoutSize(self, parent: Container) -> Dimension: ...
    def preferredLayoutSize(self, parent: Container) -> Dimension: ...
    def removeLayoutComponent(self, comp: Component) -> None: ...
    def setColumns(self, cols: int) -> None: ...
    def setHgap(self, hgap: int) -> None: ...
    def setRows(self, rows: int) -> None: ...
    def setVgap(self, vgap: int) -> None: ...
