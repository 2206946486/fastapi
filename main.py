#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time    : 2021/2/18 11:03
@Author  : LJ
@Site    : 
@File    : main.py
@Software: PyCharm
"""
from uvicorn import run

from app import create_app


app = create_app()

if __name__ == "__main__":
    run(app=app, host='0.0.0.0', port=5027)
