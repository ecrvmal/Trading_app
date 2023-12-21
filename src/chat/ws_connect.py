import aiohttp
import time
import asyncio

# User Manual WebSocket on python (listening)
# run gunicorn src/main:app --reload
# run  python ws_connect.py
# web browser: http://127.0.0.1:8000/pages/chat    send 123
#  ws_connect prints to file and to console.

async def main():
    async with aiohttp.ClientSession() as session:
        client_id = int(time.time() * 1000)
        async with session.ws_connect(f'http://localhost:8000/chat/ws/{client_id}') as ws:
            async for msg in ws:
                if msg.type == aiohttp.WSMsgType.TEXT:
                    print(f'msg_data: {msg.data}')
                    with open("ws_messages.txt", "a") as file:
                        file.write(f"{msg.data}\n")

asyncio.run(main())
