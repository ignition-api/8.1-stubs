from typing import Mapping

from dev.coatl.helper.types import AnyStr

class ScriptFunctionHint:
    def getAutocompleteText(self) -> AnyStr: ...
    def getMethodDescription(self) -> AnyStr: ...
    def getMethodSignature(self) -> AnyStr: ...
    def getParameterDescriptions(self) -> Mapping[AnyStr, AnyStr]: ...
    def getReturnValueDescription(self) -> AnyStr: ...
