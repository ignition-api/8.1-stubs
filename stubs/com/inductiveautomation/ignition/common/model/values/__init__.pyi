from typing import Any, Union

from dev.thecesrom.helper.types import AnyStr
from enum import Enum
from java.lang import Object
from java.util import Date

class QualifiedValue:
    def derive(self, arg: Union[None, QualityCode, AnyStr] = ...) -> QualifiedValue: ...
    def getQuality(self) -> QualityCode: ...
    def getTimestamp(self) -> Date: ...
    def getValue(self) -> Object: ...

class Quality:
    def getDescription(self) -> None: ...
    def getLevel(self) -> None: ...
    def getName(self) -> None: ...
    def getQualityCode(self) -> None: ...
    def isGood(self) -> None: ...

    class Level(Enum):
        Bad: int
        Good: int
        Unknown: int
        def values(self) -> None: ...

class QualityCode(Object):
    Bad: QualityCode
    Bad_AccessDenied: QualityCode
    Bad_AggregateNotFound: QualityCode
    Bad_DatabaseNotConnected: QualityCode
    Bad_Disabled: QualityCode
    Bad_Failure: QualityCode
    Bad_GatewayCommOff: QualityCode
    Bad_LicenseExceeded: QualityCode
    Bad_NotConnected: QualityCode
    Bad_NotFound: QualityCode
    Bad_OutOfRange: QualityCode
    Bad_ReadOnly: QualityCode
    Bad_Stale: QualityCode
    Bad_ReferenceNotFound: QualityCode
    Bad_TrialExpired: QualityCode
    Bad_Unauthorized: QualityCode
    Bad_Unsupported: QualityCode
    Error: QualityCode
    Error_Configuration: QualityCode
    Error_CycleDetected: QualityCode
    Error_DatabaseQuery: QualityCode
    Error_Exception: QualityCode
    Error_ExpressionEval: QualityCode
    Error_Formatting: QualityCode
    Error_InvalidPathSyntax: QualityCode
    Error_IO: QualityCode
    Error_ScriptEval: QualityCode
    Error_TagExecution: QualityCode
    Error_TimeoutExpired: QualityCode
    Error_TypeConversion: QualityCode
    Good: QualityCode
    Good_Backfill: QualityCode
    Good_Initial: QualityCode
    Good_Overload: QualityCode
    Good_Provisional: QualityCode
    Good_Unspecified: QualityCode
    Good_WritePending: QualityCode
    Uncertain: QualityCode
    Uncertain_LastKnownValue: QualityCode
    Uncertain_InitialValue: QualityCode
    Uncertain_DataSubNormal: QualityCode
    Uncertain_EngineeringUnitsExceeded: QualityCode
    Uncertain_IncompleteOperation: QualityCode
    def __init__(self, *args: Any) -> None: ...
    def derive(self, diagnosticMessage) -> None: ...
    def getCode(self) -> None: ...
    def getDiagnosticMessage(self) -> None: ...
    def getLevel(self) -> None: ...
    def getName(self) -> None: ...
    def isBad(self) -> bool: ...
    def isBadOrError(self) -> bool: ...
    def isError(self) -> bool: ...
    def isGood(self) -> bool: ...
    def isNotGood(self) -> bool: ...
    def isUncertain(self) -> bool: ...

    class Level(Object):
        def __init__(self) -> None: ...
        def code(self, userCode) -> None: ...
        @staticmethod
        def valueOf(name) -> None: ...
        @staticmethod
        def values() -> None: ...

class BasicQualifiedValue(QualifiedValue, Object):
    quality: QualityCode
    timestamp: Date
    value: Object
    def __init__(self, *args: Any) -> None: ...
    def BAD(self) -> BasicQualifiedValue: ...
    def CONFIG_ERROR(self) -> BasicQualifiedValue: ...
    def DISABLED(self) -> BasicQualifiedValue: ...
    def EXPRESSION_EVAL_ERROR(self) -> BasicQualifiedValue: ...
    def INITIAL_VALUE(self) -> BasicQualifiedValue: ...
    def NOT_CONNECTED(self) -> BasicQualifiedValue: ...
    def NOT_FOUND(self) -> BasicQualifiedValue: ...
    def REFERENCE_NOT_FOUND(self) -> BasicQualifiedValue: ...
    def STALE(self) -> BasicQualifiedValue: ...
    def TRANSFORM_ERROR(self) -> BasicQualifiedValue: ...
    def TYPE_CONVERSION(self) -> BasicQualifiedValue: ...
    def UNKNOWN(self) -> BasicQualifiedValue: ...
    def UNSUPPORTED(self) -> BasicQualifiedValue: ...
    def clone(self) -> BasicQualifiedValue: ...
    def derive(self, arg: Union[None, QualityCode, AnyStr] = ...) -> QualifiedValue: ...
    @staticmethod
    def fromObject(obj: Object) -> QualifiedValue: ...
    def getQuality(self) -> QualityCode: ...
    def getTimestamp(self) -> Date: ...
    def getValue(self) -> Object: ...
    def setQuality(self, code: QualityCode) -> None: ...
    def setTimestamp(self, timestamp: Date) -> None: ...
    def setValue(self, value: Object) -> None: ...
    @staticmethod
    def unwrap(obj: Object) -> Object: ...
    @staticmethod
    def updateTimestamp(copy: QualifiedValue) -> QualifiedValue: ...
    @staticmethod
    def valueOf(obj: Object) -> Object: ...
