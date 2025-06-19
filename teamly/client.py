import asyncio
from .http import HTTPClient
from typing import Any, Coroutine, Callable, TypeVar

import logging
from teamly.utils import FormatLogging

T = TypeVar('T')
Coro = Coroutine[Any, Any, T]
CoroT = TypeVar('CoroT', bound=Callable[..., Coro[Any]])

_log = logging.getLogger(__name__)

class Client:

    def __init__(self):
        self.http = HTTPClient()

    async def start(self,token):
        _log.debug("starting static_token() function")
        await self.http.static_login(token)

    def run(self,token: str):
        _log.debug("running run() function")

        self.setup_logger(_log) #Logger setup
        
        async def runner():
            _log.debug("running runner() function")
            async with self:
                _log.debug("starting start() function")
                await self.start(token)

        try:
            _log.debug("Trying to run asyncio.run(runner())")
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
        _log.debug("http ClinetSession closed successfuly")





    async def setup_logger(log: logging.Logger):
        handle = logging.StreamHandler()
        handle.setFormatter(FormatLogging("%(levelname)s: %(message)s"))

        log.setLevel(level=logging.DEBUG)
        log.addHandler(handle)
        log.propagate = False


    








            
            
    