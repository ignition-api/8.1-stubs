from typing import Any, List, Optional

from java.awt import Component, Container, Frame, Graphics
from java.lang import String
from java.util import Locale
from javax.swing.event import AncestorListener
from javax.swing.plaf import DesktopPaneUI
from javax.swing.text import JTextComponent

class DesktopManager:
    def activateFrame(self, f: JInternalFrame) -> None: ...
    def beginDragginFrame(self, f: JComponent) -> None: ...
    def beginResizingFrame(self, f: JComponent, direction: int) -> None: ...
    def closeFrame(self, f: JInternalFrame) -> None: ...
    def deactivateFrame(self, f: JInternalFrame) -> None: ...
    def deiconifyFrame(self, f: JInternalFrame) -> None: ...
    def dragFrame(self, f: JComponent, newX: int, newY: int) -> None: ...
    def endDraggingFrame(self, f: JComponent) -> None: ...
    def endResizing(self, f: JComponent) -> None: ...
    def iconifyFrame(self, f: JInternalFrame) -> None: ...
    def maximizeFrame(self, f: JInternalFrame) -> None: ...
    def minimizeFrame(self, f: JInternalFrame) -> None: ...
    def openFrame(self, f: JInternalFrame) -> None: ...
    def resizeFrame(
        self, f: JComponent, newX: int, newY: int, newWidth: int, newHeight: int
    ) -> None: ...
    def setBoundsForFrame(
        self, f: JComponent, newX: int, newY: int, newWidth: int, newHeight: int
    ) -> None: ...

class Icon:
    def getIconHeight(self) -> int: ...
    def getIconWidth(self) -> int: ...
    def paintIcon(self, c: Component, g: Graphics, x: int, y: int) -> None: ...

class JComponent(Container):
    TOOL_TIP_TEXT_KEY: String
    UNDEFINED_CONDITION: int
    WHEN_ANCESTOR_OF_FOCUSED_COMPONENT: int
    WHEN_FOCUSED: int
    WHEN_IN_FOCUSED_WINDOW: int
    def __init__(self) -> None: ...
    def addAncestorListener(self, listener: AncestorListener) -> None: ...
    def addNotify(self) -> None: ...
    def createToolTip(self) -> JToolTip: ...
    @staticmethod
    def getDefaultLocale() -> Locale: ...
    @staticmethod
    def isLightweightComponent(c: Component) -> bool: ...
    @staticmethod
    def setDefaultLocale(l: Locale) -> None: ...

class JFrame(Frame):
    def __init__(self, *args: Any) -> None: ...

class JInternalFrame(JComponent):
    def __init__(
        self,
        title: Optional[String] = ...,
        resizable: Optional[bool] = ...,
        closable: Optional[bool] = ...,
        maximizable: Optional[bool] = ...,
        iconifiable: Optional[bool] = ...,
    ) -> None: ...

class JLabel(JComponent):
    def __init__(self, *args: Any) -> None: ...

class JLayeredPane(JComponent):
    DEFAULT_LAYER: int
    DRAG_LAYER: int
    FRAME_CONTENT_LAYER: int
    LAYER_PROPERTY: str
    MODAL_LAYER: int
    PALETTE_LAYER: int
    POPUP_LAYER: int
    def __init__(self) -> None: ...
    def getComponentCountInLayer(self, layer: int) -> int: ...
    def getLayer(self, c: Component) -> int: ...
    def highestLayer(self) -> int: ...
    def lowestLayer(self) -> int: ...
    def setPosition(self, c: Component, position: int) -> None: ...

class JDesktopPane(JLayeredPane):
    LIVE_DRAG_MODE: int
    OUTLINE_DRAG_MODE: int
    def __init__(self) -> None: ...
    def getAllFrames(self) -> List[JInternalFrame]: ...
    def getAllFramesInLayer(self, layer: int) -> List[JInternalFrame]: ...
    def getDesktopManager(self) -> DesktopManager: ...
    def getDragMode(self) -> int: ...
    def getSelectedFrame(self) -> JInternalFrame: ...
    def getUI(self) -> DesktopPaneUI: ...
    def getUIClassID(self) -> String: ...
    def updateUI(self) -> None: ...

class JOptionPane(JComponent):
    PLAIN_MESSAGE: int
    ERROR_MESSAGE: int
    INFORMATION_MESSAGE: int
    WARNING_MESSAGE: int
    QUESTION_MESSAGE: int
    DEFAULT_OPTION: int
    YES_NO_OPTION: int
    YES_NO_CANCEL_OPTION: int
    OK_CANCEL_OPTION: int
    CLOSED_OPTION: int
    OK_OPTION: int
    YES_OPTION: int
    NO_OPTION: int
    CANCEL_OPTION: int
    @staticmethod
    def showConfirmDialog(
        parentComponent: Optional[Any],
        message: Any,
        title: Optional[String] = ...,
        optionType: Optional[int] = ...,
        messageType: Optional[int] = ...,
        icon: Optional[Icon] = ...,
    ) -> int: ...
    @staticmethod
    def showInputDialog(
        parentComponent: Optional[Any],
        message: Any,
        title: Optional[String] = ...,
        messageType: Optional[int] = ...,
        icon: Optional[Icon] = ...,
        selectionValues: Optional[List[Any]] = ...,
        initialSelectionValue: Optional[Any] = ...,
    ) -> String: ...
    @staticmethod
    def showMessageDialog(
        parentComponent: Optional[Any],
        message: Any,
        title: Optional[String] = ...,
        messageType: Optional[int] = ...,
        icon: Optional[Icon] = ...,
    ) -> None: ...
    @staticmethod
    def showOptionDialog(
        parentComponent: Optional[Any],
        message: Any,
        title: Optional[String] = ...,
        optionType: Optional[int] = ...,
        messageType: Optional[int] = ...,
        icon: Optional[Icon] = ...,
        options: Optional[List[Any]] = ...,
        initialValue: Optional[Any] = ...,
    ) -> int: ...

class JPanel(JComponent):
    def __init__(self, *args: Any) -> None: ...

class JToolTip(JComponent):
    def __init__(self) -> None: ...
    def getComponent(self) -> JComponent: ...
    def getTipText(self) -> String: ...

class JPopupMenu(JComponent):
    def __init__(self, label: Optional[String] = ...) -> None: ...

class JTextField(JTextComponent):
    def __init__(self, *args: Any) -> None: ...

class JPasswordField(JTextField):
    def __init__(self, *args: Any) -> None: ...
    def copy(self) -> None: ...
    def cut(self) -> None: ...
    def echoCharIsSet(self) -> bool: ...
    def getEchoChar(self) -> String: ...
    def getPassword(self) -> List[String]: ...
    def getUIClassID(self) -> String: ...
    def setEchoChar(self, c: String) -> None: ...
    def updateUI(self) -> None: ...
