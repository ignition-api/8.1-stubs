from java.awt import Component, Graphics
from java.lang import Object

class ComponentUI(Object):
    def __init__(self) -> None: ...
    def contains(self, c: Component, x: int, y: int) -> bool: ...
    def paint(self, g: Graphics, c: Component) -> None: ...
    def update(self, g: Graphics, c: Component) -> None: ...

class DesktopPaneUI(ComponentUI):
    def __init__(self) -> None: ...
