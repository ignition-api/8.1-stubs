from typing import Any, Set, Union

from dev.coatl.helper.types import AnyStr
from java.lang import Class, Object
from java.util import Collection, Date, Map
from org.bson.codecs.configuration import CodecRegistry
from org.bson.types import ObjectId

class BSONObject:
    def containsField(self, s: AnyStr) -> bool: ...
    def get(self, key: AnyStr) -> Object: ...
    def keySet(self) -> Set[AnyStr]: ...
    def put(self, k: AnyStr, v: Object) -> Object: ...
    def putAll(self, arg: Union[BSONObject, Map]) -> None: ...
    def removeField(self, key: AnyStr) -> Object: ...
    def toMap(self) -> Map: ...

class BsonValue(Object):
    def __init__(self) -> None: ...

class BsonDocument(BsonValue):
    def __init__(self, *args: Any) -> None: ...

class Document(Object):
    def __init__(self, *args: Any) -> None: ...
    def append(self, key: AnyStr, value: Object) -> Document: ...
    def clear(self) -> None: ...
    def containsKey(self, key: Object) -> bool: ...
    def containsValue(self, value: Object) -> bool: ...
    def entrySet(self) -> Set[Any]: ...
    def get(self, *args: Any) -> Any: ...
    def getBoolean(self, *args: Any) -> bool: ...
    def getDate(self, key: Object) -> Date: ...
    def getDouble(self, key: Object) -> float: ...
    def getInteger(self, key: Object) -> int: ...
    def getLong(self, key: Object) -> long: ...
    def getObjectId(self, key: Object) -> ObjectId: ...
    def getString(self, key: Object) -> AnyStr: ...
    def isEmpty(self) -> bool: ...
    def keySet(self) -> Set[AnyStr]: ...
    @staticmethod
    def parse(*args: Any) -> Document: ...
    def put(self, key: AnyStr, value: Object) -> Object: ...
    def putAll(self, map: Map) -> None: ...
    def remove(self, key: Object) -> Object: ...
    def size(self) -> int: ...
    def toBsonDocument(
        self, documentClass: Class, codecRegistry: CodecRegistry
    ) -> BsonDocument: ...
    def toJson(self, *args: Any) -> AnyStr: ...
    def values(self) -> Collection: ...
