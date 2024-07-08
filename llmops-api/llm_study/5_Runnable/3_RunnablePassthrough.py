#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024/7/7 13:43
@author: wenyan
@file: 3_RunnablePassthrough.py
"""
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from langchain_openai import ChatOpenAI

load_dotenv()

def retrieve(query:str) -> str:
    print("searching online")
    return "Tom is a full-stack software developer but without AI knowledge in a fierce job market ."

prompt = ChatPromptTemplate.from_template("""according to context:{context}, 
                            we can answer your question:{query}""")
llm = ChatOpenAI(model="gpt-3.5-turbo-16k")
parser = StrOutputParser()

# chain = {
#     "context": retrieve,
#     "query": RunnablePassthrough()
# } | prompt | llm | parser
# 研究源码,发现：使用callable对象（func）内部会转换成RunableLambda，等同于lambda x : retrieve(x)
#     elif callable(thing):
#         return RunnableLambda(cast(Callable[[Input], Output], thing))
chain = RunnablePassthrough.assign(context=lambda x : retrieve(x["query"]))| prompt | llm | parser

print(chain.invoke({"query":"how can Tom be employed ???"}))