#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024/7/5 22:09
@author: wenyan
@file: 2_JsonOutputParser.py
"""
import dotenv
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()

# 1.构建输出json格式类
class Joke(BaseModel):
    joke: str = Field(description="回答用户的冷笑话")
    punchline: str = Field(description="冷笑话的笑点")

parser = JsonOutputParser(pydantic_object=Joke)
#print(p.get_format_instructions())

prompt = (ChatPromptTemplate.from_template("请根据用户的提问回答，规范是：{json_instructions}\n 用户提问为：{query}")
          .partial(json_instructions=parser.get_format_instructions()))

# 2.创建大语言模型
llm = ChatOpenAI(model="gpt-3.5-turbo-16k")
baseMsg = llm.invoke(prompt.invoke({"query":"你讲一个joke和joke的punchline"}))
json = parser.invoke(baseMsg)

print(type(json))
print(json.get("punchline"))