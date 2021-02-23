#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time    : 2021/2/18 11:27
@Author  : LJ
@Site    : 
@File    : __init__.py.py
@Software: PyCharm
"""
import os
from fastapi import APIRouter

from app.apis.test import tests
from app.apis import websockets, courses
from app.tools.logger import logger


api_router = APIRouter()
"""
注册路由
"""
env = os.getenv("ENV", "TESTING")
logger.info(f"{env}")
if env == "TESTING":
    api_router.include_router(tests.router, tags=["测试"])
api_router.include_router(websockets.router, tags=["websocket"])
api_router.include_router(courses.router, tags=["课程"])
