import asyncio
from .http import HTTPClient
from .teamylsocket import TeamlySocketClient
from typing import List

class Client:

    #initializing
    def __init__(self):
        self.http = HTTPClient()
        self.socket = TeamlySocketClient()
        self.tasks: List[asyncio.Task] = []

    #HTTPClient ile oturum acar
    async def start(self,token):
        await self.connect(token)

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
        await self.close()


    async def connect(self, token: str):

        await self.http.connect()

        await self.add_task(self.socket.connect(token))
        await self.add_task(self.socket.keepalive())

        #bu while loop bizim Client'in kapatana kadar hep acik kalmasini saglar
        while True:
            print("Client is running") # Log
            await asyncio.sleep(5)

    async def close(self):
        print(f"\n{__name__}: calling the function http.close() & socket.close()") # Log

        await self.socket.close()
        await self.http.close()

        await self.cancel_tasks()
    
    async def add_task(self, task):
        task = asyncio.create_task(task)
        self.tasks.append(task)
        return task
    
    async def cancel_tasks(self):
        for task in self.tasks:
            task.cancel()

        await asyncio.gather(*self.tasks, return_exceptions=True)

    async def listen(self):
        pass

    








            
            
    