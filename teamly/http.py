import aiohttp
import asyncio
import json
from teamly.utils import MISSING, TwoType

from typing import ClassVar, Optional, Any
from urllib.parse import quote

'''The Route class takes the base URL from the Teamly API
 and appends the extra path required by the program.'''
class Route:
    BASE: ClassVar[str] = "https://api.teamly.one/api/v1"

    def __init__(self, method: str, path: str, **parameters: Any):
        self.path: str = path
        self.method: str = method

        url = self.BASE + self.path
        if parameters:
            url = url.format_map({k: quote(v,safe="") if isinstance(v, str) else v for k, v in parameters.items()})
        self.url: str = url

        self.teamId: Optional[TwoType] = parameters.get("teamId")
        self.channelId: Optional[TwoType] = parameters.get("channeld")
        self.webhookId: Optional[TwoType] = parameters.get("webhookId")
        self.webhook_token: Optional[TwoType] = parameters.get("webhook_token")



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

        self.token = token
    
    #function will close the session
    async def close(self):
        if self.__session:
            await self.__session.close()

    async def request(
            self,
            route: Route,
            **kwargs
    ):
        method = route.method
        url = route.url

        response = await self.__session.request(method, url)
        print(json.dumps(response.text,indent=4))