#ch09/09_02.py
import websockets
import asyncio
import json

async def upbit_ws_client():
    url = "wss://api.upbit.com/websocket/v1"
    async with websockets.connect(url) as websocket:
        subscribe_fmt = [
            {"tickest":"test",
             "codes":["KRW-BTC"],
             "isOnlyRealtime":True},
            {"format":"SIMPLE"}
        ]
        subscribe_data = json.dumps(subscribe_fmt)
        # 해당 데이터 구독신청
        await websocket.send(subscribe_data)
        # 무한루프로 실시간 데이터를 전달받고 이를 화면으로 표시
        while True:
            data = await websocket.recv()
            data = json.loads(data)
            print(data)
async def main():
    await upbit_ws_client()
asyncio.run(main())