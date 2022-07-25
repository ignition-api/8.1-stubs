from typing import Optional

from java.lang import Object
from org.python.core import PyObject

class PyJsonObjectAdapter(Object):
    def __init__(self, obj) -> None: ...
    def __delitem__(self, key) -> None: ...
    def __findattr_ex__(self, name) -> None: ...
    def __finditem__(self, key) -> None: ...
    def __iter__(self): ...
    def __len__(self) -> None: ...
    def __setitem__(self, key, value) -> None: ...
    def clear(self) -> None: ...
    def get(self, key: PyObject, default: Optional[PyObject] = ...) -> PyObject: ...
    def has_key(self, key) -> None: ...
    def items(self) -> None: ...
    def iteritems(self) -> None: ...
    def iterkeys(self) -> None: ...
    def itervalues(self) -> None: ...
    def keys(self) -> None: ...
    def pop(self, key) -> None: ...
    def popitem(self) -> None: ...
    def setdefault(self, key, default) -> None: ...
    def update(self, *args, **kwargs) -> None: ...
    def values(self) -> None: ...
