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
from dotenv import load_dotenv
from config import Config

injector = Injector()
app = Http(__name__, config=Config(), router=injector.get(Router))
load_dotenv()
if __name__ == '__main__':
    app.run(debug=True)
