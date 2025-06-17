import asyncio
import websockets
import json

class TeamlySocketClient:
    def __init__(self):
        self.ws_url = "wss://api.teamly.one/api/v1/ws"
        self.websocket = None
        self._running = False

    async def connect(self, token: str, retries: int = 5, delay: int = 5):
        attempt = 0
        while attempt < retries:
            try:
                print("🔌 Bağlantı kuruluyor...")
                self.websocket = await websockets.connect(
                    self.ws_url,
                    additional_headers = {"Authorization": f"Bot {token}"}
                )

                self._running = True
                print("🟢 WebSocket bağlantısı kuruldu.")
                await self.listen()
                return
            except Exception as e:
                print(f"❌ Bağlantı hatası: {e}")
                attempt += 1
                print(f"⏳ {delay} saniye sonra yeniden deneniyor...")
                await asyncio.sleep(delay)

    async def close(self):
        self._running = False
        print("Closing WebsocketClient...")
        await self.websocket.close()

    async def listen(self):
        try:
            async for message in self.websocket:
                data = json.loads(message)
                print("📨 Event geldi:", json.dumps(data,indent=4))
        except websockets.ConnectionClosed as e:
            print("🔴 Bağlantı kapandı:", e)

    async def keepalive(self):
        await asyncio.sleep(25)
        while self._running:
            keepalive_msg = json.dumps({"t": "HEARTBEAT"})
            await self.websocket.send(keepalive_msg)
            print("🔄 Keepalive gönderildi")
            await asyncio.sleep(25)

    async def run(self):
        await self.connect()