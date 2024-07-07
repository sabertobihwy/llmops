#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024/7/5 21:40
@author: wenyan
@file: 1_StrOutputParser.py
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

#StrOutputParser().parse("程序员的梦工厂")
# invoke也调用了parse()
content = StrOutputParser().invoke(llm.invoke(prompt.invoke({"query":"introduce waterloo"})))
print(content)