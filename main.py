import asyncio
import time
from package import dm, send_message
from package.utile import get_name, get_live

"""
需要 aiohttp 模块进行 WebSocket 连接
弹幕数据解析参考了 https://github.com/xfgryujk/blivedm 的代码

room_list
    type: list
    直播间id，整数型

提醒方式：
    1. Telegram
    2. Server酱（通过微信提醒）【http://sc.ftqq.com/3.version】

  Telegram：
    tg: 启用则 True，否则 False
    tg_token: 你的 Bot 的 token
    tg_id: 你的tg账号的 id

  Server酱：
    sc: 启用则 True，否则 False
    sc_token: 你的 SCKEY
"""


room_list = [  # 房间ID，每个ID用 英文逗号 隔开
    5946727
]

tg = False  # 是否使用 Telegram 通知
sc = True  # 是否使用 Server酱 通知
tg_token = ''  # Telegram机器人 的 Token
tg_id = ''  # Telegram账号 的 ID
sc_token = 'SCT12142TNb7NEiqiyWkGNCNUyo7zFCpp'  # Server酱 的 Token

ssl = None  # SSL

room_result = {}
tasks = []


async def get_message(queue):
    k = 0
    s_m = send_message.SessionAio(tg_token=tg_token, tg_id=tg_id, sc_token=sc_token, loop=loop)
    while True:
        status, room_id, live, uid = await get_live(room_id=21756924)
        print(live)
        print(k)
        if live == 1 and k == 0:
            await s_m.send(tg=tg, sc=True, sc_title="【雪绘yukie】开播啦！", text=k)
            print('kkkkkk3')
            k = 1
        if live == 2 or live == 0:
            k = 0
        time.sleep(4)
        print('kkkkkkkkkkkbbbbbbbbbbb33')

if __name__ == '__main__':
    q = asyncio.Queue()
    loop = asyncio.get_event_loop()
    tasks.append(asyncio.ensure_future(get_message(queue=q)))
    loop.run_until_complete(asyncio.wait(tasks))
