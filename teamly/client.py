import asyncio
from .http import HTTPClient
from .gateway import TeamlyWebSocket
from typing import List, Dict, Any, Coroutine, Callable, TypeVar

T = TypeVar('T')
Coro = Coroutine[Any, Any, T]
CoroT = TypeVar('CoroT', bound=Callable[..., Coro[Any]])

class Client:

    def __init__(self):
        self.http = HTTPClient()

    async def start(self,token):
        await self.http.static_login(token)

    def run(self,token: str):
        
        async def runner():
            async with self:
                await self.start(token)

        try:
            asyncio.run(runner())
        except KeyboardInterrupt:
            pass

    async def __aenter__(self):
        return self

    async def __aexit__(self,exc_type, exc_value, traceback):
        await self.close()


    async def connect(self, token: str):
        pass

    async def close(self):
        await self.http.close()


    








            
            
    