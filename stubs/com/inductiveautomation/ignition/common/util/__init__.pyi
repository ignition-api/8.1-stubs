from typing import Any, Optional, Union

from java.io import Closeable
from java.lang import AutoCloseable, Class, Object, String, Throwable
from org.apache.commons.lang3.builder import ToStringStyle
from org.slf4j import Logger

class LoggerEx(Object):
    DEFAULT_TO_STRING_STYLE: ToStringStyle
    def createSubLogger(self, arg: Union[Class, String]) -> LoggerEx: ...
    def debug(self, message: String, t: Optional[Throwable] = ...) -> None: ...
    def debugDuration(self, message: String) -> Closeable: ...
    def debugEvent(self, message: String, *args: Any) -> None: ...
    def debugf(self, message: String, *args: Any) -> None: ...
    def error(self, message: String, t: Optional[Throwable] = ...) -> None: ...
    def errorEvent(self, message: String, *args: Any) -> None: ...
    def errorf(self, message: String, *args: Any) -> None: ...
    def fatal(self, message: String, t: Optional[Throwable] = ...) -> None: ...
    def getIdentObject(self) -> Object: ...
    def getLoggerSLF4J(self) -> Logger: ...
    def getName(self) -> String: ...
    def getToStringStyle(self) -> ToStringStyle: ...
    def info(self, message: String, t: Optional[Throwable] = ...) -> None: ...
    def infoDuration(self, message: String) -> Closeable: ...
    def infoEvent(self, message: String, *args: Any) -> None: ...
    def infof(self, message: String, *args: Any) -> None: ...
    def isDebugEnabled(self) -> bool: ...
    def isIdentObjectEnabled(self) -> bool: ...
    def isInfoEnabled(self) -> bool: ...
    def isTraceEnabled(self) -> bool: ...
    def mdcClose(self) -> None: ...
    def mdcPut(self, key: String, value: String) -> None: ...
    def mdcPutCloseable(self, key: String, value: String) -> LoggerEx.MDCCloseable: ...
    def mdcRemove(self, key: String) -> None: ...
    def mdcSet(self) -> LoggerEx.MDCCloseable: ...
    @staticmethod
    def newBuilder() -> LoggerEx.Builder: ...
    def setIdentObject(self, identObj: Object) -> None: ...
    def setToStringStyle(self, toStringStyle: ToStringStyle) -> None: ...
    def trace(self, message: String, t: Optional[Throwable] = ...) -> None: ...
    def traceDuration(self, message: String) -> Closeable: ...
    def traceEvent(self, message: String, *args: Any) -> None: ...
    def tracef(self, message: String, *args: Any) -> None: ...
    def warn(self, message: String, t: Optional[Throwable] = ...) -> None: ...
    def warnEvent(self, message: String, *args: Any) -> None: ...
    def warnf(self, message: String, *args: Any) -> None: ...

    class Builder(Object):
        def build(self, *args: Any) -> LoggerEx: ...
        def eventSystem(self, systemId: str) -> LoggerEx.Builder: ...
        def identObject(self, identObj: Object) -> LoggerEx.Builder: ...
        def mdcContext(self, *args: Object) -> LoggerEx.Builder: ...
        def mutableIdentObject(self, identObj: Object) -> LoggerEx.Builder: ...

    class MDCCloseable(Object, AutoCloseable):
        def close(self) -> None: ...
