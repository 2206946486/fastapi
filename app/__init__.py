#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time    : 2021/2/18 11:24
@Author  : LJ
@Site    : 
@File    : __init__.py.py
@Software: PyCharm
"""
import traceback
from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from app.apis import api_router
from app.tools.database import config
from app.tools.logger import logger


tag_metadata = [{
                    "name": "API",
                    "description": "测试系统数据API",
},
]


def create_app():
    app = FastAPI(
        title=config.TITLE,
        description="",
        version="0.1.1",
        docs_url=config.DOCS_URL,
        openapi_url=config.OPENAPI_URL,
        redoc_url=config.REDOC_URL,
        openapi_tags=tag_metadata,
    )

    app.include_router(
        api_router,
        prefix="/api/v1",
    )
    register_exception(app)  # 注册捕获异常信息
    register_cors(app)  # 跨域设置
    register_middleware(app)
    return app


def register_exception(app: FastAPI):
    """
    全局异常捕获
    :param app:
    :return:
    """

    # 捕获参数 验证错误
    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        """
        捕获请求参数 验证错误
        :param request:
        :param exc:
        :return:
        """
        logger.error(f"参数错误\nURL:{request.url}\nHeaders:{request.headers}\n{traceback.format_exc()}")
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content=jsonable_encoder({"code": 400, "data": {"tip": exc.errors()}, "body": exc.body, "message": "fail"}),
        )

    # 捕获全部异常
    @app.exception_handler(Exception)
    async def all_exception_handler(request: Request, exc: Exception):
        logger.error(f"全局异常\nURL:{request.url}\nHeaders:{request.headers}\n{traceback.format_exc()}")
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"code": 500, "data": {"tip": "服务器错误"}, "message": "fail"},
        )

    # 捕获断言错误，用于返回错误状态
    @app.exception_handler(AssertionError)
    async def asser_exception_handler(request: Request, exc: AssertionError):
        logger.error(f"断言错误，URL：{request.url}, 此处条件不符合")
        logger.info(f"------------------------{exc.args}")
        state = exc.args[0] if exc.args else 0
        return JSONResponse(res(state=state))

def register_cors(app: FastAPI):
    """
    支持跨域
    :param app:
    :return:
    """

    app.add_middleware(
        CORSMiddleware,
        allow_origin_regex='https?://.*',  # 改成用正则就行了
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


def register_middleware(app: FastAPI):
    """
    请求响应拦截 hook
    :param app:
    :return:
    """

    @app.middleware("http")
    async def logger_request(request: Request, call_next):
        logger.info(f"访问记录:{request.method} url:{request.url}")

        response = await call_next(request)

        return response
