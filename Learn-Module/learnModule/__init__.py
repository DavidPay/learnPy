#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
---normal module structure---

|- LICENSE
|- README.md
|- TODO.md
|- docs
| |-- conf.py
| |-- generated
| |-- index.rst
| |-- installation.rst
| |-- modules.rst
| |-- quickstart.rst
| |-- sandman.rst
|- requirements.txt
|- sandman
| |-- __init__.py
| |-- exception.py
| |-- model.py
| |-- sandman.py
| |-- test
| |-- models.py
| |-- test_sandman.py                  #add .. to sys.path 
|--tests                               #can use sandman module
|- setup.py

'''


'''
search path is sys.path including current path. so in module, you can't find the module name!
'''
 
__all__ = ["getFunc"] 