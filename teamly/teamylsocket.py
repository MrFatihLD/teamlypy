import asyncio
import websockets
import json

class TeamlySocketClient:
    def __init__(self):
        self.ws_url = "wss://api.teamly.one/api/v1/ws"
        self.websocket = None

    async def connect(self, token: str):
        print("🔌 Bağlantı kuruluyor...")
        self.websocket = await websockets.connect(
            self.ws_url,
            additional_headers = {"Authorization": f"Bot {token}"}
        )

        print("🟢 WebSocket bağlantısı kuruldu.")
        await self.listen()

    async def close(self):
        print("Closing WebsocketClient...")
        await self.websocket.close()

    async def listen(self):
        try:
            async for message in self.websocket:
                data = json.loads(message)
                print("📨 Event geldi:", json.dumps(data,indent=4))
        except websockets.ConnectionClosed as e:
            print("🔴 Bağlantı kapandı:", e)

    # async def keepalive(self):
    #     while self._running:
    #         keepalive_msg = json.dumps({"t": "keepalive"})
    #         await self.websocket.send(keepalive_msg)
    #         print("🔄 Keepalive gönderildi")
    #         await asyncio.sleep(25)

    async def run(self):
        await self.connect()