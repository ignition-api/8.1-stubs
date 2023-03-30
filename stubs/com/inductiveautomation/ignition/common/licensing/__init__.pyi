from typing import Iterable, List

from dev.thecesrom.helper.types import AnyStr as AnyStr
from java.lang import Enum, Object
from java.util import Date

class LicenseDetails:
    def checkFlag(self, key: AnyStr) -> bool: ...
    def getExpirationDate(self) -> Date: ...
    def getLicenseDetail(self, key: AnyStr) -> AnyStr: ...
    def getLicenseDetails(self, key: AnyStr) -> List[LicenseRestriction]: ...
    def getModuleId(self) -> AnyStr: ...
    def getVersion(self) -> int: ...
    def isPlatformDetails(self) -> bool: ...

class LicenseState:
    def getLicenseMode(self) -> LicenseMode: ...
    def getModuleLicense(self) -> ModuleLicense: ...
    def getPlatformLicense(self) -> LicenseDetails: ...
    def getTrialExpirationDate(self) -> Date: ...
    def isTrialExpired(self) -> bool: ...

class LicenseMode(Enum):
    @staticmethod
    def values() -> Iterable[LicenseMode]: ...

class LicenseRestriction(Object):
    def __init__(self, restrictionName: AnyStr, restrictionValue: AnyStr) -> None: ...
    def getrestrictionName(self) -> AnyStr: ...
    def getrestrictionValue(self) -> AnyStr: ...

class ModuleLicense(LicenseDetails):
    def getLicenseDetail(self, key: AnyStr) -> AnyStr: ...
    def getLicenseDetails(self, key: AnyStr) -> List[LicenseRestriction]: ...
    def getModuleId(self) -> AnyStr: ...
    def getVersion(self) -> int: ...
