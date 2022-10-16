from typing import Any, Dict, List, Optional, Set, TypeVar, Union

from java.lang import Object, String
from java.time import Instant, ZoneId
from java.util.function import (
    Consumer,
    Function,
    Predicate,
    Supplier,
    ToDoubleFunction,
    ToIntFunction,
    ToLongFunction,
)

E = TypeVar("E")
T = TypeVar("T")

class Collection:
    def add(self, e: E) -> bool: ...
    def addAll(self, c: Collection) -> bool: ...
    def clear(self) -> None: ...
    def contains(self, o: Object) -> bool: ...
    def containsAll(self, c: Collection) -> bool: ...
    def equals(self, o: Object) -> bool: ...
    def hashCode(self) -> int: ...
    def isEmpty(self) -> bool: ...
    def iterator(self) -> Iterator: ...
    def parallelStream(self) -> Stream: ...
    def remove(self, o: Object) -> bool: ...
    def removeAll(self, c: Collection) -> bool: ...
    def removeIf(self, filter: Predicate) -> bool: ...
    def retainAll(self, v: Collection) -> bool: ...
    def size(self) -> int: ...
    def spliterator(self) -> Spliterator: ...
    def stream(self) -> Stream: ...
    def toArray(self, arg: Optional[Any] = ...) -> List[Object]: ...

class Comparator:
    def compare(self, o1: T, o2: T) -> int: ...
    @staticmethod
    def comparing(keyExtractor: Function, keyComparator: Comparator) -> Comparator: ...
    @staticmethod
    def comparingDouble(keyExtractor: ToDoubleFunction) -> Comparator: ...
    @staticmethod
    def comparingInt(keyExtractor: ToIntFunction) -> Comparator: ...
    @staticmethod
    def comparingLong(keyExtractor: ToLongFunction) -> Comparator: ...
    def equals(self, obj: Object) -> bool: ...
    @staticmethod
    def naturalOrder() -> Comparator: ...
    @staticmethod
    def nullsFirst(comparator: Comparator) -> Comparator: ...
    @staticmethod
    def nullsLast(comparator: Comparator) -> Comparator: ...
    def reversed(self) -> Comparator: ...
    @staticmethod
    def reverseOrder() -> Comparator: ...
    def thenComparing(self, *args: Any) -> Comparator: ...
    def thenComparingDouble(self, keyExtractor: ToDoubleFunction) -> Comparator: ...
    def thenComparingInt(self, keyExtractor: ToIntFunction) -> Comparator: ...
    def thenComparingLong(self, keyExtractor: ToLongFunction) -> Comparator: ...

class Iterator:
    def forEachRemaining(self, action: Consumer) -> None: ...
    def hasNext(self) -> bool: ...
    def next(self) -> E: ...
    def remove(self) -> bool: ...

class ListIterator(Iterator):
    def add(self, e: E) -> None: ...
    def hasNext(self) -> bool: ...
    def hasPrevious(self) -> bool: ...
    def next(self) -> E: ...
    def nextIndex(self) -> int: ...
    def previous(self) -> E: ...
    def previousIndex(self) -> int: ...
    def set(self, e: E) -> None: ...

class Spliterator:
    CONCURRENT: int
    DISTINCT: int
    IMMUTABLE: int
    NONNULL: int
    ORDERED: int
    SIZED: int
    SORTED: int
    SUBSIZED: int
    def characteristics(self) -> int: ...
    def estimateSize(self) -> long: ...
    def forEachRemaining(self, action: Consumer) -> None: ...
    def getComparator(self) -> Comparator: ...
    def getExactSizeIfKnown(self) -> long: ...
    def hasCharacteristics(self, characteristics: int) -> bool: ...
    def tryAdvance(self, action: Consumer) -> bool: ...
    def trySplit(self) -> Spliterator: ...

class Stream:
    @staticmethod
    def builder() -> Builder: ...
    @staticmethod
    def concat(a: Stream, b: Stream) -> Stream: ...
    @staticmethod
    def empty() -> Stream: ...
    @staticmethod
    def generate(s: Supplier) -> Stream: ...
    @staticmethod
    def iterate(*args: Any) -> Stream: ...
    @staticmethod
    def of(*args: T) -> Stream: ...
    @staticmethod
    def ofNullable(t: T) -> Stream: ...

    class Builder(Consumer):
        def accept(self, t: T) -> None: ...
        def add(self, t: T) -> Stream.Builder: ...
        def build(self) -> Stream: ...

class Calendar(Object):
    ALL_STYLES: int
    AM: int
    AM_PM: int
    APRIL: int
    AUGUST: int
    DATE: int
    DAY_OF_MONTH: int
    DAY_OF_WEEK: int
    DAY_OF_WEEK_IN_MONTH: int
    DAY_OF_YEAR: int
    DECEMBER: int
    DST_OFFSET: int
    ERA: int
    FEBRUARY: int
    FIELD_COUNT: int
    FRIDAY: int
    HOUR: int
    HOUR_OF_DAY: int
    JANUARY: int
    JULY: int
    JUNE: int
    LONG: int
    LONG_FORMAT: int
    LONG_STANDALONE: int
    MARCH: int
    MAY: int
    MILLISECOND: int
    MINUTE: int
    MONDAY: int
    MONTH: int
    NARROW_FORMAT: int
    NARROW_STANDALONE: int
    NOVEMBER: int
    OCTOBER: int
    PM: int
    SATURDAY: int
    SECOND: int
    SEPTEMBER: int
    SHORT: int
    SHORT_FORMAT: int
    SHORT_STANDALONE: int
    SUNDAY: int
    THURSDAY: int
    TUESDAY: int
    UNDECIMBER: int
    WEDNESDAY: int
    WEEK_OF_MONTH: int
    WEEK_OF_YEAR: int
    YEAR: int
    ZONE_OFFSET: int
    def add(self, field: int, amount: int) -> None: ...
    def after(self, when: Object) -> bool: ...
    def before(self, when: Object) -> bool: ...
    def clear(self, field: Optional[int] = ...) -> None: ...
    def clone(self) -> Object: ...
    def compareTo(self, anotherCalendar: Calendar) -> int: ...
    def get(self, field: int) -> int: ...
    def getActualMaximum(self, field: int) -> int: ...
    def getActualMinimum(self, field: int) -> int: ...
    @staticmethod
    def getAvailableCalendarTypes() -> Set[String]: ...
    @staticmethod
    def getAvailableLocales() -> List[Locale]: ...
    def getCalendarType(self) -> String: ...
    def getDisplayName(self, field: int, style: int, locale: Locale) -> String: ...
    def getDisplayNames(
        self, field: int, style: int, locale: Locale
    ) -> Dict[String, int]: ...
    def getFirstDayOfWeek(self) -> int: ...
    def getGreatestMinimum(self, field: int) -> int: ...
    def getInstance(self, *args: Any) -> Calendar: ...
    def getTimeZone(self) -> TimeZone: ...
    def getWeeksInWeekYear(self) -> int: ...
    def getWeekYear(self) -> int: ...
    def isLenient(self) -> bool: ...
    def isSet(self, field: int) -> bool: ...
    def isWeekDateSUpported(self) -> bool: ...
    def roll(self, field: int, amount: int) -> None: ...
    def set(self, *args: int) -> None: ...
    def setFirstDayOfWeek(self, value: int) -> None: ...
    def setLenient(self, lenient: bool) -> None: ...
    def setMinimalDaysInFirstWeek(self, value: int) -> None: ...
    def setTime(self, date: Date) -> None: ...
    def setTimeInMillis(self, millis: long) -> None: ...
    def setTimeZone(self, value: TimeZone) -> None: ...
    def setWeekDate(self, weekYear: int, weekOfYear: int, dayOfWeek: int) -> None: ...
    def toInstant(self) -> Instant: ...

class Currency(Object):
    @staticmethod
    def getAvailableCurrencies() -> Set[Currency]: ...
    def getCurrencyCode(self) -> String: ...
    def getDisplayName(self, locale: Optional[Locale] = ...) -> String: ...
    @staticmethod
    def getInstance(arg: Union[Locale, String]) -> Currency: ...
    def getNumericCode(self) -> int: ...
    def getNumericCodeAsString(self) -> String: ...
    def getSymbol(self, locale: Optional[Locale] = ...) -> String: ...

class Date(Object):
    def __init__(self, date: Optional[long] = ...) -> None: ...
    def after(self, when: Date) -> bool: ...
    def before(self, when: Date) -> bool: ...
    def compareTo(self, anotherDate: Date) -> int: ...
    def getTime(self) -> long: ...
    def setTime(self, time: long) -> None: ...

class EventObject(Object):
    def __init__(self, source: Object) -> None: ...
    def getSource(self) -> Object: ...

class Locale(Object):
    country: Optional[str]
    language: str
    variant: Optional[str]
    def __init__(
        self, language: str, country: Optional[str] = ..., variant: Optional[str] = ...
    ) -> None: ...
    def CANADA(self) -> Locale: ...
    def CANADA_FRENCH(self) -> Locale: ...
    def CHINA(self) -> Locale: ...
    def CHINESE(self) -> Locale: ...
    def ENGLISH(self) -> Locale: ...
    def FRANCE(self) -> Locale: ...
    def FRENCH(self) -> Locale: ...
    def GERMAN(self) -> Locale: ...
    def GERMANY(self) -> Locale: ...
    def ITALIAN(self) -> Locale: ...
    def ITALY(self) -> Locale: ...
    def JAPAN(self) -> Locale: ...
    def JAPANESE(self) -> Locale: ...
    def KOREA(self) -> Locale: ...
    def KOREAN(self) -> Locale: ...
    def PRC(self) -> Locale: ...
    def SIMPLIFIED_CHINESE(self) -> Locale: ...
    def TAIWAN(self) -> Locale: ...
    def TRADITIONAL_CHINESE(self) -> Locale: ...
    def UK(self) -> Locale: ...
    def US(self) -> Locale: ...

class TimeZone(Object):
    LONG: int
    SHORT: int
    def clone(self) -> Object: ...
    @staticmethod
    def getAvailableIDs(rawOffset: Optional[int] = ...) -> List[String]: ...
    @staticmethod
    def getDefault() -> TimeZone: ...
    def getDisplayName(self, *args: Any) -> String: ...
    def getDSTSavings(self) -> int: ...
    def getID(self) -> String: ...
    def getOffset(self, *args: Any) -> int: ...
    def getRawOffset(self) -> int: ...
    @staticmethod
    def getTimeZone(arg: Union[String, ZoneId]) -> TimeZone: ...
    def hasSameRules(self, other: TimeZone) -> bool: ...
    def isDaylightTime(self, date: Date) -> bool: ...
    def observesDaylightTime(self) -> bool: ...
    @staticmethod
    def setDefault(zone: TimeZone) -> None: ...
    def setID(self, ID: String) -> None: ...
    def setRawOffset(self, offsetMillis: int) -> None: ...
    def toZoneId(self) -> ZoneId: ...
    def useDaylightTime(self) -> bool: ...

class UUID(Object):
    def __init__(self, mostSigBits: long, leastSigBits: long) -> None: ...
    def clockSequence(self) -> int: ...
    def compareTo(self, val: UUID) -> int: ...
    @staticmethod
    def fromString(name: String) -> UUID: ...
    def getLeastSignificantBits(self) -> long: ...
    def getMostSignificantBits(self) -> long: ...
    @staticmethod
    def nameUUIDFromBytes(name: bytearray) -> UUID: ...
    def node(self) -> long: ...
    @staticmethod
    def randomUUID() -> UUID: ...
    def timestamp(self) -> long: ...
    def variant(self) -> int: ...
    def version(self) -> int: ...
