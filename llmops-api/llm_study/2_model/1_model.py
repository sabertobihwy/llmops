#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024/7/5 19:12
@author: wenyan
@file: 1_model.py
"""
from datetime import datetime
from dotenv import load_dotenv

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()
# 1.编排Prompt_template
prompt = ChatPromptTemplate.from_messages([
    ("system", "你是OpenAI开发的聊天机器人，请回答用户的问题，现在的时间是{now}"),
    ("human", "{query}"),
]).partial(now=datetime.now())

# 2.创建大语言模型
llm = ChatOpenAI(model="gpt-3.5-turbo-16k")

# 3.生成内容prompt value
# prompt_value = prompt.invoke({"query": "现在是几点，请讲一个关于程序员的冷笑话"})
# ai_message = llm.invoke(prompt_value)
#
# # 4.提取内容
# print("type:", ai_message.type)
# print("content:", ai_message.content)
# print("response_metadata:", ai_message.response_metadata)

