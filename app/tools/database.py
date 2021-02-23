#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time    : 2021/2/18 15:34
@Author  : LJ
@Site    : 
@File    : database.py
@Software: PyCharm
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import load_config
from app.tools.logger import logger

config = load_config()
# print("开始加载数据库")
logger.info(f"开始加载数据库")


engine = create_engine(
    config.SQLALCHEMY_DATABASE_URI
)
#
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

