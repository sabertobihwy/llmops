#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024/6/29 12:57
@author: wenyan
@file: response.py
"""

from dataclasses import dataclass, field
from typing import Any
from .http_code import HttpCode
from flask import jsonify


@dataclass
class Response:
    code: HttpCode = HttpCode.SUCCESS
    message: str = ""
    data: Any = field(default_factory=dict)


def json(data: Response = None):
    return jsonify(data), 200


def success_json(data: Any = None):
    return json(Response(code=HttpCode.SUCCESS, message="", data=data))


def fail_json(data: Any = None):
    return json(Response(code=HttpCode.FAIL, message="", data=data))


def validate_error_json(errors: dict = None):
    first_key = next(iter(errors.keys()))
    if first_key is not None:
        msg = errors.get(first_key)
    else:
        msg = ""
    return json(Response(code=HttpCode.VALIDATE_ERROR, message=msg, data=errors))


"""
提示msg，不返回数据
"""


def message(code: HttpCode = None, message: str = ""):
    return json(Response(code=code, message=message, data={}))


"""
success msg
"""


def success_message(msg: str = ""):
    return message(code=HttpCode.SUCCESS, message=msg)


def fail_message(msg: str = ""):
    return message(code=HttpCode.FAIL, message=msg)


def not_found_message(msg: str = ""):
    return message(code=HttpCode.NOT_FOUND, message=msg)


def unauthorized_message(msg: str = ""):
    return message(code=HttpCode.UNAUTHORIZED, message=msg)


def forbidden_message(msg: str = ""):
    return message(code=HttpCode.FORBIDDEN, message=msg)
