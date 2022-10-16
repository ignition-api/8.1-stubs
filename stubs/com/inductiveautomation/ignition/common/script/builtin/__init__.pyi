from typing import Any, Dict, List, Optional, Tuple, Union

from com.inductiveautomation.ignition.common import BasicDataset, Dataset
from com.inductiveautomation.ignition.common.model.values import QualityCode
from com.inductiveautomation.ignition.common.opc import BrowseElementType
from com.inductiveautomation.ignition.common.script.abc import AbstractJythonSequence
from com.inductiveautomation.ignition.common.script.message import Request
from java.lang import Class
from java.lang import Exception as JavaException
from java.lang import Object, String
from org.python.core import PyFunction, PyObject
from org.slf4j import Logger

class AbstractOPCUtilities(Object):
    def browseServer(
        self, opcServer: String, nodeId: String
    ) -> List[AbstractOPCUtilities.PyOPCTag]: ...
    def getServers(self) -> None: ...
    def getServerState(self, opcServer) -> None: ...
    def isServerEnabled(self, serverName) -> None: ...
    def readValue(self, opcServer, itemPath) -> None: ...
    def readValues(self, opcServer, itemPaths) -> None: ...
    def setServerEnabled(self, serverName, enabled) -> None: ...
    def writeValue(self, *args, **kwargs) -> None: ...
    def writeValues(self, *args, **kwargs) -> None: ...

    class PyOPCTag(PyObject):
        displayName: String
        elementType: BrowseElementType
        nodeId: String
        serverName: String
        def __init__(
            self,
            serverName: String,
            nodeId: String,
            displayName: String,
            elementType: BrowseElementType,
        ) -> None: ...
        def __findattr_ex__(self, name: String) -> PyObject: ...
        def getDisplayName(self) -> String: ...
        def getElementType(self) -> BrowseElementType: ...
        def getNodeId(self) -> String: ...
        def getServerName(self) -> String: ...

class DatasetUtilities(Object):
    @staticmethod
    def addColumn(*args) -> None: ...
    @staticmethod
    def addRow(*args) -> None: ...
    @staticmethod
    def addRows(*args) -> None: ...
    @staticmethod
    def appendDataset(ds1, ds2) -> None: ...
    @staticmethod
    def clearDataset(ds) -> None: ...
    @staticmethod
    def dataSetToExcel(headerRow, datasets) -> None: ...
    @staticmethod
    def dataSetToExcelBytes(headerRow, objects, nullsEmpty, sheetNames) -> None: ...
    @staticmethod
    def dataSetToExcelStreaming(headerRow, objects, out, nullsEmpty) -> None: ...
    @staticmethod
    def dataSetToHTML(headerRow, ds, title) -> None: ...
    @staticmethod
    def dataSetToHTMLStreaming(headerRow, ds, title, fw) -> None: ...
    @staticmethod
    def deleteRow(ds, row) -> None: ...
    @staticmethod
    def deleteRows(ds, rows) -> None: ...
    @staticmethod
    def filterColumns(dataset, columns) -> None: ...
    @staticmethod
    def formatDates(dataset, format, locale=...) -> None: ...
    @staticmethod
    def fromCSV(csv) -> None: ...
    @staticmethod
    def fromCSVJava(csv) -> None: ...
    @staticmethod
    def getColumnHeaders(ds) -> None: ...
    @staticmethod
    def insertColumn(*args) -> None: ...
    @staticmethod
    def insertRow(*args) -> None: ...
    @staticmethod
    def setValue(*args) -> None: ...
    @staticmethod
    def sort(
        ds: BasicDataset,
        keyColumn: Union[int, String],
        ascending: Optional[bool] = ...,
        naturalOrdering: Optional[bool] = ...,
    ) -> BasicDataset: ...
    @staticmethod
    def toCSV(*args, **kwargs) -> None: ...
    @staticmethod
    def toCSVJava(ds, showHeaders, forExport, localized: bool = ...) -> None: ...
    @staticmethod
    def toCSVJavaStreaming(ds, showHeaders, forExport, sw, localized) -> None: ...
    @staticmethod
    def toDataSet(*args) -> None: ...
    @staticmethod
    def toExcel(*args, **kwargs) -> None: ...
    @staticmethod
    def toJSONObject(data) -> None: ...
    @staticmethod
    def toPyDataSet(dataset: Dataset) -> PyDataSet: ...
    @staticmethod
    def updateRow(ds, row, changes) -> None: ...

    class PyDataSet(Dataset, AbstractJythonSequence):
        def __init__(self, ds: Optional[Dataset] = ...) -> None: ...
        def __add__(self, other: PyObject) -> PyObject: ...
        def getColumnCount(self) -> int: ...
        def getColumnIndex(self, colName: String) -> int: ...
        def getColumnName(self, col: int) -> String: ...
        def getColumnNames(self) -> List[String]: ...
        def getColumnType(self, col: int) -> Class: ...
        def getColumnTypes(self) -> List[Class]: ...
        def getPrimitiveValueAt(self, row: int, col: int) -> float: ...
        def getQualityAt(self, row: int, col: int) -> QualityCode: ...
        def getRowCount(self) -> int: ...
        def getValueAt(self, row: int, col: Union[int, String]) -> Any: ...
        def setData(self, data: Dataset) -> None: ...

class SProcCall(Object):
    callFinished: bool
    datasource: String
    params: Dict[SProcCall.SProcArgKey, SProcCall.SProcArg]
    procedureName: String
    resultset: Dataset
    returnParam: SProcCall.SProcArg
    skipAudit: bool
    txId: String
    updateCount: int
    def getDataSource(self) -> String: ...
    def getOutParamValue(self, param: Union[int, String]) -> Any: ...
    def getProcedureName(self) -> String: ...
    def getResultSet(self) -> BasicDataset: ...
    def getReturnValue(self) -> Any: ...
    def getTxId(self) -> String: ...
    def getUpdateCount(self) -> int: ...
    def isSkipAudit(self) -> bool: ...
    def registerInParam(
        self, param: Union[int, String], typeCode: int, value: Any
    ) -> None: ...
    def registerOutParam(self, param: Union[int, String], typeCode: int) -> None: ...
    def registerReturnParam(self, typeCode: int) -> None: ...
    def setSkipAudit(self, skipAudit: bool) -> None: ...
    def setTxId(self, txId: String) -> None: ...

    class SProcArg(Object):
        outParam: bool
        inParam: bool
        paramType: int
        value: Object
        def getParamType(self) -> int: ...
        def getValue(self) -> Any: ...
        def isInParam(self) -> bool: ...
        def isOutParam(self) -> bool: ...
        def setParamType(self, paramType: int) -> None: ...
        def setValue(self, value: Object) -> None: ...

    class SProcArgKey(Object):
        index: int
        name: String
        def getParamIndex(self) -> int: ...
        def getParamName(self) -> String: ...
        def isNamedParam(self) -> bool: ...

class SystemUtilities(Object):
    @staticmethod
    def logger(loggerName: String) -> Logger: ...
    @staticmethod
    def parseTranslateArguments(
        *args: PyObject, **kwargs: String
    ) -> Tuple[String, String, bool]: ...

    class RequestImpl(Object, Request):
        timeout: int
        def __init__(self, timeout: int) -> None: ...
        def cancel(self) -> None: ...
        def checkTimeout(self) -> None: ...
        def finishExceptionally(self, e: JavaException) -> None: ...
        def finishSuccessfully(self, value: Object) -> None: ...
        def get(self) -> Object: ...
        def getError(self) -> JavaException: ...
        def getLongId(self) -> long: ...
        def onError(self, func: PyFunction) -> None: ...
        def onSuccess(self, func: PyFunction) -> None: ...
