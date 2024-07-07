#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024/7/5 16:37
@author: wenyan
@file: 4_reuse_prompt_temp.py
"""
from langchain_core.prompts import PromptTemplate, PipelinePromptTemplate

full_prompt = PromptTemplate.from_template("""
    {instruction}
    
    {example}
    
    {start}

""")

instruction_pmt = PromptTemplate.from_template("you are simulating {person}")
example_pmt = PromptTemplate.from_template("""This is an example:
Q1:{Q1}
A1:{A1}
""")
start_pmt = PromptTemplate.from_template("""Now start:
Q1:{Q2}
A1:
""")

pipeline_prompts = [
    ("instruction", instruction_pmt),
    ("example",example_pmt),
    ("start",start_pmt)
]

pt = PipelinePromptTemplate(
    final_prompt=full_prompt,
    pipeline_prompts=pipeline_prompts,
)
str = pt.invoke({"person": "Lady gaga",
                 "Q1": "what's your favourite song?",
                 "A1": "rain on me",
                 "Q2": "what is your favourite music style?"})
print(str.to_string())
