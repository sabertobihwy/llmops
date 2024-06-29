#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024/6/28 14:12
@author: wenyan
@file: app_handler.py
"""
from flask import request
from openai import OpenAI
from internal.scheme import CompletionReq
class AppHandler:

    def openai_app(self):
        req = CompletionReq()
        if not req.validate():
            return req.errors

        client = OpenAI()
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system",
                 "content": "You are a poetic assistant, "
                            "skilled in explaining complex programming concepts with creative flair."},
                {"role": "user", "content": req.query.data}
            ]
        )

        content = completion.choices[0].message.content
        return content

    def ping(self):
        return 'pong'
