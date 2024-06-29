#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024/6/28 14:28
@author: wenyan
@file: http.py
"""
from flask import Flask
from internal.router import Router
from config import Config
class Http(Flask):
    def __init__(self, *args, config:Config, router:Router, **kwargs):
        super().__init__(*args, **kwargs)
        router.register_router(self)
        # from_object(config)：from_object 方法会将传入对象（例如上面的 Config 类）中的所有大写属性加载到 Flask 应用实例的配置中。
        self.config.from_object(config)