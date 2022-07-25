from typing import Any, Dict, Optional

from com.inductiveautomation.ignition.common import BasicDataset
from java.lang import String

def addDevice(
    deviceType: String,
    deviceName: String,
    deviceProps: Dict[String, Any],
    description: Optional[String] = ...,
) -> None: ...
def getDeviceHostname(deviceName: String) -> String: ...
def listDevices() -> BasicDataset: ...
def refreshBrowse(deviceName: String) -> None: ...
def removeDevice(deviceName: String) -> None: ...
def restart(deviceName: String) -> None: ...
def setDeviceEnabled(deviceName: String, enabled: bool) -> None: ...
def setDeviceHostname(deviceName: String, hostname: String) -> None: ...
