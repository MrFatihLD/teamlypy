import aiohttp
import asyncio
import yarl
from teamly.utils import MISSING

from typing import ClassVar, Optional

'''The Route class takes the base URL from the Teamly API
 and appends the extra path required by the program.'''
class Route:
    BASE: ClassVar[str] = "https://api.teamly.one/api/v1"

    def __init__(self, method: str, path: str):
        self.path: str = path
        self.method: str = method



class HTTPClient:
    
    def __init__(
            self,
            loop: asyncio.AbstractEventLoop = None, # temporaly None
            connector: Optional[aiohttp.BaseConnector] = None,
            *,
            proxy: Optional[str] = None,
            proxy_auth: Optional[aiohttp.BasicAuth] = None,
            #unsync_clock: bool = True,
            http_trace: Optional[aiohttp.TraceConfig] = None,
            #max_ratelimit_timeout: Optional[float] = None
        ):
        self.loop: asyncio.AbstractEventLoop = loop
        self.connector: Optional[aiohttp.BaseConnector] = connector or MISSING
        self.proxy: Optional[str] = proxy
        self.proxy_auth: Optional[aiohttp.BasicAuth] = proxy_auth
        self.http_trace: Optional[aiohttp.TraceConfig] = http_trace

        self.__session: aiohttp.ClientSession = MISSING


        self.token: str = None
        self.ws_url: str = "https://api.teamly.one/api/v1"

    #function to connect to WebSocket
    async def ws_connect(self, url: str) -> aiohttp.ClientWebSocketResponse:
        kwargs = {
            "proxy": self.proxy,
            "proxy_auth": self.proxy_auth,
            "timeout": 30,
            "autoclose": False,
            "headers": {
                "Authorization": "Bot " + self.token
            }
        }
        return await self.__session.ws_connect(self.ws_url, **kwargs)
    
    #function to login to ClientSession
    async def static_login(self, token: str):
        if self.connector is MISSING:
            self.connector = aiohttp.TCPConnector(limit=0)

        self.__session = aiohttp.ClientSession(
            connector = self.connector,
            trace_configs = None if self.http_trace is None else self.http_trace
        )
    
    #function will close the session
    async def close(self):
        if self.__session:
            await self.__session.close()
    
