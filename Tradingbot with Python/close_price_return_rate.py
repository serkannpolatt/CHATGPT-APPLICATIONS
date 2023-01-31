import asyncio
import json
import websockets
from datetime import datetime
async def live_price():
    previous_price = None
    async with websockets.connect('wss://stream.binance.com: 9443/ws/btcusdt@ticker') as websocket:
        while True:
            response = json. loads (await websocket.recv())
            timestamp = datetime.fromtimestamp (response ["E"]/1000).strftime('%Y-%m-%d %H:%M: %S')
            close_price = float(response ['c'])
            if previous_price:
                return_rate= (close_price - previous_price) / previous_price* 100
                print (f"{timestamp} - Close price: {close_price} Return Rate: {return_rate} %")
            else:
                print (f"{timestamp} - Close price: {close_price}")
            previous_price = close_price
asyncio.get_event_loop().run_until_complete(live_price())