from typing import Any, Iterable, List, Mapping, Optional, Union

from dev.thecesrom.helper.types import AnyStr as AnyStr
from java.awt import Dimension, Image
from java.io import File, InputStream, OutputStream, PrintWriter, Writer
from java.lang import Enum, Object
from javax.swing import JComponent, JPanel, RootPaneContainer

class LaunchContext:
    def getAttribute(self, key: AnyStr, defaultValue: Optional[Any] = ...) -> Any: ...
    def getAttributes(self) -> Mapping[AnyStr, Object]: ...
    def getCacheDir(self) -> File: ...
    def getEdgeFlags(self) -> List[AnyStr]: ...
    def getGatewayAddress(self) -> GatewayAddress: ...
    def getGatewayAddresses(self) -> List[GatewayAddress]: ...
    def getGwCacheDir(self) -> File: ...
    def getLaunchManifest(self) -> LaunchManifest: ...
    def getLog(self) -> PrintWriter: ...
    def getMainClass(self) -> AnyStr: ...
    def getParent(self) -> LaunchParent: ...
    def getPlatformEdition(self) -> AnyStr: ...
    def getProjectCacheChkFile(self) -> File: ...
    def getProjectCacheFile(self) -> File: ...
    def getProjectName(self) -> AnyStr: ...
    def getResourceDir(self) -> File: ...
    def getScopeCode(self) -> AnyStr: ...
    def getTranslationDBLocation(self) -> File: ...
    def getUserObject(self) -> bytearray: ...
    def log(self, message: AnyStr, *args: Object) -> None: ...
    def setAttribute(self, key: AnyStr, value: Object) -> None: ...
    def updateGatewayAddressListCache(self, addrs: List[GatewayAddress]) -> None: ...
    def updateProjectCache(self, project: LaunchContext.WritableProject) -> None: ...

    class WritableProject:
        def write(self, stream: OutputStream) -> None: ...

class LaunchParent:
    def getLaunchFlavor(self) -> LaunchParent.LaunchFlavor: ...
    def getRootPaneContainer(self) -> RootPaneContainer: ...
    def isFullScreen(self) -> bool: ...
    def restart(
        self,
        addresses: List[GatewayAddress],
        projectName: AnyStr,
        scope: AnyStr,
        userObj: bytearray,
    ) -> None: ...
    def setContent(self, context: LaunchContext, app: LaunchableApp) -> None: ...

    class LaunchFlavor(Enum):
        @staticmethod
        def values() -> Iterable[LaunchParent.LaunchFlavor]: ...

class GatewayAddress(Object):
    def __init__(
        self, protocol: AnyStr, address: AnyStr, port: int, path: AnyStr
    ) -> None: ...
    def getAddress(self) -> AnyStr: ...
    def getPath(self) -> AnyStr: ...
    def getPort(self) -> int: ...
    def getProcotol(self) -> AnyStr: ...
    @staticmethod
    def parse(addr: AnyStr) -> GatewayAddress: ...
    def toParseableString(self) -> AnyStr: ...

class LaunchContextImpl(Object, LaunchContext):
    def getAttribute(self, key: AnyStr, defaultValue: Optional[Any] = ...) -> Any: ...
    def getAttributes(self) -> Mapping[AnyStr, Object]: ...
    def getCacheDir(self) -> File: ...
    def getEdgeFlags(self) -> List[AnyStr]: ...
    def getGatewayAddress(self) -> GatewayAddress: ...
    def getGatewayAddresses(self) -> List[GatewayAddress]: ...
    def getGwCacheDir(self) -> File: ...
    def getLaunchManifest(self) -> LaunchManifest: ...
    def getLog(self) -> PrintWriter: ...
    def getMainClass(self) -> AnyStr: ...
    def getParent(self) -> LaunchParent: ...
    def getPlatformEdition(self) -> AnyStr: ...
    def getProjectCacheChkFile(self) -> File: ...
    def getProjectCacheFile(self) -> File: ...
    def getProjectName(self) -> AnyStr: ...
    def getResourceDir(self) -> File: ...
    def getScopeCode(self) -> AnyStr: ...
    def getTranslationDBLocation(self) -> File: ...
    def getUserObject(self) -> bytearray: ...
    def log(self, message: AnyStr, *args: Object) -> None: ...
    def setAttribute(self, key: AnyStr, value: Object) -> None: ...
    def updateGatewayAddressListCache(self, addrs: List[GatewayAddress]) -> None: ...
    def updateProjectCache(self, project: LaunchContext.WritableProject) -> None: ...

class LaunchManifest(Object):
    def __init__(self, *args: Any) -> None: ...
    def addModule(self, module: LaunchManifest.Module) -> None: ...
    def getFrameworkVersion(self) -> int: ...
    def getJavaExecutable(self) -> AnyStr: ...
    def getJreVersion(self) -> AnyStr: ...
    def getModules(self) -> Iterable[LaunchManifest.Module]: ...
    def getPort(self) -> int: ...
    def getScope(self) -> AnyStr: ...
    def getThirdPartyScriptModulesHash(self) -> AnyStr: ...
    def isEmpty(self) -> bool: ...
    def isUseSsl(self) -> bool: ...
    def newDiffAction(self, context: LaunchContextImpl) -> Any: ...
    @staticmethod
    def readFrom(is_: InputStream) -> LaunchManifest: ...
    def setJavaExecutable(self, javaExecutable: AnyStr) -> None: ...
    def setUseCondensedDialogFont(self, useCondensedDialogFont: bool) -> None: ...
    def storeTo(self, arg: Union[OutputStream, Writer]) -> None: ...
    def useCondensedDialogFont(self) -> bool: ...

    class Jar(Object):
        def __init__(self, name: AnyStr, crc32: long, length: long) -> None: ...
        def getCrc32(self) -> long: ...
        def getLength(self) -> long: ...
        def getName(self) -> AnyStr: ...

    class Module(Object):
        def __init__(self, name: AnyStr, build: int) -> None: ...
        def addJar(self, file: LaunchManifest.Jar) -> None: ...
        def getBuild(self) -> int: ...
        def getJarFiles(self) -> List[LaunchManifest.Jar]: ...
        def getName(self) -> AnyStr: ...

class LaunchableApp(JPanel):
    def __init__(self, *args: Any) -> None: ...
    def canShutdown(self) -> bool: ...
    def getFrameIcon(self) -> Image: ...
    def getFrameTitle(self) -> AnyStr: ...
    def getGlassPane(self) -> JComponent: ...
    def getInitialFrameSize(self) -> Dimension: ...
    def getScreenIndex(self) -> int: ...
    def isStartCentered(self) -> bool: ...
    def isStartMaximized(self) -> bool: ...
    def setFrameIcon(self, frameIcon: Image) -> None: ...
    def setFrameTitle(self, frameTitle: AnyStr) -> None: ...
    def setGlassPane(self, frameIcon: JComponent) -> None: ...
    def shutdown(self) -> None: ...
