#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024/7/3 20:18
@author: wenyan
@file: app_service.py
"""
from dataclasses import dataclass
import uuid

from pkg.sqlalchemy import SQLAlchemy

from injector import inject
from internal.model import AppModel


@inject
@dataclass
class AppService:

    db : SQLAlchemy
    def delete_app(self,id:uuid.UUID) -> AppModel:
        with self.db.auto_commit():
            am = AppModel.query.get(id)
            self.db.session.delete(am)
        return am

    def update_app(self,id:uuid.UUID) -> AppModel:
        with self.db.auto_commit():
            am = AppModel.query.get(id)
            am.name = "vincent"
        return am

    def query_app(self,id:uuid.UUID) -> AppModel:
        return AppModel.query.get(id)
    def insert_app(self) -> AppModel:
        with self.db.auto_commit():
            am = AppModel(name="wenyan",account_id=uuid.uuid4(),icon="123",description="123")
            self.db.session.add(am)
        return am
