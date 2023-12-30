from typing import Any, Dict, Optional

from com.inductiveautomation.ignition.common import BasicDataset
from com.inductiveautomation.sfc.api import PyChartScope
from dev.coatl.helper.types import AnyStr

def cancelChart(instanceId: AnyStr) -> None: ...
def getRunningCharts(chartPath: Optional[AnyStr] = ...) -> BasicDataset: ...
def getVariables(instanceId: AnyStr) -> PyChartScope: ...
def pauseChart(instanceId: AnyStr) -> None: ...
def redundantCheckpoint(instanceId: AnyStr) -> None: ...
def resumeChart(instanceId: AnyStr) -> None: ...
def setVariable(
    instanceId: AnyStr, stepId: AnyStr, variableName: AnyStr, variableValue: Any
) -> None: ...
def setVariables(
    instanceId: AnyStr, stepId: AnyStr, variableMap: Dict[AnyStr, Any]
) -> None: ...
def startChart(
    projectName: AnyStr, chartPath: AnyStr, arguments: Dict[AnyStr, Any]
) -> AnyStr: ...
