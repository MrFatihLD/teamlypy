import asyncio
import aiohttp
import logging

from .http import HTTPClient

from typing import Coroutine, Callable, TypeVar, Any

_log = logging.getLogger(__name__)

T = TypeVar('T') # 'T' Herhangi bit tipi temsil eder
Coro = Coroutine[Any,Any,T] #asenkron bir fonksiyonu temsil eder
CoroT = TypeVar('CoroT', bound = Callable[..., Coro[Any]]) # Coroutine döndüren herhangi bir fonksiyon tipi

class Client:

    def __init__(self):
        self.token = None
        self.http = HTTPClient()

    def run(self, token: str):
        _log.debug("started \"run()\"") #Debug

        async def runner():
            _log.debug("started \"runner()\"") #Debug
            async with self:
                await self.start()

        _log.debug("running \"asyncio.run(runner())\"") #Debug
        try:
            asyncio.run(runner())
        except KeyboardInterrupt:
            pass        

    async def start(self):
        _log.debug("Started \"start()\"...") #Debug
        await self.http.static_login(self.token)
        await self.test_request()

    async def close(self):
        await self.http.close()

    async def test_request(self):
        await self.http.test_request()









    async def __aenter__(self):
        pass

    async def __aexit__(
            self, 
            exc_type, 
            exc_val, 
            exc_tb
    ):
        _log.debug("closing HTTP client...")
        await self.http.close()