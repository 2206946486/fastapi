#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time    : 2021/2/18 13:21
@Author  : LJ
@Site    : 
@File    : errors.py
@Software: PyCharm
"""


class EnvError(Exception):

    def __init__(self, err="环境变量有误"):
        Exception.__init__(self, err)


class State(object):
    FAILURE = 0
    SUCCESS = 1

    err_msg = {
        FAILURE: "操作失败",
        SUCCESS: "操作成功",
    }


def res(state=State.SUCCESS, data=None, msg=None):
    if not msg:
        msg = State.err_msg.get(state, "未知错误")
    state = state if state else 0
    return dict(state=state, data=data, msg=msg)

