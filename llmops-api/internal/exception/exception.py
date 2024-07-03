#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024/6/29 14:56
@author: wenyan
@file: exception.py
"""
from dataclasses import field
from typing import Any

from pkg.response import HttpCode

class CustomException(Exception):
    code : HttpCode = HttpCode.FAIL
    message : str = ""
    data: Any = field(default_factory=dict)
    def __init__(self, message: str, data: Any):
        super().__init__()
        self.message = message
        self.data = data

class FailException(CustomException):
    pass

class NotFoundException(CustomException):
    code = HttpCode.NOT_FOUND

class UnauthorizedException(CustomException):
    code = HttpCode.UNAUTHORIZED

class ForbiddenException(CustomException):
    code = HttpCode.FORBIDDEN

class ValidationException(CustomException):
    code = HttpCode.VALIDATE_ERROR
