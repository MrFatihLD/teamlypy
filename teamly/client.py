import asyncio
from .http import HTTPClient

class Client:

    def __init__(self):
        self.http = HTTPClient()

    #HTTPClient ile oturum acar
    async def start(self,token):
        await self.http.connect()

    #Client'i calisiracak fonksiyon
    def run(self,token: str):
        print(f"{__name__}: got token (token: {token})")

        async def runner():
            async with self:
                print(f"{__name__}: starting")
                await self.start(token)

        try:
            print(f"{__name__}: running \"runner()\" function in asyncio")
            asyncio.run(runner())
        except KeyboardInterrupt:
            pass

    async def __aenter__(self):
        return self

    async def __aexit__(self,exc_type, exc_value, traceback):
        print(f"{__name__}: calling the function http.close()")
        await self.http.close()

    