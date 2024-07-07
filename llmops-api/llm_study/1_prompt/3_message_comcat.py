#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024/7/5 16:28
@author: wenyan
@file: 3_message_comcat.py
"""
from datetime import datetime

from langchain_core.prompts import ChatPromptTemplate

c1 = ChatPromptTemplate.from_messages([("system","i'm openai, time is {now}")])
c2 = ChatPromptTemplate.from_messages([("human","{answer}")])

c3 = c1+c2
print(c3.invoke({"now":datetime.now(), "answer":"123123"}))