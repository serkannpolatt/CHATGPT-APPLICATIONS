import asyncio
import json
import websockets
from datetime import datetime

async def live_price():
    async with websockets.connect( 'wss://stream.binance.com:9443/ws/btcusdt@ticker') as websocket:        
        while True:
            response = json. loads (await websocket.recv())
            timestamp = datetime.fromtimestamp (response ["E"] / 1000).strftime('%Y-%m-%d %H:%M: %S')
            print (f"{timestamp} Close price: {response ['c']}")

asyncio.get_event_loop().run_until_complete (live_price())