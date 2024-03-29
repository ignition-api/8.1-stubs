from typing import Any, Iterable, List, Mapping, Optional

from com.inductiveautomation.ignition.common.xmlserialization import (
    ClassNameResolver,
    SerializationException,
)
from com.inductiveautomation.ignition.common.xmlserialization.serialization import (
    XMLSerializer,
)
from dev.coatl.helper.types import AnyStr
from java.io import InputStream, Reader
from java.lang import Class, Object

class AttributesMap:
    def getClass(self, name: AnyStr) -> Class: ...
    def getDecoder(self, name: AnyStr) -> Any: ...
    def getInt(self, name: AnyStr) -> int: ...
    def getLength(self) -> int: ...
    def getName(self, index: int) -> AnyStr: ...
    def getSignature(self, name: AnyStr) -> Iterable[Class]: ...
    def getAnyStr(self, name: AnyStr) -> AnyStr: ...
    def getValue(self, name: AnyStr, decoder: Any) -> Any: ...

class DeserializationContext:
    def getClassNameMap(self) -> ClassNameResolver: ...
    def getRootAttributes(self) -> Mapping[AnyStr, AnyStr]: ...
    def getRootObjects(self) -> List[Object]: ...
    def getWarnings(self) -> List[SerializationException]: ...

class DeserializationHandler:
    def clone(self) -> DeserializationHandler: ...
    def endElement(self, context: DeserializationContext) -> None: ...
    def endObject(self, obj: Object) -> None: ...
    def endSubElement(self, name: AnyStr, context: DeserializationContext) -> None: ...
    def getBodyDecoder(self) -> Any: ...
    def getElementName(self) -> AnyStr: ...
    def getObject(self) -> Object: ...
    def getRefId(self) -> int: ...
    def onBody(self, body: Object) -> None: ...
    def setRefId(self, id_: int) -> None: ...
    def startElement(
        self, name: AnyStr, attributes: AttributesMap, context: DeserializationContext
    ) -> None: ...
    def startSubElement(
        self, name: AnyStr, attributes: AttributesMap, context: DeserializationContext
    ) -> None: ...
    def supportsNestedElements(self) -> bool: ...

class XMLDeserializer(Object):
    def __init__(self, resolver: Optional[ClassNameResolver] = ...) -> None: ...
    def addHandler(self, handler: DeserializationHandler) -> None: ...
    def deserialize(self, *args: Any) -> DeserializationContext: ...
    def deserializeBinary(self, *args: Any) -> DeserializationContext: ...
    def deserializeMultiple(
        self, bytes_: bytearray, count: int
    ) -> List[DeserializationContext]: ...
    def deserializeXML(
        self, streamReader: Reader, topAttributesOnly: bool
    ) -> DeserializationContext: ...
    def getClassNameMap(self) -> ClassNameResolver: ...
    def initDefaults(self) -> XMLDeserializer: ...
    def readRootAttributes(self, arg: Any) -> Mapping[AnyStr, AnyStr]: ...
    def transcodeToXML(
        self, binary: InputStream, serializer: XMLSerializer
    ) -> AnyStr: ...
