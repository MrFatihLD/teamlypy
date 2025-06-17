import asyncio
from .http import HTTPClient

class Client:

    #initializing
    def __init__(self):
        self.http = HTTPClient()

    #HTTPClient ile oturum acar
    async def start(self,token):
        await self.connect()

    #Client'i calisiracak fonksiyon
    def run(self,token: str):
        print(f"{__name__}: got token (token: {token})") # Log

        async def runner():
            async with self:
                print(f"{__name__}: starting") # Log
                await self.start(token)

        try:
            print(f"{__name__}: running \"runner()\" function in asyncio") # Log
            asyncio.run(runner())
        except KeyboardInterrupt:
            pass

    async def __aenter__(self):
        return self

    async def __aexit__(self,exc_type, exc_value, traceback):
        print(f"{__name__}: calling the function http.close()") # Log
        await self.http.close()

    async def connect(self):

        await self.http.connect()

        #bu while loop bizim Client'in kapatana kadar hep acik kalmasini saglar
        while True:
            print("Client is running") # Log
            await asyncio.sleep(5)
    

    








            
            
    