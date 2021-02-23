#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time    : 2021/2/18 14:38
@Author  : LJ
@Site    : 
@File    : chaptes.py
@Software: PyCharm
"""
from app.tools.database import Base
from sqlalchemy import Column, Integer, Sequence, String, DateTime, BigInteger, Boolean, Float


class Chapter(Base):
    __tablename__ = 'chapter'

    id = Column(Integer, primary_key=True)
    courseid = Column(Integer)
    coursename = Column(String)
    chaptername = Column(String)
    project_id = Column(Integer)
    updatetime = Column(DateTime)
    createtime = Column(DateTime)

    __mapper_args__ = {"order_by": id}


class Course(Base):
    __tablename__ = 'course'

    id = Column(Integer, primary_key=True)
    courseid = Column(Integer)
    name = Column(String)
    intro = Column(String)
    labels = Column(String)
    difficulty = Column(Float)
    score = Column(Float)
    visitcount = Column(BigInteger)
    learncount = Column(BigInteger)
    authorid = Column(Integer)
    chapter_total = Column(Integer)
    state = Column(Integer)
    updatetime = Column(DateTime)
    createtime= Column(DateTime)