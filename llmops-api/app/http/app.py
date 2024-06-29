#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024/6/28 14:51
@author: wenyan
@file: app.py
"""

from internal.server import Http
from injector import Injector
from internal.router import Router

injector = Injector()
app = Http(__name__, router=injector.get(Router))
if __name__ == '__main__':
    app.run(debug=True)
