from typing import Any, Dict, List, Optional

from dev.thecesrom.helper.types import AnyStr
from java.lang import Enum, Object
from java.time import Duration
from java.time.format import ResolverStyle
from java.util import Locale

class TemporalAccessor:
    def get(self, field: TemporalField) -> int: ...
    def getLong(self, field: TemporalField) -> long: ...
    def isSupported(self, field: TemporalField) -> bool: ...
    def query(self, query: TemporalQuery) -> Any: ...
    def range(self, field: TemporalField) -> ValueRange: ...

class TemporalAdjuster:
    def adjustInto(self, temporal: Temporal) -> Temporal: ...

class TemporalField:
    def adjustInto(self, temporal: Any, newValue: long) -> Temporal: ...
    def getBaseUnit(self) -> TemporalUnit: ...
    def getDisplayName(self, locale: Locale) -> AnyStr: ...
    def getFrom(self, temporal: TemporalAccessor) -> long: ...
    def getRangeUnit(self) -> TemporalUnit: ...
    def isDateBased(self) -> bool: ...
    def isSupportedBy(self, temporal: TemporalAccessor) -> bool: ...
    def isTimeBased(self) -> bool: ...
    def range(self) -> ValueRange: ...
    def rangeRefinedBy(self, temporal: TemporalAccessor) -> ValueRange: ...
    def resolve(
        self,
        fieldValues: Dict[TemporalField, long],
        partialTemporal: TemporalAccessor,
        resolverStyle: ResolverStyle,
    ) -> TemporalAccessor: ...
    def toString(self) -> AnyStr: ...

class TemporalQuery:
    def queryFrom(self, temporal: TemporalAccessor) -> Any: ...

class TemporalUnit:
    def addTo(self, temporal: Temporal, amount: long) -> Temporal: ...
    def between(
        self, temporal1Inclusive: Temporal, temporal2Exclusive: Temporal
    ) -> Temporal: ...
    def isSupportedBy(self, temporal: Temporal) -> bool: ...
    def getDuration(self) -> Duration: ...
    def isDateBased(self) -> bool: ...
    def isDurationEstimated(self) -> bool: ...
    def isTimeBased(self) -> bool: ...
    def toString(self) -> AnyStr: ...

class Temporal(TemporalAccessor):
    def minus(self, amount: long, unit: Optional[TemporalUnit] = ...) -> Temporal: ...
    def plus(self, amount: long, unit: Optional[TemporalUnit] = ...) -> Temporal: ...
    def until(self, endExclusive: Temporal, unit: TemporalUnit) -> long: ...

class ChronoUnit(Enum, TemporalUnit):
    CENTURIES: ChronoUnit
    DAYS: ChronoUnit
    DECADES: ChronoUnit
    ERAS: ChronoUnit
    FOREVER: ChronoUnit
    MICROS: ChronoUnit
    MILLENNIA: ChronoUnit
    MILLIS: ChronoUnit
    MINUTES: ChronoUnit
    MONTHS: ChronoUnit
    NANOS: ChronoUnit
    SECONDS: ChronoUnit
    HALF_DAYS: ChronoUnit
    HOURS: ChronoUnit
    WEEKS: ChronoUnit
    YEARS: ChronoUnit
    def addTo(self, temporal: Temporal, amount: long) -> Temporal: ...
    def between(
        self, temporal1Inclusive: Temporal, temporal2Exclusive: Temporal
    ) -> Temporal: ...
    def getDuration(self) -> Duration: ...
    def isDateBased(self) -> bool: ...
    def isDurationEstimated(self) -> bool: ...
    def isTimeBased(self) -> bool: ...
    @staticmethod
    def values() -> List[ChronoUnit]: ...

class ValueRange(Object):
    def checkValidIntValue(self, value: long, field: TemporalField) -> int: ...
    def checkValidValue(self, value: long, field: TemporalField) -> long: ...
    def getLargestMinimum(self) -> long: ...
    def getMaximum(self) -> long: ...
    def getMinimum(self) -> long: ...
    def getSmallestMaximum(self) -> long: ...
    def isFixed(self) -> bool: ...
    def isIntValue(self) -> bool: ...
    def isValidIntValue(self, value: long) -> bool: ...
    def isValidValue(self, value: long) -> bool: ...
    @staticmethod
    def of(*args: Any) -> ValueRange: ...
