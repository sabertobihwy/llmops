#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024/7/3 22:25
@author: wenyan
@file: sqlalchemy.py
"""
from contextlib import contextmanager

from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy

class SQLAlchemy(_SQLAlchemy):
    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e