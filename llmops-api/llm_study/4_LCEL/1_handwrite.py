#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024/7/6 21:39
@author: wenyan
@file: 1_handwrite.py
"""

from datetime import datetime

from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()
prompt = ChatPromptTemplate.from_messages([
    ("system", "你是OpenAI开发的聊天机器人，请回答用户的问题，现在的时间是{now}"),
    ("human", "{query}"),
]).partial(now=datetime.now())
llm = ChatOpenAI(model="gpt-3.5-turbo-16k")
parser = StrOutputParser()

class Chain:
    def __init__(self,lst:list):
        self.lst = lst
    def invoke(self,input:dict):
        for i in self.lst:
            input = i.invoke(input)
        return input

chain = Chain([prompt,llm,parser])
print(chain.invoke({"query":"why ecomony is bad recently???"}))