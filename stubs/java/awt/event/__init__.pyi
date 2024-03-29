from typing import Any

from dev.coatl.helper.types import AnyStr
from java.awt import AWTEvent, Component, Point
from java.lang import Object

class ActionEvent(AWTEvent):
    ACTION_FIRST: int
    ACTION_LAST: int
    ACTION_PERFORMED: int
    ACTION_MASK: int
    CTRL_MASK: int
    META_MASK: int
    SHIFT_MASK: int
    def __init__(self, source: Object, id: int, *args: Any) -> None: ...
    def getActionCommand(self) -> AnyStr: ...
    def getModifiers(self) -> int: ...
    def getWhen(self) -> long: ...

class ComponentEvent(AWTEvent):
    COMPONENT_FIRST: int
    COMPONENT_HIDDEN: int
    COMPONENT_LAST: int
    COMPONENT_MOVED: int
    COMPONENT_RESIZED: int
    COMPONENT_SHOWN: int
    def __init__(self, source: Object, id: int) -> None: ...
    def getComponent(self) -> Component: ...

class InputEvent(ComponentEvent):
    ALT_DOWN_MASK: int
    ALT_GRAPH_DOWN_MASK: int
    ALT_GRAPH_MASL: int
    ALT_MASK: int
    BUTTON1_DOWN_MASK: int
    BUTTOM1_MASK: int
    BUTTON2_DOWN_MASK: int
    BUTTON2_MASK: int
    BUTTON3_DOWN_MASK: int
    BUTTON3_MASK: int
    CTRL_DOWN_MASK: int
    CTRL_MASK: int
    META_DOWN_MASK: int
    META_MASK: int
    SHIFT_DOWN_MASK: int
    SHIFT_MASK: int
    def consume(self) -> None: ...
    @staticmethod
    def getMaskForButton(button: int) -> int: ...
    def getModifiersEx(self) -> int: ...
    @staticmethod
    def getModifiersExText(modifiers: int) -> AnyStr: ...
    def getWhen(self) -> long: ...
    def isAltDown(self) -> bool: ...
    def isAltGraphDown(self) -> bool: ...
    def isConsumed(self) -> bool: ...
    def isControlDown(self) -> bool: ...
    def isMetaDown(self) -> bool: ...
    def isShiftDown(self) -> bool: ...

class MouseEvent(InputEvent):
    BUTTON1: int
    BUTTON2: int
    BUTTON3: int
    MOUSE_CLICKED: int
    MOUSE_DRAGGED: int
    MOUSE_ENTERED: int
    MOUSE_EXITED: int
    MOUSE_FIRST: int
    MOUSE_LAST: int
    MOUSE_MOVED: int
    MOUSE_PRESSED: int
    MOUSE_RELEASED: int
    MOUSE_WHEEL: int
    NOBUTTON: int
    def __init__(self, source: Component, id: int, *args: Any) -> None: ...
    def getButton(self) -> int: ...
    def getClickCount(self) -> int: ...
    def getLocationOnScreen(self) -> Point: ...
    @staticmethod
    def getMouseModifiersText(modifiers: int) -> AnyStr: ...
    def getPoint(self) -> Point: ...
    def getX(self) -> int: ...
    def getXOnScreen(self) -> int: ...
    def getY(self) -> int: ...
    def getYOnScreen(self) -> int: ...
    def isPopupTrigger(self) -> bool: ...
    def translatePoint(self, x: int, y: int) -> None: ...
