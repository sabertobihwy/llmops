#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024/7/3 11:05
@author: wenyan
@file: app.py
"""
import uuid
from datetime import datetime

from sqlalchemy import UUID, Column, String, Text, DateTime, PrimaryKeyConstraint, Index

from internal.extension.database_extension import db

class AppModel(db.Model):
    __tablename__ = 'appmodel'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='pk_app_id'),
        Index('idx_account_id', 'account_id'),
    )
    id = Column(UUID,default=uuid.uuid4,nullable=False)
    account_id = Column(UUID,nullable=False)
    name = Column(String(255),default="",nullable=False)
    icon = Column(String(255),default="",nullable=False)
    status = Column(String(255),default="",nullable=True)
    description = Column(Text,default="",nullable=False)
    updated_at = Column(DateTime,default=datetime.now, onupdate=datetime.now,nullable=False)
    created_at = Column(DateTime,default=datetime.now, nullable=False)