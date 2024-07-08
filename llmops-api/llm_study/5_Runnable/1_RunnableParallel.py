#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024/7/7 12:59
@author: wenyan
@file: 1_RunnableParallel.py
"""

from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel
from langchain_openai import ChatOpenAI

load_dotenv()
joke_prompt = ChatPromptTemplate.from_template("tell me a brief {joke}")
poem_prompt = ChatPromptTemplate.from_template("tell me a brief {poem}")
llm = ChatOpenAI(model="gpt-3.5-turbo-16k")
parser = StrOutputParser()

joke_chain = joke_prompt | llm | parser
poem_chain = poem_prompt | llm | parser

map_chain = RunnableParallel(joke = joke_chain, poem = poem_chain)
res = map_chain.invoke({
    "joke":"joke",
    "poem":"poem",
})
print(res)