from typing import Any, List, Optional, Sequence

from com.inductiveautomation.ignition.common.model.values import QualityCode
from java.lang import Object

class Result:
    def getDisplayPath(self) -> None: ...
    def getPath(self) -> None: ...
    def getType(self) -> None: ...
    def hasChildren(self) -> None: ...

class Results(Object):
    continuationPoint: Optional[str]
    resultQuality: QualityCode
    results: Sequence[Any]
    totalAvailableResults: int
    def __init__(self, *args: Any) -> None: ...
    @staticmethod
    def error(result: Results) -> Results: ...
    def getContinuationPoint(self) -> Optional[str]: ...
    def getResultQuality(self) -> QualityCode: ...
    def getResults(self) -> Sequence[Any]: ...
    def getReturnedSize(self) -> int: ...
    def getTotalAvailableSize(self) -> int: ...
    @staticmethod
    def of(results: List[Any]) -> Results: ...
    def setContinuationPoint(self, continuationPoint: Optional[str] = ...) -> None: ...
    def setResultQuality(self, value: QualityCode) -> None: ...
    def setResults(self, results: List[Any]) -> None: ...
    def setTotalAvailableResults(self, totalAvailableResults: int) -> None: ...
