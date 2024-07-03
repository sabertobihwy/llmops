#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024/7/3 10:47
@author: wenyan
@file: extension.py
"""
from injector import Module, Binder

from internal.extension.database_extension import db
from flask_sqlalchemy import SQLAlchemy

# extension module's dependency injection

class ExtensionModule(Module):
    def configure(self, binder: Binder) -> None:
        binder.bind(SQLAlchemy, to=db)
