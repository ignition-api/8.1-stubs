import __builtin__ as builtins
from typing import Any, List, Optional, TypeVar, Union

from dev.thecesrom.helper.types import AnyStr

T = TypeVar("T")
U = TypeVar("U")

class Object:
    def __init__(self) -> None: ...
    def __cmp__(self, other: Object) -> bool: ...
    def __ge__(self, other: Object) -> bool: ...
    def __gt__(self, other: Object) -> bool: ...
    def __lt__(self, other: Object) -> bool: ...
    def equals(self, obj: Object) -> bool: ...
    def getClass(self) -> Class: ...
    def hashCode(self) -> int: ...
    def notify(self) -> None: ...
    def notifyAll(self) -> None: ...
    def toString(self) -> AnyStr: ...
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
    def toString(self) -> AnyStr: ...

class Runnable:
    def run(self) -> None: ...

class Class(Object):
    def asSubClass(self, clazz: Class) -> U: ...
    def cast(self, obj: Object) -> T: ...

class Enum(Object):
    def compareTo(self, o: Enum) -> int: ...
    def getDeclaringClass(self) -> Class: ...
    def name(self) -> AnyStr: ...
    def ordinal(self) -> int: ...
    @staticmethod
    def valueOf(enumType: Class, name: AnyStr) -> Enum: ...

class Number(Object):
    def byteValue(self) -> int: ...
    def doubleValue(self) -> float: ...
    def floatValue(self) -> float: ...
    def intValue(self) -> int: ...
    def longValue(self) -> long: ...
    def shortValue(self) -> int: ...

class StackTraceElement(Object):
    def __init__(self, *args: Any) -> None: ...
    def getClassLoaderName(self) -> str: ...
    def getClassName(self) -> str: ...
    def getFileName(self) -> str: ...
    def getLineNumber(self) -> int: ...
    def getMethodName(self) -> str: ...
    def getModuleName(self) -> str: ...
    def getModuleVersion(self) -> str: ...
    def isNativeMethod(self) -> bool: ...

class String(unicode):
    def __new__(cls, value, *args): ...
    def charAt(self, index: int) -> unicode: ...
    def chars(self) -> None: ...
    def codePointAt(self, index: int) -> int: ...
    def codePointBefore(self, index: int) -> int: ...
    def codePointCount(self, beginIndex: int, endIndex: int) -> int: ...
    def codePoints(self) -> None: ...
    @staticmethod
    def compare(cs1: CharSequence, cs2: CharSequence) -> int: ...
    def compareTo(self, anotherString: String) -> int: ...
    def compareToIgnoreCase(self, arg: String) -> int: ...
    def concat(self, arg: String) -> String: ...
    def contains(self, arg: String) -> bool: ...
    def contentEquals(self, arg: Union[CharSequence, StringBuffer]) -> bool: ...
    @staticmethod
    def copyValueOf(*args: Any) -> String: ...
    def endsWith(self, suffix: String) -> bool: ...
    def equals(self, anObject: Object) -> bool: ...
    def equalsIgnoreCase(self, anotherString: String) -> bool: ...
    def getBytes(self, *args: Any) -> Optional[object]: ...
    def getChars(
        self, srcBegin: int, srcEnd: int, dst: object, dstBegin: int
    ) -> None: ...
    def getClass(self) -> Class: ...
    def hashCode(self) -> int: ...
    def indexOf(
        self, arg: Union[int, String], fromIndex: Optional[int] = ...
    ) -> int: ...
    def intern(self) -> String: ...
    def isBlank(self) -> bool: ...
    def isEmpty(self) -> bool: ...
    def lastIndexOf(
        self, arg: Union[int, String], fromIndex: Optional[int] = ...
    ) -> int: ...
    def length(self) -> int: ...
    def lines(self) -> None: ...
    def matches(self, regex: String) -> bool: ...
    def notify(self) -> None: ...
    def notifyAll(self) -> None: ...
    def offsetByCodePoints(self, index: int, codePointOffset: int) -> int: ...
    def regionMatches(self, *args: Any) -> bool: ...
    def repeat(self, count: int) -> String: ...
    def replaceAll(self, regex: String, replacement: String) -> String: ...
    def replaceFirst(self, regex: String, replacement: String) -> String: ...
    def startsWith(self, prefix: String, offset: int = ...) -> bool: ...
    def stripLeading(self) -> String: ...
    def stripTrailing(self) -> String: ...
    def subSequence(self, start: int, end: int) -> CharSequence: ...
    def substring(self, beginIndex: int, endIndex: Optional[int] = ...) -> String: ...
    def toCharArray(self) -> object: ...
    def toLowerCase(self, locale: Optional[Any] = ...) -> String: ...
    def toString(self) -> unicode: ...
    def toUpperCase(self) -> String: ...
    @staticmethod
    def valueOf(*args: Any) -> String: ...
    def wait(self, timeoutMillis: long = ..., nanos: int = ...) -> None: ...

class StringBuffer(Object, CharSequence):
    def __init__(self, *args: Any) -> None: ...
    def append(self, *args: Any) -> StringBuffer: ...
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
    def insert(self, *args: Any) -> StringBuffer: ...
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
    def indexOf(self, str_: AnyStr, fromIndex: int = ...) -> int: ...
    def insert(self, *args: Any) -> StringBuilder: ...
    def lastIndexOf(self, str_: AnyStr, fromIndex: int = ...) -> int: ...
    def length(self) -> int: ...
    def offsetByCodePoints(self, index: int, codePointOffset: int) -> int: ...
    def replace(self, start: int, end: int, str_: int) -> StringBuilder: ...
    def reverse(self) -> StringBuilder: ...
    def setCharAt(self, index: int, ch: str) -> None: ...
    def setLength(self, newLength: int) -> None: ...
    def subSequence(self, start: int, end: int) -> CharSequence: ...
    def substring(self, start: int, end: int = ...) -> AnyStr: ...
    def trimToSize(self) -> None: ...

class Throwable(Object, builtins.Exception):
    def __init__(
        self, message: Optional[str] = ..., cause: Optional[Throwable] = ...
    ) -> None: ...
    @property
    def cause(self) -> Throwable: ...
    def addSuppressed(self, exception: Throwable) -> None: ...
    def fillInStackTrace(self) -> Throwable: ...
    def getCause(self) -> Throwable: ...
    def getLocalizedMessage(self) -> str: ...
    def getMessage(self) -> str: ...
    def getStackTrace(self) -> List[StackTraceElement]: ...
    def getSuppressed(self) -> List[Throwable]: ...
    def initCause(self, cause: Optional[Throwable] = ...) -> None: ...
    @property
    def message(self) -> str: ...
    def printStackTrace(self, *args: Any) -> None: ...
    def setStackTrace(self, stackTrace: List[StackTraceElement]) -> None: ...
    def toString(self) -> AnyStr: ...

class Exception(Throwable):
    def __init__(
        self, message: Optional[str] = ..., cause: Optional[Throwable] = ...
    ) -> None: ...

class RuntimeException(Exception):
    def __init__(
        self, message: Optional[str] = ..., cause: Optional[Throwable] = ...
    ) -> None: ...

class IllegalArgumentException(RuntimeException):
    def __init__(
        self, message: Optional[str] = ..., cause: Optional[Throwable] = ...
    ) -> None: ...

class NullPointerException(RuntimeException):
    def __init__(
        self, message: Optional[str] = ..., cause: Optional[Throwable] = ...
    ) -> None: ...

class Thread(Object):
    @staticmethod
    def sleep(millis: long) -> None: ...
