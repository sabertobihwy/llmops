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
from pkg.sqlalchemy import SQLAlchemy
from config.extension import ExtensionModule
# when db.create_all(), make sure import model
from internal.model import AppModel

# when injector use module
injector = Injector([ExtensionModule()])
db = injector.get(SQLAlchemy)
load_dotenv()
app = Http(__name__, db=db, config=Config(), router=injector.get(Router))

if __name__ == '__main__':
    app.run(debug=True)
   #  with app.app_context():
   #       _ = AppModel()
   #      db.create_all()