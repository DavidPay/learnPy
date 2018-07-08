#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author: David Pay
#date: 07-05-2018

from jinja2 import Template
template = Template('Hello {{ name }}')
print(template.render(name='John doe'))