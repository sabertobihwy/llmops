#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024/6/29 11:52
@author: wenyan
@file: req_scheme.py
"""

from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length

class CompletionReq(FlaskForm):
    query = StringField('query', validators=
                    [DataRequired(message="This field is required."),
                    Length(min=1, max=50)])
