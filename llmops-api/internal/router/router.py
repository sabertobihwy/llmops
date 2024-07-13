#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024/6/28 14:14
@author: wenyan
@file: router.py
"""

from flask import Flask, Blueprint
from internal.handler import AppHandler
from injector import inject
from dataclasses import dataclass


@inject
@dataclass
class Router:
    """register router: bind router with handler"""
    apphandler: AppHandler

    def register_router(self, app: Flask):
        bp = Blueprint("llmops_router", __name__, url_prefix="")
        bp.add_url_rule("/ping", view_func=self.apphandler.ping)  # func name, not result!
        bp.add_url_rule("/openai/<api_key>", methods=["POST"], view_func=self.apphandler.openai_app)
        bp.add_url_rule("/insert", methods=["POST"], view_func=self.apphandler.insert_app)
        bp.add_url_rule("/get/<uuid:id>", view_func=self.apphandler.query_app)
        bp.add_url_rule("/update/<uuid:id>", methods=["POST"], view_func=self.apphandler.update_app)
        bp.add_url_rule("/del/<uuid:id>", view_func=self.apphandler.delete_app)

        app.register_blueprint(bp)
