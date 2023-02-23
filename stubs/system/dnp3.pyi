from typing import List, Optional, Union

from dev.thecesrom.helper.types import AnyStr

Number = Union[float, int]
NUL: int
PULSE_ON: int
PULSE_OFF: int
LATCH_ON: int
LATCH_OFF: int
CLOSE: int
TRIP: int

def directOperateAnalog(
    deviceName: AnyStr, index: int, value: Number, variation: Optional[int] = ...
) -> int: ...
def directOperateBinary(
    deviceName: AnyStr,
    indexes: List[int],
    opType: int,
    tcCode: Optional[int] = ...,
    count: Optional[int] = ...,
    onTime: Optional[int] = ...,
    offTime: Optional[int] = ...,
) -> int: ...
def freezeAnalogs(deviceName: AnyStr, indexes: List[int]) -> None: ...
def freezeAnalogsAtTime(
    deviceName: AnyStr, absoluteTime: int, intervalTime: int, indexes: List[int]
) -> None: ...
def freezeCounters(deviceName: AnyStr, indexes: List[int]) -> None: ...
def freezeCountersAtTime(
    deviceName: AnyStr, absoluteTime: int, intervalTime: int, indexes: List[int]
) -> None: ...
def selectOperateAnalog(
    deviceName: AnyStr, index: int, value: Number, variation: Optional[int] = ...
) -> int: ...
def selectOperateBinary(
    deviceName: AnyStr,
    indexes: List[int],
    opType: int,
    tcCode: Optional[int] = ...,
    count: Optional[int] = ...,
    onTime: Optional[int] = ...,
    offTime: Optional[int] = ...,
) -> int: ...
