from typing import Any

class EqualityDelegate:
    def eq(self, foo: Any, bar: Any) -> bool: ...
    def hash(self, foo: Any) -> int: ...
