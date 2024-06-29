#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024/6/28 14:28
@author: wenyan
@file: http.py
"""
from flask import Flask
from internal.router import Router
class Http(Flask):
    def __init__(self, *args, router:Router, **kwargs):
        super().__init__(*args, **kwargs)
        router.register_router(self)