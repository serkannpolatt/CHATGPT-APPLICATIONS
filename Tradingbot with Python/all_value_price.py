import asyncio
import json
import websockets
async def live_price():
        async with websockets.connect( 'wss://stream.binance.com: 9443/ws/btcusdt@ticker') as websocket:
            while True:
                response = json. loads (await websocket.recv())
                print (response)
asyncio.get_event_loop().run_until_complete(live_price())