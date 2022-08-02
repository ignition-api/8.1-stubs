from typing import Any, List, Optional, Union

from com.inductiveautomation.ignition.common.model.values import QualityCode
from com.inductiveautomation.ignition.common.sqltags.model.types import DataQuality
from java.lang import Class, Object, String

class Dataset:
    def binarySearch(self, column: int, key: Any) -> int: ...
    def getColumnAsList(self, col: int) -> List[Any]: ...
    def getColumnCount(self) -> int: ...
    def getColumnIndex(self, name: str) -> int: ...
    def getColumnName(self, col: int) -> String: ...
    def getColumnNames(self) -> List[String]: ...
    def getColumnType(self, col: int) -> Class: ...
    def getColumnTypes(self) -> List[Class]: ...
    def getPrimitiveValueAt(self, row: int, col: int) -> float: ...
    def getQualityAt(self, row: int, col: int) -> QualityCode: ...
    def getRowCount(self) -> int: ...
    def getValueAt(self, row: int, col: Union[int, String]) -> Any: ...
    def hasQualityData(self) -> bool: ...

class AbstractDataset(Dataset):
    def __init__(
        self,
        columnNames: List[String],
        columnTypes: List[Class],
        qualityCodes: Optional[List[List[QualityCode]]] = ...,
    ) -> None: ...
    @staticmethod
    def convertToQualityCodes(
        dataQualities: List[List[DataQuality]],
    ) -> List[List[QualityCode]]: ...
    def getBulkQualityCodes(self) -> List[List[QualityCode]]: ...
    def getColumnCount(self) -> int: ...
    def getColumnIndex(self, name: str) -> int: ...
    def getColumnName(self, col: int) -> String: ...
    def getColumnNames(self) -> List[String]: ...
    def getColumnType(self, col: int) -> Class: ...
    def getColumnTypes(self) -> List[Class]: ...
    def getPrimitiveValueAt(self, row: int, col: int) -> float: ...
    def getQualityAt(self, row: int, col: int) -> QualityCode: ...
    def getRowCount(self) -> int: ...
    def getValueAt(self, row: int, col: Union[int, String]) -> Any: ...
    def setColumnNames(self, arg: List[str]) -> None: ...
    def setColumnTypes(self, arg: List[Class]) -> None: ...
    def setDirty(self) -> None: ...

class BasicDataset(AbstractDataset):
    def __init__(self, *args: Any) -> None: ...
    def columnContainsNulls(self, col) -> None: ...
    def datasetContainsNulls(self) -> None: ...
    def getData(self) -> None: ...
    def setAllDirectly(self, columnNames, columnTypes, data) -> None: ...
    def setDataDirectly(self, arg) -> None: ...
    def setFromXML(self, columnNames, columnTypes, encodedData, rowCount) -> None: ...
    def setValueAt(self, row, col, value) -> None: ...

class Path:
    def getLastPathComponent(self) -> str: ...
    def getParentPath(self) -> Path: ...
    def getPathLength(self) -> int: ...
    def isAncestorOf(self, path: Path) -> bool: ...

class QualifiedPath(Object):
    def extend(self, id_, value) -> None: ...
    def getFirstPathComponent(self) -> None: ...
    def getFirstPathComponentId(self) -> None: ...
