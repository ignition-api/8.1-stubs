from typing import Any, List, Optional, Set, TypeVar

from dev.thecesrom.helper.types import AnyStr
from java.io import Closeable, InputStream, OutputStream
from java.lang import Class, Enum, Object
from java.nio.channels import SocketChannel as SocketChannel

T = TypeVar("T")

class SocketAddress(Object):
    def __init__(self) -> None: ...

class FileNameMap:
    def getContentTypeFor(self, fileName: AnyStr) -> AnyStr: ...

class SocketImplFactory:
    def createSocketImpl(self) -> SocketImpl: ...

class SocketOption:
    def name(self) -> AnyStr: ...
    def type(self) -> Class: ...

class InetAddress(Object):
    def getAddress(self) -> bytearray: ...
    @staticmethod
    def getAllByName(host: AnyStr) -> List[InetAddress]: ...
    @staticmethod
    def getByAddress(*args: Any) -> InetAddress: ...
    @staticmethod
    def getByName(host: AnyStr) -> InetAddress: ...
    def getCanonicalHostName(self) -> AnyStr: ...
    def getHostAddress(self) -> AnyStr: ...
    def getHostName(self) -> AnyStr: ...
    @staticmethod
    def getLocalHost() -> InetAddress: ...
    @staticmethod
    def getLoopbackAddress() -> InetAddress: ...
    def isAnyLocalAddress(self) -> bool: ...
    def isLinkLocalAddress(self) -> bool: ...
    def isLoopbackAddress(self) -> bool: ...
    def isMCGlobal(self) -> bool: ...
    def isMCLinkLocal(self) -> bool: ...
    def isMCNodeLocal(self) -> bool: ...
    def isMCOrgLocal(self) -> bool: ...
    def isMCSiteLocal(self) -> bool: ...
    def isMulticastAddress(self) -> bool: ...
    def isReachable(self, *args: Any) -> bool: ...
    def isSiteLocalAddress(self) -> bool: ...

class InetSocketAddress(SocketAddress):
    def __init__(self, *args: Any) -> None: ...
    @staticmethod
    def createUnresolved(host: AnyStr, port: int) -> InetSocketAddress: ...
    def getAddress(self) -> InetAddress: ...
    def getHostname(self) -> AnyStr: ...
    def getHostString(self) -> AnyStr: ...
    def getPort(self) -> int: ...
    def isUnresolved(self) -> bool: ...

class Proxy(Object):
    NO_PROXY: Proxy
    def __init__(self, type_: Proxy.Type, sa: SocketAddress) -> None: ...
    def address(self) -> SocketAddress: ...
    def type(self) -> Proxy.Type: ...

    class Type(Enum):
        DIRECT: Proxy.Type
        HTTP: Proxy.Type
        SOCKS: Proxy.Type
        @staticmethod
        def values() -> List[Proxy.Type]: ...

class Socket(Object, Closeable):
    def __init__(self, *args: Any) -> None: ...
    def bind(self, bindpoint: SocketAddress) -> None: ...
    def close(self) -> None: ...
    def connect(
        self, endpoint: SocketAddress, timeout: Optional[int] = ...
    ) -> None: ...
    def getChannel(self) -> SocketChannel: ...
    def getInetAddress(self) -> InetAddress: ...
    def getInputStream(self) -> InputStream: ...
    def getKeepAlive(self) -> bool: ...
    def getLocalAddress(self) -> InetAddress: ...
    def getLocalPort(self) -> int: ...
    def getLocalSocketAddress(self) -> SocketAddress: ...
    def getOOBInline(self) -> bool: ...
    def getOption(self, name: SocketOption) -> T: ...
    def getOutputStream(self) -> OutputStream: ...
    def getPort(self) -> int: ...
    def getReceiveBufferSize(self) -> int: ...
    def getRemoteSocketAddress(self) -> SocketAddress: ...
    def getReuseAddress(self) -> bool: ...
    def getSendBufferSize(self) -> int: ...
    def getSoLinger(self) -> int: ...
    def getSoTimeout(self) -> int: ...
    def getTcpNoDelay(self) -> bool: ...
    def getTrafficClass(self) -> int: ...
    def isBound(self) -> bool: ...
    def isClosed(self) -> bool: ...
    def isConnected(self) -> bool: ...
    def isInputShutdown(self) -> bool: ...
    def isOutputShutdown(self) -> bool: ...
    def sendUrgentData(self, data: int) -> None: ...
    def setKeepAlive(self, on: bool) -> None: ...
    def setOOBInline(self, on: bool) -> None: ...
    def setOption(self, name: SocketOption, value: T) -> Socket: ...
    def setPerformancePreferences(
        self, connectionTime: int, latency: int, bandwidth: int
    ) -> None: ...
    def setReceiveBufferSize(self, size: int) -> None: ...
    def setReuseAddress(self, on: bool) -> None: ...
    def setSendBufferSize(self, size: int) -> None: ...
    @staticmethod
    def setSocketImplFactory(fac: SocketImplFactory) -> None: ...
    def setSoLinger(self, on: bool, linger: int) -> None: ...
    def setSoTimeout(self, timeout: int) -> None: ...
    def setTcpNoDelay(self, on: bool) -> None: ...
    def setTrafficClass(self, tc: int) -> None: ...
    def shutdownInput(self) -> None: ...
    def shutdownOutput(self) -> None: ...
    def supportedOptions(self) -> Set[SocketOption]: ...

class SocketImpl(Object):
    def __init__(self) -> None: ...
