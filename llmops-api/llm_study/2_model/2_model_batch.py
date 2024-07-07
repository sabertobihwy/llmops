#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024/7/5 19:36
@author: wenyan
@file: 2_model_batch.py
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

# 3.批处理获取响应
ai_messages = llm.batch([
    prompt.invoke({"query": "will ai application developer be popular in the future?"}),
    prompt.invoke({"query": "python or golang, which one is promising?"}),
])

for ai_message in ai_messages:
    print(ai_message.content)
    print("==========")