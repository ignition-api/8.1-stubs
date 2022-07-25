from typing import Any, List, Sequence, TypeVar, Union

from java.beans import PropertyChangeListener
from java.lang import Class, Object, String

T = TypeVar("T")

class Property:
    def getDefaultValue(self) -> T: ...
    def getName(self) -> String: ...
    def getType(self) -> Class: ...

class PropertySet:
    @staticmethod
    def builder() -> BasicPropertySet.Builder: ...
    def extend(self, parent: PropertySet) -> PropertySet: ...
    def isExtended(self, prop: Property) -> bool: ...
    def newDefaultInstance(self) -> PropertySet: ...
    def newExtension(self) -> PropertySet: ...

class BasicProperty(Property, Object):
    def __init__(self, *args) -> None: ...
    def getClazz(self) -> Class: ...
    def getDefaultValue(self) -> T: ...
    def getName(self) -> String: ...
    def getType(self) -> Class: ...
    def setClazz(self, clazz: Class) -> None: ...
    def setClazz_(self, clazz: Class) -> BasicProperty: ...
    def setDefaultValue(self, defaultValue: Any) -> None: ...
    def setDefaultValue_(self, defaultValue: Any) -> BasicProperty: ...
    def setName(self, name: String) -> None: ...
    def setName_(self, name: String) -> BasicProperty: ...

class BasicPropertySet(Object):
    def __init__(self, *args: Any) -> None: ...
    def addPropertySet(self, *args: Any) -> None: ...
    def contains(self, prop: Property) -> bool: ...
    def get(self, prop: Property) -> T: ...
    def getCount(self) -> int: ...
    def getExtension(self) -> PropertySet: ...
    def getOrDefault(self, prop: Property) -> T: ...
    def getOrElse(self, prop: Property, value: T) -> T: ...
    def getProperties(self) -> List[Property]: ...
    def getRawValueMap(self) -> Any: ...
    def getValues(self) -> List[PropertyValue]: ...
    def isExtended(self, prop: Property) -> bool: ...
    def isInherited(self, prop: Property) -> bool: ...
    def iterator(self) -> Sequence[PropertyValue]: ...
    @staticmethod
    def of(*args: PropertyValue) -> PropertySet: ...
    def remove(self, prop: Property) -> None: ...
    def removePropertyChangeListener(
        self, listener: PropertyChangeListener
    ) -> None: ...
    def set(self, prop: Union[Property, PropertyValue], value: T) -> None: ...
    def setDirect(self, prop: Property, value: Object) -> None: ...
    def setRawValueMap(self, copy: Any) -> None: ...

    class Builder(Object):
        def build(self) -> BasicPropertySet: ...
        def set(self, prop: Property, value: T) -> BasicPropertySet.Builder: ...

class PropertyValue(Object):
    def __init__(self, *args: Any) -> None: ...
    def getProperty(self) -> Property: ...
    def getValue(self) -> Object: ...
    @staticmethod
    def of(prop: Property, value: Object) -> PropertyValue: ...
