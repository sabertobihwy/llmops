#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024/7/7 13:20
@author: wenyan
@file: 2_RunnableParallel_demo.py
"""
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel
from langchain_openai import ChatOpenAI

load_dotenv()

def retrieve(query:str) -> str:
    print("searching online")
    return "Tom is a full-stack software developer but without AI knowledge."

prompt = ChatPromptTemplate.from_template("""according to context:{context}, 
                            we can answer your question:{query}""")
llm = ChatOpenAI(model="gpt-3.5-turbo-16k")
parser = StrOutputParser()

chain = {
    "context": lambda x : retrieve(x["query"]),
    "query": lambda x : x["query"]
} | prompt | llm | parser

print(chain.invoke({"query":"Can Tom get on a path of developing AI applications?"}))