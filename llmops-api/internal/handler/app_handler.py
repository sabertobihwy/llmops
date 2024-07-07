#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024/6/28 14:12
@author: wenyan
@file: app_handler.py
"""
import uuid
from dataclasses import dataclass

from injector import inject
from openai import OpenAI
from internal.scheme import CompletionReq
from internal.service import AppService
from pkg.response import success_json, validate_error_json, success_message
from internal.exception import FailException
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

@inject
@dataclass
class AppHandler:
    service: AppService

    def delete_app(self,id:uuid.UUID):
        am = self.service.delete_app(id)
        return success_message(f"successfully delete appModel, {am.name}")
    def update_app(self,id:uuid.UUID):
        am = self.service.update_app(id)
        return success_message(f"successfully update appModel, {am.name}")

    def query_app(self,id:uuid.UUID):
        am = self.service.query_app(id)
        return success_message(f"successfully query appModel, {am.name}")
    def insert_app(self):
        self.service.insert_app()
        return success_message("successfully inserted into appModel")

    def openai_app(self):
        req = CompletionReq()
        if not req.validate():
            return validate_error_json(req.errors)

        prompt_tmp = ChatPromptTemplate.from_template("{query}")
        llm = ChatOpenAI(model="gpt-3.5-turbo-16k")
       # msg = llm.invoke(prompt_tmp.invoke({"query": req.query}))
        parser = StrOutputParser()

        chain = prompt_tmp | llm | parser
        content = chain.invoke({"query": req.query})

        return success_json({"content": content})

    def ping(self):
        raise FailException("failed msg", {})
