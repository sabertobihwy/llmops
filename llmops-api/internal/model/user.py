#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024/7/3 14:21
@author: wenyan
@file: user.py
"""
from sqlalchemy import Column

from internal.extension.database_extension import db


class UserTest(db.Model):
    id = Column(db.Integer, primary_key=True)
    username = Column(db.String(80), unique=True, nullable=False)
    email = Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User2 {self.username}>'