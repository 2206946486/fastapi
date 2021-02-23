#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time    : 2021/2/18 11:26
@Author  : LJ
@Site    : 
@File    : __init__.py.py
@Software: PyCharm
"""
import os
from app.tools.errors import EnvError
from app.tools.logger import logger


def load_config():
    logger.info("开始加载环境配置")
    env = os.getenv("ENV", "TESTING")
    if env == "TESTING":
        from app.config.testing import config
        logger.info("加载测试环境")
        return config
    elif env == "ONLINES":
        logger.info("加载线上环境")
        from app.config.onlines import config
        return config
    else:
        raise EnvError
