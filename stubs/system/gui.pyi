from typing import Any, Callable, List, Optional, Tuple

from com.inductiveautomation.factorypmi.application import FPMIWindow
from com.inductiveautomation.factorypmi.application.script.builtin import (
    WindowUtilities,
)
from dev.coatl.helper.types import AnyNum, AnyStr
from java.awt import Color
from java.org.jdesktop.core.animation.timing import Animator
from java.util import EventObject
from javax.swing import JComponent, JFrame, JPopupMenu

ACCL_NONE: int
ACCL_CONSTANT: int
ACCL_FAST_TO_SLOW: int
ACCL_SLOW_TO_FAST: int
ACCL_EASE: int
COORD_DESIGNER: int
COORD_SCREEN: int

def chooseColor(initialColor: Color, dialogTitle: AnyStr = ...) -> Color: ...
def closeDesktop(handle: AnyStr) -> None: ...
def color(*args: Any) -> Color: ...
def confirm(
    message: AnyStr, title: AnyStr = ..., allowCancel: bool = ...
) -> Optional[bool]: ...
def convertPointToScreen(x: int, y: int, event: EventObject) -> Tuple[int, int]: ...
def createPopupMenu(
    itemNames: List[AnyStr], itemFunctions: List[Callable[..., Any]]
) -> JPopupMenu: ...
def desktop(handle: AnyStr) -> WindowUtilities: ...
def errorBox(message: AnyStr, title: AnyStr = ...) -> None: ...
def findWindow(path: AnyStr) -> List[FPMIWindow]: ...
def getCurrentDesktop() -> AnyStr: ...
def getDesktopHandles() -> List[AnyStr]: ...
def getOpenedWindowNames() -> Tuple[AnyStr, ...]: ...
def getOpenedWindows() -> Tuple[FPMIWindow, ...]: ...
def getParentWindow(event: EventObject) -> FPMIWindow: ...
def getQuality(component: JComponent, propertyName: AnyStr) -> int: ...
def getScreenIndex() -> int: ...
def getScreens() -> List[Tuple[AnyStr, int, int]]: ...
def getSibling(event: EventObject, name: AnyStr) -> FPMIWindow: ...
def getWindow(name: AnyStr) -> FPMIWindow: ...
def getWindowNames() -> Tuple[AnyStr, ...]: ...
def inputBox(message: AnyStr, defaultText: AnyStr = ...) -> Optional[AnyStr]: ...
def isTouchscreenModeEnabled() -> bool: ...
def messageBox(message: AnyStr, title: AnyStr = ...) -> None: ...
def openDesktop(
    screen: int = ...,
    handle: Optional[AnyStr] = ...,
    title: Optional[AnyStr] = ...,
    width: Optional[int] = ...,
    height: Optional[int] = ...,
    x: int = ...,
    y: int = ...,
    windows: Optional[List[AnyStr]] = ...,
) -> JFrame: ...
def openDiagnostics() -> None: ...
def passwordBox(
    message: AnyStr, title: AnyStr = ..., echoChar: AnyStr = ...
) -> Optional[AnyStr]: ...
def setScreenIndex(index: int) -> None: ...
def setTouchscreenModeEnabled(enabled: bool) -> None: ...
def showNumericKeypad(
    initialValue: AnyNum, fontSize: Optional[int] = ..., usePasswordMode: bool = ...
) -> AnyNum: ...
def showTouchscreenKeyboard(
    initialText: AnyStr,
    fontSize: Optional[int] = ...,
    passwordMode: Optional[bool] = ...,
) -> AnyStr: ...
def transform(
    component: JComponent,
    newX: Optional[int] = ...,
    newY: Optional[int] = ...,
    newWidth: Optional[int] = ...,
    newHeight: Optional[int] = ...,
    duration: int = ...,
    callback: Optional[Callable[..., Any]] = ...,
    framesPerSecond: int = ...,
    acceleration: Optional[int] = ...,
    coordSpace: Optional[int] = ...,
) -> Animator: ...
def warningBox(message: AnyStr, title: AnyStr = ...) -> None: ...
