#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time    : 2021/2/20 16:14
@Author  : LJ
@Site    : 
@File    : logger.py
@Software: PyCharm
"""
import os
import time
from loguru import logger


basedir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

log_path = os.path.join(basedir, 'logs')

if not os.path.exists(log_path):
    os.mkdir(log_path)

log_path = os.path.join(log_path, f'dema_simplify_{time.strftime("%Y-%m-%d")}.log')

logger.add(log_path, rotation="01:00", format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}", enqueue=True,
           encoding="utf-8")
