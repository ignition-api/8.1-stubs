from typing import Dict, List

from com.inductiveautomation.ignition.alarming.common.rosters import RosterModel
from com.inductiveautomation.ignition.common.user import PyUser
from java.lang import String

def addUsers(rosterName: String, users: List[PyUser]) -> None: ...
def createRoster(name: String, description: String) -> None: ...
def deleteRoster(rosterName: String) -> None: ...
def getRoster(name: String) -> RosterModel: ...
def getRosterNames() -> List[String]: ...
def getRosters() -> Dict[String, List[String]]: ...
def removeUsers(rosterName: String, users: List[PyUser]) -> None: ...
