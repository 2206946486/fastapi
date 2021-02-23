#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time    : 2021/2/18 13:38
@Author  : LJ
@Site    : 
@File    : tests.py
@Software: PyCharm
"""
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, Query
from typing import Optional

from app.tools.database import get_db
from app.tools.errors import State, res

from app.models.chaptes import Chapter

from app.schemas.tests import Course

router = APIRouter()


@router.get('/tests')
async def test_get():
    return res(state=State.SUCCESS)


@router.get('/test_mysql', summary="fast_api 测试连接mysql接口")
async def test_mysql_get(*, db: Session = Depends(get_db)):
    data = db.query(Chapter).filter().all()
    return res(data=data)


@router.get('/test_param', summary="fast_api get请求参数验证")
async def test_param_get(*, db: Session = Depends(get_db), course_id: Optional[int] = None):
    """
    :param db:  数据库连接对象
    :param course_id: 课程id, Optional 可选参数
    :return:
    """
    if course_id:
        data = db.query(Chapter).filter(Chapter.courseid == course_id).all()
    else:
        data = db.query(Chapter).filter().all()
    return res(data=data)


@router.post('/test_param', summary="fast_api post请求参数验证")
async def test_param_post(*, db: Session = Depends(get_db), course: Course):
    """
    :param db: 数据库连接对象
    :param course: 参数验证类
    :return:
    """
    if course.course_id:
        data = db.query(Chapter).filter(Chapter.courseid == course.course_id).all()
    else:
        data = db.query(Chapter).filter().all()
    return res(data=data)