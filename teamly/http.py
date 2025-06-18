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
        self.__session: aiohttp.ClientSession = None
        self.token: str = None
        self.ws_url: str | yarl.URL = "https://api.teamly.one/api/v1"

    #function to connect to WebSocket
    async def ws_connect(self, url: str) -> aiohttp.ClientWebSocketResponse:
        kwargs = {
            "timeout": 30,
            "autoclose": False,
            "headers": {
                "Authorization": "Bot " + self.token
            }
        }
        return await self.__session.ws_connect(self.ws_url, **kwargs)
    
    #function to login to ClientSession
    async def static_login(self, token: str):
        pass
    
    #function will close the session
    async def close(self):
        if self.__session:
            await self.__session.close()
    
