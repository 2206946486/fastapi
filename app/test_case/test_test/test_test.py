#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time    : 2021/3/11 13:39
@Author  : LJ
@Site    : 
@File    : test_test.py
@Software: PyCharm
"""
from fastapi.testclient import TestClient
from main import app

"""
    测试用例
"""
client = TestClient(app)


def test_test_get():
    response = client.get('/api/v1/tests')
    assert response.status_code
    assert response.json().get('state') == 1