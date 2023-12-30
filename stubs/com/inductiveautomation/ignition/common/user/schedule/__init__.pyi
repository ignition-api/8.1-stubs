from typing import Iterable, List

from com.inductiveautomation.ignition.common.util import Timeline
from com.palantir.ptoss.cinch.core import DefaultBindableModel
from dev.coatl.helper.types import AnyStr
from java.lang import Enum
from java.util import Calendar, Date

class AbstractScheduleModel(DefaultBindableModel):
    def __init__(self) -> None: ...
    def getDescription(self) -> AnyStr: ...
    def getName(self) -> AnyStr: ...
    def getScheduleForDay(self, cal: Calendar) -> Timeline: ...
    def getType(self) -> AnyStr: ...
    def isObserveHolidays(self) -> bool: ...
    def setDescription(self, description: AnyStr) -> None: ...
    def setName(self, name: AnyStr) -> None: ...
    def setObserveHolidays(self, observeHolidays: bool) -> None: ...

class BasicScheduleModel(AbstractScheduleModel):
    def __init__(self) -> None: ...
    def getAllDayTime(self) -> AnyStr: ...
    def getFridayTime(self) -> AnyStr: ...
    def getMondayTime(self) -> AnyStr: ...
    def getRepeat(self) -> ScheduleRepeatStyle: ...
    def getRepeatOff(self) -> int: ...
    def getRepeatOn(self) -> int: ...
    def getSaturdayTime(self) -> AnyStr: ...
    def getScheduleForDay(self, cal: Calendar) -> Timeline: ...
    def getStartingAt(self) -> Date: ...
    def getSundayTime(self) -> AnyStr: ...
    def getThursdayTime(self) -> AnyStr: ...
    def getTuesdayTime(self) -> AnyStr: ...
    def getWednesdayTime(self) -> AnyStr: ...
    def getWeekDayTime(self) -> AnyStr: ...
    def isAllDays(self) -> bool: ...
    def isFriday(self) -> bool: ...
    def isMonday(self) -> bool: ...
    def isObserveHolidays(self) -> bool: ...
    def isRepeating(self) -> bool: ...
    def isSaturday(self) -> bool: ...
    def isSunday(self) -> bool: ...
    def isThursday(self) -> bool: ...
    def isTuesday(self) -> bool: ...
    def isUseDays(self) -> bool: ...
    def isWednesday(self) -> bool: ...
    def isWeekDays(self) -> bool: ...
    def set(self, that: BasicScheduleModel) -> None: ...
    def setAllDays(self, allDays: bool) -> None: ...
    def setAllDayTime(self, allDayTime: AnyStr) -> None: ...
    def setFriday(self, friday: bool) -> None: ...
    def setFridayTime(self, fridayTime: AnyStr) -> None: ...
    def setMonday(self, monday: bool) -> None: ...
    def setMondayTime(self, mondayTime: AnyStr) -> None: ...
    def setObserveHolidays(self, observeHolidays: bool) -> None: ...
    def setRepeat(self, repeat: ScheduleRepeatStyle) -> None: ...
    def setRepeatOff(self, repeatOff: int) -> None: ...
    def setRepeatOn(self, repeatOn: int) -> None: ...
    def setSaturday(self, saturday: bool) -> None: ...
    def setSaturdayTime(self, saturdayTime: AnyStr) -> None: ...
    def setStartingAt(self, startingAt: Date) -> None: ...
    def setSunday(self, sunday: bool) -> None: ...
    def setSundayTime(self, sundayTime: AnyStr) -> None: ...
    def setThursday(self, thursday: bool) -> None: ...
    def setThursdayTime(self, thursdayTime: AnyStr) -> None: ...
    def setTuesday(self, tuesday: bool) -> None: ...
    def setTuesdayTime(self, tuesdayTime: AnyStr) -> None: ...
    def setWednesday(self, wednesday: bool) -> None: ...
    def setWednesdayTime(self, wednesdayTime: AnyStr) -> None: ...
    def setWeekDays(self, weekDays: bool) -> None: ...
    def setWeekDayTime(self, weekDayTime: AnyStr) -> None: ...

class CompositeScheduleModel(AbstractScheduleModel):
    def __init__(self, models: List[AbstractScheduleModel]) -> None: ...
    def getModels(self) -> List[AbstractScheduleModel]: ...
    def getScheduleForDay(self, cal: Calendar) -> Timeline: ...
    def isObserveHolidays(self) -> bool: ...
    def setObserveHolidays(self, observeHolidays: bool) -> None: ...

class HolidayModel(DefaultBindableModel):
    date: Date
    name: AnyStr
    repeatAnnually: bool
    def __init__(self, name: AnyStr, date: Date, repeatAnnually: bool) -> None: ...
    def getDate(self) -> Date: ...
    def getName(self) -> AnyStr: ...
    def isRepeatAnnually(self) -> bool: ...
    def set(self, that: HolidayModel) -> None: ...
    def setDate(self, date: Date) -> None: ...
    def setName(self, name: AnyStr) -> None: ...
    def setRepeatAnnually(self, repeatAnnually: bool) -> None: ...

class ScheduleAdjustment(DefaultBindableModel):
    start: Date
    end: Date
    available: bool
    note: AnyStr
    def __init__(
        self, start: Date, end: Date, available: bool, note: AnyStr
    ) -> None: ...
    def contains(self, timestamp: long) -> bool: ...
    def getEnd(self) -> Date: ...
    def getNote(self) -> AnyStr: ...
    def getStart(self) -> Date: ...
    def isAvailable(self) -> bool: ...
    def setAvailable(self, available: bool) -> None: ...
    def setEnd(self, end: Date) -> None: ...
    def setNote(self, note: AnyStr) -> None: ...
    def setStart(self, start: Date) -> None: ...

class ScheduleRepeatStyle(Enum):
    @staticmethod
    def values() -> Iterable[ScheduleRepeatStyle]: ...
