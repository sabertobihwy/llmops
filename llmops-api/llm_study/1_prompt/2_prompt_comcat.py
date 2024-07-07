#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024/7/5 15:41
@author: wenyan
@file: 2_prompt_comcat.py
"""
from langchain_core.prompts import PromptTemplate

# __add__
pv = (
        PromptTemplate.from_template("tell me a story about {who}")
        + " what is this?"
)
print(pv.invoke({"who": 123}))
