#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time    : 2021/2/18 16:02
@Author  : LJ
@Site    : 
@File    : __init__.py.py
@Software: PyCharm
"""
from typing import Optional
from pydantic import BaseModel, conint


class PageBase(BaseModel):
    page: int = 1
    pageSize: conint(le=50) = 10  # 限制最大长度小于等于 50 默认10


class Course(BaseModel):
    course_id: int = None
