#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024/7/5 15:17
@author: wenyan
@file: 1_promt.py
"""
from datetime import datetime

from langchain_core.prompts import (
    PromptTemplate,ChatPromptTemplate,HumanMessagePromptTemplate,
    MessagesPlaceholder
)
from langchain_core.messages import AIMessage

# 1. template
#prompt = PromptTemplate.from_template("tell me a story about {who}")
#print(prompt.format(who="elden ring"))
cpt = ChatPromptTemplate.from_messages([
    ("system","i'm openai, time is {now}"),
    MessagesPlaceholder("chat_hist"),
    HumanMessagePromptTemplate.from_template("tell me a story about {who}")
])

# 2. invoke
#pmt_value = prompt.invoke({"who":"elden ring"})
#print(pmt_value)
#print(pmt_value.to_string())
#print(pmt_value.to_messages())

cpt_value = cpt.invoke({
    "now": datetime.now(),
    "chat_hist": [
        ("human","last time"),
        AIMessage("what can i do for you?")
    ],
    "who": "elden ring"
})
print(cpt_value)