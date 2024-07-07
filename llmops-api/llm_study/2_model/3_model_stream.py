#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024/7/5 19:37
@author: wenyan
@file: 3_model_stream.py
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

# 3.流式输出
response = llm.stream(prompt.invoke({"query": "LLM和LLMOps"}))
for chunk in response:
    print(chunk.content, flush=True, end="")