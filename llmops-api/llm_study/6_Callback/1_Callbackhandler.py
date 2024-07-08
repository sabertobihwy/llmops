#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024/7/7 15:27
@author: wenyan
@file: 1_Callbackhandler.py
"""
from typing import Dict, Any, Optional, List, Union
from uuid import UUID

from dotenv import load_dotenv
from langchain_core.messages import BaseMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.outputs import GenerationChunk, ChatGenerationChunk
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from langchain_openai import ChatOpenAI
from langchain_core.callbacks import StdOutCallbackHandler, BaseCallbackHandler

load_dotenv()
class LlmopsCallbackHandler(BaseCallbackHandler):
    def on_chain_start(
        self,
        serialized: Dict[str, Any],
        inputs: Dict[str, Any],
        *,
        run_id: UUID,
        parent_run_id: Optional[UUID] = None,
        tags: Optional[List[str]] = None,
        metadata: Optional[Dict[str, Any]] = None,
        **kwargs: Any,
    ) -> Any:
        pass
        # print("====start====")
        # print(serialized)
        # print(inputs)
    def on_chat_model_start(
        self,
        serialized: Dict[str, Any],
        messages: List[List[BaseMessage]],
        *,
        run_id: UUID,
        parent_run_id: Optional[UUID] = None,
        tags: Optional[List[str]] = None,
        metadata: Optional[Dict[str, Any]] = None,
        **kwargs: Any,
    ) -> Any:
        print("====on_chat_model_start start====")

    def on_llm_new_token(
        self,
        token: str,
        *,
        chunk: Optional[Union[GenerationChunk, ChatGenerationChunk]] = None,
        run_id: UUID,
        parent_run_id: Optional[UUID] = None,
        **kwargs: Any,
    ) -> Any:
        print(f"token:{token}")

def retrieve(query:str) -> str:
    print("searching online")
    return "Tom is a full-stack software developer but without AI knowledge in a fierce job market ."

prompt = ChatPromptTemplate.from_template(""" 
                            {query}""")
llm = ChatOpenAI(model="gpt-3.5-turbo-16k")
parser = StrOutputParser()

chain = ({"query": RunnablePassthrough()}
        | prompt | llm | parser)

#content = chain.invoke("how can Tom be employed ???", config={"callbacks":[StdOutCallbackHandler(),LlmopsCallbackHandler()]})
#print(content)

content = chain.stream("how can Tom be employed ???", config={"callbacks":[StdOutCallbackHandler(),LlmopsCallbackHandler()]})
for i in content:
    pass