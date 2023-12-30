from typing import Any, Optional

from com.inductiveautomation.ignition.common.gson import Gson
from dev.coatl.helper.types import AnyStr
from java.lang import Object
from java.net import CookieManager as JCookieManager
from java.net.http import HttpClient, HttpResponse
from java.nio.charset import Charset
from java.util.concurrent import CompletableFuture
from org.python.core import PyObject

class CookieManager(JCookieManager):
    def __init__(self, *args: Any) -> None: ...

class JythonHttpClient(Object):
    def delete(self, *args: PyObject, **kwargs: AnyStr) -> Response: ...
    def deleteAsync(self, *args: PyObject, **kwargs: AnyStr) -> Promise: ...
    def get(self, *args: PyObject, **kwargs: AnyStr) -> Response: ...
    def getAsync(self, *args: PyObject, **kwargs: AnyStr) -> Promise: ...
    def getConnectTimeout(self) -> long: ...
    def getCookieManager(self) -> CookieManager: ...
    def getJavaClient(self) -> HttpClient: ...
    def getRedirectPolicy(self) -> AnyStr: ...
    def getVersion(self) -> AnyStr: ...
    def head(self, *args: PyObject, **kwargs: AnyStr) -> Response: ...
    def headAsync(self, *args: PyObject, **kwargs: AnyStr) -> Promise: ...
    def options(self, *args: PyObject, **kwargs: AnyStr) -> Response: ...
    def optionsAsync(self, *args: PyObject, **kwargs: AnyStr) -> Promise: ...
    def parseChart(self, contentType: AnyStr) -> Optional[Charset]: ...
    def patch(self, *args: PyObject, **kwargs: AnyStr) -> Response: ...
    def patchAsync(self, *args: PyObject, **kwargs: AnyStr) -> Promise: ...
    def post(self, *args: PyObject, **kwargs: AnyStr) -> Response: ...
    def postAsync(self, *args: PyObject, **kwargs: AnyStr) -> Promise: ...
    def put(self, *args: PyObject, **kwargs: AnyStr) -> Response: ...
    def putAsync(self, *args: PyObject, **kwargs: AnyStr) -> Promise: ...
    def request(self, *args: PyObject, **kwargs: AnyStr) -> Response: ...
    def requestAsync(self, *args: PyObject, **kwargs: AnyStr) -> Promise: ...
    def setGson(self, gson: Gson) -> None: ...
    def trace(self, *args: PyObject, **kwargs: AnyStr) -> Response: ...
    def traceAsync(self, *args: PyObject, **kwargs: AnyStr) -> Promise: ...

class Promise(Object):
    def cancel(self) -> bool: ...
    def get(self, *args: PyObject, **kwargs: AnyStr) -> Any: ...
    def getFuture(self) -> CompletableFuture: ...
    def handleException(self, callback: PyObject) -> Promise: ...
    def isDone(self) -> bool: ...
    def then(self, callback: PyObject) -> Promise: ...
    def whenComplete(self, callback: PyObject) -> None: ...

class Response(Object):
    def __init__(self, httResponse: HttpResponse, client: JythonHttpClient) -> None: ...
