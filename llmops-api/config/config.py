#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024/6/29 12:07
@author: wenyan
@file: config.py
"""
import os
from typing import Any

from config.default_config import DEFAULT_CONFIG

def _get_env(key : str) -> Any:
    #print(os.environ.get(key, DEFAULT_CONFIG.get(key)))
    return os.environ.get(key, DEFAULT_CONFIG.get(key))
# "True", "123"

def _get_env_bool(key : str) -> Any:
    value:str = _get_env(key)
    return True if value.lower() == "true" else False

class Config:
    def __init__(self):
        self.WTF_CSRF_ENABLED = _get_env_bool("WTF_CSRF_ENABLED")
        self.SQLALCHEMY_DATABASE_URI= _get_env("SQLALCHEMY_DATABASE_URI")
        self.SQLALCHEMY_ENGINE_OPTIONS ={
            "pool_size" :  int(_get_env("SQLALCHEMY_POOL_SIZE")),
            "pool_recycle" : int(_get_env("SQLALCHEMY_POOL_RECYCLE"))
        }
        self.SQLALCHEMY_ECHO= _get_env_bool("SQLALCHEMY_ECHO")