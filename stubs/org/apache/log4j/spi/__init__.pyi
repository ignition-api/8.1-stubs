from typing import Any, Optional

from dev.coatl.helper.types import AnyStr
from java.lang import Exception, Object
from java.util import Enumeration

class OptionHandler:
    def activateOptions(self) -> None: ...

class ErrorHandler(OptionHandler):
    def activateOptions(self) -> None: ...
    def error(
        self,
        message: AnyStr,
        e: Optional[Exception] = ...,
        errorCode: Optional[int] = ...,
        event: Optional[LoggingEvent] = ...,
    ) -> None: ...
    def setAppender(self, appender: Any) -> None: ...
    def setBackupAppender(self, appender: Any) -> None: ...
    def setLogger(self, logger: Any) -> None: ...

class HierarchyEventListener:
    def addAppenderEvent(self, cat: Any, appender: Any) -> None: ...
    def removeAppenderEvent(self, cat: Any, appender: Any) -> None: ...

class LoggerFactory:
    def makeNewLoggerInstance(self, name: AnyStr) -> Any: ...

class LoggerRepository:
    def addHierarchyEventListener(self, listener: HierarchyEventListener) -> None: ...
    def emitNoAppenderWarning(self, cat: Any) -> None: ...
    def exists(self, name: AnyStr) -> Any: ...
    def fireAddAppenderEvent(self, logger: Any, appender: Any) -> None: ...
    def getCurrentLoggers(self) -> Enumeration: ...
    def getLogger(
        self, name: AnyStr, factory: Optional[LoggerFactory] = ...
    ) -> Any: ...
    def getRootLogger(self) -> Any: ...
    def getThreshold(self) -> Any: ...
    def isDisabled(self, level: int) -> bool: ...
    def resetConfiguration(self) -> None: ...
    def setThreshold(self, arg: Any) -> None: ...
    def shutdown(self) -> None: ...

class Filter(Object, OptionHandler):
    def activateOptions(self) -> None: ...
    def decide(self, event: LoggingEvent) -> int: ...
    def getNext(self) -> Filter: ...
    def setNext(self, next: Filter) -> None: ...

class LoggingEvent(Object):
    categoryName: AnyStr
    fqnOfCategoryClass: AnyStr
    level: Any
    timeStamp: long
    def __init__(self, *args: Any) -> None: ...
