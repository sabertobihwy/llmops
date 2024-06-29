#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024/6/29 12:57
@author: wenyan
@file: http_code.py
"""
from enum import Enum

class HttpCode(str, Enum):
    """
    HTTP 基础业务状态码
    """
    SUCCESS = "success"        # 成功状态
    FAIL = "fail"              # 失败状态
    NOT_FOUND = "not_found"    # 未找到
    UNAUTHORIZED = "unauthorized"  # 未授权
    FORBIDDEN = "forbidden"    # 无权限
    VALIDATE_ERROR = "validate_error"  # 数据验证错误