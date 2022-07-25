import __builtin__ as builtins
from typing import Any, TypeVar, Union

String = Union[str, unicode]
T = TypeVar("T")
U = TypeVar("U")

class Object:
    def equals(self, obj: Object) -> bool: ...
    def getClass(self) -> Class: ...
    def hashCode(self) -> int: ...
    def notify(self) -> None: ...
    def notifyAll(self) -> None: ...
    def toString(self) -> String: ...
    def wait(self, timeoutMillis: long = ..., nanos: int = ...) -> None: ...

class Appendable:
    def append(
        self, c_csq: Union[CharSequence, str], start: int = ..., end: int = ...
    ) -> Appendable: ...

class AutoCloseable:
    def close(self) -> None: ...

class CharSequence:
    def charAt(self, index: int) -> str: ...
    def chars(self) -> None: ...
    def codePoints(self) -> None: ...
    @staticmethod
    def compare(cs1: CharSequence, cs2: CharSequence) -> int: ...
    def length(self) -> int: ...
    def subSequence(self, start: int, end: int) -> CharSequence: ...
    def toString(self) -> String: ...

class Class(Object):
    def asSubClass(self, clazz: Class) -> U: ...
    def cast(self, obj: Object) -> T: ...

class Enum(Object):
    def compareTo(self, o) -> None: ...
    def getDeclaringClass(self) -> None: ...
    def name(self) -> None: ...
    def ordinal(self) -> None: ...
    def valueOf(self, enumType, name) -> None: ...

class StackTraceElement(Object):
    def __init__(self, *args) -> None: ...
    def getClassLoaderName(self) -> str: ...
    def getClassName(self) -> str: ...
    def getFileName(self) -> str: ...
    def getLineNumber(self) -> int: ...
    def getMethodName(self) -> str: ...
    def getModuleName(self) -> str: ...
    def getModuleVersion(self) -> str: ...
    def isNativeMethod(self) -> bool: ...

class StringBuffer(Object, CharSequence):
    def __init__(self, *args) -> None: ...
    def append(self, *args) -> None: ...
    def appendCodePoint(self, codePoint: int) -> StringBuffer: ...
    def capacity(self) -> int: ...
    def charAt(self, index: int) -> str: ...
    def codePointAt(self, index: int) -> int: ...
    def codePointBefore(self, index: int) -> int: ...
    def codePointCount(self, beginIndex: int, endIndex: int) -> int: ...
    def compareTo(self, another: StringBuffer) -> int: ...
    def delete(self, start: int, end: int) -> StringBuffer: ...
    def deleteCharAt(self, index: int) -> StringBuffer: ...
    def ensureCapacity(self, minimumCapacity: int) -> None: ...
    def getChars(self, srcBegin: int, srcEnd: int, dst: str, dstBegin: int) -> None: ...
    def indexOf(self, string: str, fromIndex: int = ...) -> int: ...
    def insert(self, *args) -> None: ...
    def lastIndexOf(self, string: str, fromIndex: int = ...) -> int: ...
    def length(self) -> int: ...
    def offsetByCodePoints(self, index: int, codePointOffset: int) -> int: ...
    def replace(self, start: int, end: int, string: str) -> StringBuffer: ...
    def reverse(self) -> StringBuffer: ...
    def setCharAt(self, index: int, ch: str) -> None: ...
    def setLength(self, newLength: int) -> None: ...
    def subSequence(self, start: int, end: int) -> CharSequence: ...
    def substring(self, start: int, end: int = ...) -> str: ...
    def trimToSize(self) -> None: ...

class StringBuilder(Object, CharSequence):
    def __init__(self, *args: Any) -> None: ...
    def append(self, *args: Any) -> StringBuilder: ...
    def capacity(self) -> int: ...
    def charAt(self, index: int) -> str: ...
    def codePointAt(self, index: int) -> int: ...
    def codePointBefore(self, index: int) -> int: ...
    def codePointCount(self, beginIndex: int, endIndex: int) -> int: ...
    def compareTo(self, another: StringBuilder) -> int: ...
    def delete(self, start: int, end: int) -> StringBuilder: ...
    def deleteCharAt(self, index: int) -> StringBuilder: ...
    def ensureCapacity(self, minimumCapacity: int) -> None: ...
    def getChars(self, srcBegin: int, srcEnd: int, dst: str, dstBegin: int) -> None: ...
    def indexOf(self, str_: String, fromIndex: int = ...) -> int: ...
    def insert(self, *args: Any) -> StringBuilder: ...
    def lastIndexOf(self, str_: String, fromIndex: int = ...) -> int: ...
    def length(self) -> int: ...
    def offsetByCodePoints(self, index: int, codePointOffset: int) -> int: ...
    def replace(self, start: int, end: int, str_: int) -> StringBuilder: ...
    def reverse(self) -> StringBuilder: ...
    def setCharAt(self, index: int, ch: str) -> None: ...
    def setLength(self, newLength: int) -> None: ...
    def subSequence(self, start: int, end: int) -> CharSequence: ...
    def substring(self, start: int, end: int = ...) -> String: ...
    def trimToSize(self) -> None: ...

class Throwable(Object, builtins.Exception):
    def __init__(self, message: str = ..., cause: Throwable = ...) -> None: ...
    @property
    def cause(self) -> Throwable: ...
    def addSuppressed(self, exception: Throwable) -> None: ...
    def fillInStackTrace(self) -> Throwable: ...
    def getCause(self) -> Throwable: ...
    def getLocalizedMessage(self) -> str: ...
    def getMessage(self) -> str: ...
    def getStackTrace(self) -> None: ...
    def getSuppressed(self) -> None: ...
    def initCause(self, cause: Throwable = ...) -> None: ...
    @property
    def message(self) -> str: ...
    def printStackTrace(self, *args) -> None: ...
    def setStackTrace(self, stackTrace) -> None: ...
    def toString(self) -> String: ...

class Exception(Throwable):
    def __init__(self, message: str = ..., cause: Throwable = ...) -> None: ...

class RuntimeException(Exception):
    def __init__(self, message: str = ..., cause: Throwable = ...) -> None: ...

class IllegalArgumentException(RuntimeException):
    def __init__(self, message: str = ..., cause: Throwable = ...) -> None: ...

class NullPointerException(RuntimeException):
    def __init__(self, message: str = ..., cause: Throwable = ...) -> None: ...

class Thread(Object):
    @staticmethod
    def sleep(millis) -> None: ...
