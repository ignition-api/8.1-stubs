from typing import Dict, Optional, Set, Union

from dev.coatl.helper.types import AnyStr
from java.lang import Object
from java.nio import ByteBuffer, CharBuffer
from java.util import Locale

class Charset(Object):
    def aliases(self) -> Set[AnyStr]: ...
    @staticmethod
    def availableCharsets() -> Dict[AnyStr, Charset]: ...
    def canEncode(self) -> bool: ...
    def compareTo(self, that: Charset) -> int: ...
    def contains(self, cs: Charset) -> bool: ...
    def decode(self, bb: ByteBuffer) -> CharBuffer: ...
    @staticmethod
    def defaultCharset() -> Charset: ...
    def displayName(self, locale: Optional[Locale]) -> AnyStr: ...
    def encode(self, arg: Union[Charset, AnyStr]) -> ByteBuffer: ...
    @staticmethod
    def forName(charsetName: AnyStr) -> Charset: ...
    def isRegistered(self) -> bool: ...
    @staticmethod
    def isSupported(charsetName: AnyStr) -> bool: ...
    def name(self) -> AnyStr: ...
    def newDecoder(self) -> CharsetDecoder: ...
    def newEncoder(self) -> CharsetEncoder: ...

class CharsetDecoder(Object):
    def charset(self) -> Charset: ...
    def decode(
        self,
        in_: ByteBuffer,
        out: Optional[CharBuffer] = ...,
        endOfInput: Optional[bool] = ...,
    ) -> CharBuffer: ...

class CharsetEncoder(Object):
    def charset(self) -> Charset: ...
    def encode(
        self,
        in_: ByteBuffer,
        out: Optional[ByteBuffer] = ...,
        endOfInput: Optional[bool] = ...,
    ) -> Union[ByteBuffer, CoderResult]: ...

class CoderResult(Object):
    OVERFLOW: CoderResult
    UNDERFLOW: CoderResult
    def isError(self) -> bool: ...
    def isMalformed(self) -> bool: ...
    def isOverflow(self) -> bool: ...
    def isUnderFlow(self) -> bool: ...
    def isUnmappable(self) -> bool: ...
    def length(self) -> int: ...
    @staticmethod
    def malformedForLength(length: int) -> CoderResult: ...
    def throwException(self) -> None: ...
    @staticmethod
    def unmappableForLength(length: int) -> CoderResult: ...
