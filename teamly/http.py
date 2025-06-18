import aiohttp
import asyncio
import yarl

from typing import ClassVar

'''The Route class takes the base URL from the Teamly API
 and appends the extra path required by the program.'''
class Route:
    BASE: ClassVar[str] = "https://api.teamly.one/api/v1"

    def __init__(self, method: str, path: str):
        self.path: str = path
        self.method: str = method



class HTTPClient:
    
    def __init__(self):
        self._session: aiohttp.ClientSession = None
        self.token: str = None
        self.ws_url: str | yarl.URL = "https://api.teamly.one/api/v1"

    async def ws_connect(self, url: str):
        return await self._session.ws_connect(self.ws_url)