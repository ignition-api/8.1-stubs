from typing import Any, Optional

from dev.coatl.helper.types import AnyStr
from java.lang import Object, Throwable
from java.util import Enumeration
from org.apache.log4j.spi import ErrorHandler, Filter, LoggerRepository, LoggingEvent

class Appender:
    def addFilter(self, newFilter: Filter) -> None: ...
    def clearFilters(self) -> None: ...
    def close(self) -> None: ...
    def doAppend(self, event: LoggingEvent) -> None: ...
    def getErrorHandler(self) -> ErrorHandler: ...
    def getFilter(self) -> Filter: ...
    def getLayout(self) -> Layout: ...
    def getName(self) -> AnyStr: ...
    def requiresLayout(self) -> bool: ...
    def setErrorHandler(self, errorHandler: ErrorHandler) -> None: ...
    def setLayout(self, layout: Layout) -> None: ...
    def setName(self, name: AnyStr) -> None: ...

class Category(Object):
    def addApender(self, newAppender: Appender) -> None: ...
    def assertLog(self, assertion: bool, msg: AnyStr) -> None: ...
    def callAppenders(self, event: LoggingEvent) -> None: ...
    def debug(self, message: AnyStr, t: Optional[Throwable] = ...) -> None: ...
    def error(self, message: AnyStr, t: Optional[Throwable] = ...) -> None: ...
    def fatal(self, message: AnyStr, t: Optional[Throwable] = ...) -> None: ...
    def getAdditivity(self) -> bool: ...
    def getAllAppenders(self) -> Enumeration: ...
    def getAppender(self, name: AnyStr) -> Appender: ...
    def getLevel(self) -> Level: ...
    def getLoggerRepository(self) -> LoggerRepository: ...
    def info(self, message: AnyStr, t: Optional[Throwable] = ...) -> None: ...
    def warn(self, message: AnyStr, t: Optional[Throwable] = ...) -> None: ...

class Layout(Object):
    def __init__(self) -> None: ...
    def format(self, event: LoggingEvent) -> AnyStr: ...
    def getContentType(self) -> AnyStr: ...
    def getFooter(self) -> AnyStr: ...
    def getHeader(self) -> AnyStr: ...
    def ignoresThrowable(self) -> bool: ...

class Priority(Object):
    def getSyslogEquivalent(self) -> int: ...
    def isGreaterOrEqual(self, r: Priority) -> bool: ...
    def toInt(self) -> int: ...

class Level(Priority):
    @staticmethod
    def toLevel(*args: Any) -> Level: ...

class Logger(Category):
    @staticmethod
    def getLogger(*args: Any) -> Logger: ...
    def isTraceEnabled(self) -> bool: ...
    def trace(self, message: AnyStr, t: Optional[Throwable] = ...) -> None: ...
