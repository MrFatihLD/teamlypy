import aiohttp

from colorama import Fore, init

init(autoreset=True)

class HTTPClient:

    def __init__(self):
        self.__session = None

    async def connect(self):
        self.__session = aiohttp.ClientSession(base_url="https://api.teamly.one/api/v1/")
        print(f"{__name__}: " + Fore.GREEN + "Client connected") # Log

    async def close(self):
        await self.__session.close()
        print(f"{__name__}: " + Fore.RED + "Client disconnected") # Log

