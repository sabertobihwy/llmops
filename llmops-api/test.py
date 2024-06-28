#!/usr/bin/env python
# -*- coding: utf-8 -*-

from injector import Injector,inject


class A:
    def print(self):
        print("aaaaa")

@inject
class B:
    def __init__(self,a:A):
        self.a = a

injector = Injector()
b_instance = injector.get(B)
b_instance.a.print()