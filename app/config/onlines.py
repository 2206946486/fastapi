#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time    : 2021/2/18 13:11
@Author  : LJ
@Site    : 
@File    : onlines.py
@Software: PyCharm
"""
from typing import Union, Optional
from pydantic import AnyHttpUrl, BaseSettings, IPvAnyAddress


class OnlinesSetting(BaseSettings):
    # 文档地址
    DOCS_URL: str = "/api/v1/docs"
    # 文档关联请求数据接口
    OPENAPI_URL: str = "/api/v1/openapi.json"
    # redoc 文档
    REDOC_URL: Optional[str] = None
    # title
    TITLE = "FASTAPI"

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    SECRET_KEY: str = 'aeq)s(*&dWEQasd8**&^9asda_asdasd*&*&^+_sda'

    # 配置你的Mysql环境
    MYSQL_USERNAME: str = 'root'
    MYSQL_PASSWORD: str = "gta@2014"
    MYSQL_HOST: Union[AnyHttpUrl, IPvAnyAddress] = "192.168.203.34"
    MYSQL_DATABASE: str = 'dema'
    MYSQL_PORT = 3306

    # Mysql地址
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{MYSQL_USERNAME}:{MYSQL_PASSWORD}@" \
                              f"{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}?charset=utf8mb4"


config = OnlinesSetting()
