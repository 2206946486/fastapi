#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time    : 2021/2/20 14:32
@Author  : LJ
@Site    : 
@File    : websockets.py
@Software: PyCharm
"""
import typing
from fastapi import FastAPI, WebSocket
from fastapi import APIRouter
import json
from starlette.endpoints import WebSocketEndpoint
import httpx
from tornado.httpclient import AsyncHTTPClient, HTTPRequest
from tornado.escape import json_encode, json_decode, url_escape

from app.tools.logger import logger


router = APIRouter()


# @router.websocket('/runcode')
# async def websocker_runcode(ws: WebSocket):
#     await ws.accept()
#     print("websocker opened!")
#     data = await ws.receive_text()
#     print(f'-------------------------data:{data}')
#     await ws.close()


@router.websocket('/runtest')
async def websocet_test(ws: WebSocket):
    # 等待连接
    await ws.accept()
    while True:
        data = await ws.receive_text()  # 接收消息
        data = json.loads(data)
        if data.get('state') == 0:
            break
        elif data.get('state') == 1:
            await ws.send_text(f"你对我说了: {data.get('msg')}, 然而我不想听！")
    await ws.close()


@router.websocket_route('/ws', name='ws')
class WebsocketTest(WebSocketEndpoint):

    async def on_connect(self, websocket: WebSocket) -> None:
        logger.info(f"打开websocket连接")
        await websocket.accept()

    async def on_receive(self, websocket: WebSocket, data: typing.Any) -> None:
        logger.info(f"收到消息{data}")
        data = json.loads(data)
        state = data.get("state")
        if state == 0:
            await websocket.send_text(f"最后一次给你发送消息")
            await websocket.close()
        else:
            await websocket.send_text(f"后端接收到你发送的消息信息，{json.dumps(data)}, 已经处理完毕")

    async def on_disconnect(self, websocket: WebSocket, close_code: int) -> None:
        logger.info(f"断开了连接")


@router.websocket_route('/runcode', name="运行代码")
class Runcode(WebSocketEndpoint):

    async def on_connect(self, websocket: WebSocket) -> None:
        logger.info(f"打开websocket连接")
        await websocket.accept()

    async def on_receive(self, websocket: WebSocket, data: typing.Any) -> None:
        par_data = json.loads(data)
        lang = par_data.get("lang")
        url = "10.1.137.142:8888"
        # 用httpx 库进行异步请求
        # async with httpx.AsyncClient() as client:
        #     resp = await client.post(f"http://{url}/api/kernels", data=json.dumps(dict(name=lang)))
        #     result = resp.json()
        #     await websocket.send_json(dict(id=result.get('id')))

        # 可以套用tornado的AsyncHTTPClient做异步请求和异步websocket请求
        client = AsyncHTTPClient()
        kernel_id = await self.open_kernel(client, lang, url)
        await websocket.send_json(dict(id=kernel_id))

    async def on_disconnect(self, websocket: WebSocket, close_code: int) -> None:
        pass

    async def open_kernel(self, client, lang, url):
        response = await client.fetch(
            'http://{}/api/kernels'.format(url), method='POST',
            body=json_encode({'name': lang})
        )
        kernel = json_decode(response.body)
        kernel_id = kernel.get('id', None)
        logger.info('创建内核{}成功'.format(kernel_id) if kernel_id else '创建内核失败')
        return kernel_id