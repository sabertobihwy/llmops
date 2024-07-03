#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024/6/28 14:28
@author: wenyan
@file: http.py
"""
import os

from flask import Flask
from internal.router import Router
from config import Config
from internal.exception import CustomException
from pkg.response import json,Response,HttpCode
from flask_sqlalchemy  import SQLAlchemy
class Http(Flask):
    def __init__(self, *args, db : SQLAlchemy,config:Config, router:Router, **kwargs):
        super().__init__(*args, **kwargs)
        router.register_router(self)

        # from_object(config)：from_object 方法会将传入对象（例如上面的 Config 类）中的所有大写属性加载到 Flask 应用实例的配置中。
        self.config.from_object(config)
        self.register_error_handler(Exception, self._error_handler)

        db.init_app(self)

    def _error_handler(self, error : Exception):
        if isinstance(error, CustomException):
            return json(
                Response(
                    code = error.code,
                    message = error.message,
                    data = error.data
                )
            )

        if self.debug or os.environ.get('FLASK_DEBUG') == 1:
            raise error
        else:
            return json(
                Response(
                    code = HttpCode.FAIL,
                    message = str(error),
                    data = {}
                )
            )
