#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time    : 2021/2/20 16:51
@Author  : LJ
@Site    : 
@File    : courses.py
@Software: PyCharm
"""
from fastapi import APIRouter, Depends, BackgroundTasks
from sqlalchemy.orm import Session

from app.tools.database import get_db
from app.tools.errors import State, res
from app.models.chaptes import Course, Chapter


router = APIRouter()


@router.get('/get_course', summary="获取课程列表")
async def get_course_get(*, db: Session = Depends(get_db)):
    data = db.query(Course).filter().all()
    return res(data=data)


@router.get('/get_chapter', summary="通过课程，获取章节列表")
async def get_chapter_get(*, db: Session = Depends(get_db), course_id: int):
    data = db.query(Chapter).filter(Chapter.courseid == course_id).all()
    return res(data=data)


def task(a):
    print(a)


@router.post('/background_tasks')
async def background_tasks(framework: str, background_task: BackgroundTasks):
    background_task.add_task(task, framework)
    return res(msg="后台任务执行成功")