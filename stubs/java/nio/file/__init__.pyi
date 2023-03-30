from typing import Any, Iterator, List, Optional, Set, Union

from dev.thecesrom.helper.types import AnyStr
from java.io import BufferedReader, BufferedWriter, InputStream, OutputStream
from java.lang import AutoCloseable, CharSequence, Class, Enum, Object
from java.nio.channels import SeekableByteChannel
from java.nio.charset import Charset
from java.nio.file.attribute import (
    BasicFileAttributes,
    FileAttribute,
    FileAttributeView,
    FileStoreAttributeView,
    FileTime,
    PosixFilePermission,
    UserPrincipal,
)
from java.util.function import BiPredicate
from java.util.stream import Stream

class CopyOption: ...

class DirectoryStream(AutoCloseable):
    def close(self) -> None: ...

class OpenOption: ...

class Watchable:
    def register(self, *args: Any) -> WatchKey: ...

class FileStore(Object):
    def getAttribute(self, attribute: AnyStr) -> Object: ...
    def getBlockSize(self) -> long: ...
    def getFileStoreAttributeView(self, type: Class) -> FileStoreAttributeView: ...
    def getTotalSpace(self) -> long: ...
    def getUnallocatedSpace(self) -> long: ...
    def getUsableSpace(self) -> long: ...
    def isReadOnly(self) -> bool: ...
    def name(self) -> AnyStr: ...
    def supportsFileAttributeView(self, type: Class) -> bool: ...
    def type(self) -> AnyStr: ...

class FileVisitOption(Enum):
    FOLLOW_LINKS: FileVisitOption
    @staticmethod
    def values() -> List[FileVisitOption]: ...

class Files(Object):
    @staticmethod
    def copy(*args: Any) -> Union[long, Path]: ...
    @staticmethod
    def createDirectories(dir: Path, *attrs: FileAttribute) -> Path: ...
    @staticmethod
    def createDirectory(dir: Path, *attrs: FileAttribute) -> Path: ...
    @staticmethod
    def createFile(path: Path, *attrs: FileAttribute) -> Path: ...
    @staticmethod
    def createLink(link: Path, existing: Path) -> Path: ...
    @staticmethod
    def createSymbolicLink(link: Path, target: Path, *attrs: FileAttribute) -> Path: ...
    @staticmethod
    def createTempDirectory(*args: Any) -> Path: ...
    @staticmethod
    def createTempFile(*args: Any) -> Path: ...
    @staticmethod
    def delete(path: Path) -> None: ...
    @staticmethod
    def deleteIfExists(path: Path) -> bool: ...
    @staticmethod
    def exists(path: Path, *options: LinkOption) -> bool: ...
    @staticmethod
    def find(
        start: Path, maxDepth: int, matcher: BiPredicate, *options: FileVisitOption
    ) -> Stream: ...
    @staticmethod
    def getAttribute(path: Path, attribute: AnyStr, *options: LinkOption) -> Object: ...
    @staticmethod
    def getFileAttributeView(
        path: Path, type: Class, *options: LinkOption
    ) -> FileAttributeView: ...
    @staticmethod
    def getFileStore(path: Path) -> FileStore: ...
    @staticmethod
    def getLastModifiedTime(path: Path, *options: LinkOption) -> FileTime: ...
    @staticmethod
    def getOwner(path: Path, *options: LinkOption) -> UserPrincipal: ...
    @staticmethod
    def getPosixFilePermissions(
        path: Path, *options: LinkOption
    ) -> Set[PosixFilePermission]: ...
    @staticmethod
    def isDirectory(path: Path, *options: LinkOption) -> bool: ...
    @staticmethod
    def isExecutable(path: Path) -> bool: ...
    @staticmethod
    def isHidden(path: Path) -> bool: ...
    @staticmethod
    def isReadable(path: Path) -> bool: ...
    @staticmethod
    def isRegularFile(path: Path, *options: LinkOption) -> bool: ...
    @staticmethod
    def isSameFile(path: Path, path2: Path) -> bool: ...
    @staticmethod
    def isSymbolicLink(path: Path) -> bool: ...
    @staticmethod
    def isWritable(path: Path) -> bool: ...
    @staticmethod
    def lines(path: Path, cs: Optional[Charset] = ...) -> Stream: ...
    @staticmethod
    def list(path: Path) -> Stream: ...
    @staticmethod
    def move(source: Path, target: Path, *options: CopyOption) -> Path: ...
    @staticmethod
    def newBufferedReader(
        path: Path, cs: Optional[Charset] = ...
    ) -> BufferedReader: ...
    @staticmethod
    def newBufferedWriter(path: Path, *args: Any) -> BufferedWriter: ...
    @staticmethod
    def newByteChannel(path: Path, *args: Any) -> SeekableByteChannel: ...
    @staticmethod
    def newDirectoryStream(dir: Path, *args: Any) -> DirectoryStream: ...
    @staticmethod
    def newInputStream(path: Path, *options: OpenOption) -> InputStream: ...
    @staticmethod
    def newOutputStream(path: Path, *options: OpenOption) -> OutputStream: ...
    @staticmethod
    def notExists(path: Path, *options: LinkOption) -> bool: ...
    @staticmethod
    def probeContentType(path: Path) -> AnyStr: ...
    @staticmethod
    def readAllBytes(path: Path) -> bytearray: ...
    @staticmethod
    def readAllLines(path: Path, cs: Optional[Charset] = ...) -> List[AnyStr]: ...
    @staticmethod
    def readAttributes(path: Path, *args: Any) -> BasicFileAttributes: ...
    @staticmethod
    def readString(path: Path, cs: Optional[Charset] = ...) -> AnyStr: ...
    @staticmethod
    def readSymbolicLink(link: Path) -> Path: ...
    @staticmethod
    def setAttribute(
        path: Path, attribute: AnyStr, value: Object, *options: LinkOption
    ) -> Path: ...
    @staticmethod
    def setLastModifiedTime(path: Path, time: FileTime) -> Path: ...
    @staticmethod
    def setOwner(path: Path, owner: UserPrincipal) -> Path: ...
    @staticmethod
    def setPosixFilePermissions(
        path: Path, perms: Set[PosixFilePermission]
    ) -> Path: ...
    @staticmethod
    def size(path: Path) -> long: ...
    @staticmethod
    def walk(path: Path, *args: Any) -> Stream: ...
    @staticmethod
    def walkFileTree(path: Path, *args: Any) -> Path: ...
    @staticmethod
    def write(path: Path, *args: Any) -> Path: ...
    @staticmethod
    def writeString(path: Path, csq: CharSequence, *args: Any) -> Path: ...

class LinkOption(Enum, CopyOption, OpenOption):
    NOFOLLOW_LINKS: LinkOption
    @staticmethod
    def values() -> List[LinkOption]: ...

class Path(Watchable):
    def compareTo(self, other: Path) -> int: ...
    def endsWith(self, other: Union[Object, Path, AnyStr]) -> bool: ...
    def equals(self, other: Object) -> bool: ...
    def getFileName(self) -> Path: ...
    def getName(self, index: int) -> Path: ...
    def getNameCount(self) -> int: ...
    def getParent(self) -> Path: ...
    def getRoot(self) -> Path: ...
    def hashCode(self) -> int: ...
    def isAbsolute(self) -> bool: ...
    def iterator(self) -> Iterator[Path]: ...
    def normalize(self) -> Path: ...
    @staticmethod
    def of(*args: Any) -> Path: ...
    def register(self, *args: Any) -> WatchKey: ...
    def relativize(self, other: Path) -> Path: ...
    def resolve(self, other: Union[Path, AnyStr]) -> Path: ...
    def resolveSibling(self, other: Path) -> Path: ...
    def startsWith(self, other: Path) -> bool: ...
    def subpath(self, beginIndex: int, endIndex: int) -> Path: ...
    def toAbsolutePath(self) -> Path: ...
    def toFile(self) -> Any: ...
    def toRealPath(self, *args: LinkOption) -> Path: ...
    def toString(self) -> AnyStr: ...
    def toUri(self) -> Any: ...

class Paths(Object):
    @staticmethod
    def get(*args: Any) -> Path: ...

class StandardCopyOption(Enum, CopyOption, OpenOption):
    ATOMIC_MOVE: StandardCopyOption
    COPY_ATTRIBUTES: StandardCopyOption
    REPLACE_EXISTING: StandardCopyOption
    @staticmethod
    def values() -> List[StandardCopyOption]: ...

class WatchEvent:
    def context(self) -> Any: ...
    def count(self) -> int: ...
    def kind(self) -> WatchEvent.Kind: ...

    class Kind:
        def name(self) -> AnyStr: ...
        def type(self) -> Class: ...

    class Modifier:
        def name(self) -> AnyStr: ...

class WatchKey:
    def cancel(self) -> None: ...
    def isValid(self) -> bool: ...
    def pollEvents(self) -> List[WatchEvent]: ...
    def reset(self) -> bool: ...
    def watchable(self) -> Watchable: ...
