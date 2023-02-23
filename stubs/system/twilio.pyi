from typing import List

from com.inductiveautomation.ignition.common import BasicDataset
from dev.thecesrom.helper.types import AnyStr

def getAccounts() -> List[AnyStr]: ...
def getAccountsDataset() -> BasicDataset: ...
def getPhoneNumbers(accountName: AnyStr) -> List[AnyStr]: ...
def getPhoneNumbersDataset(accountName: AnyStr) -> BasicDataset: ...
def sendSms(
    accountName: AnyStr, fromNumber: AnyStr, toNumber: AnyStr, message: AnyStr
) -> None: ...
