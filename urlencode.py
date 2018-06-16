#!/bin/env python
# -*- coding:utf-8 -*-
import urllib

# use %20 as space
x = urllib.quote("test 我们")
# use + as space
y = urllib.quote_plus("test 我们")
print urllib.unquote(x)
print urllib.unquote(y)
print urllib.unquote_plus(x)
print urllib.unquote_plus(y)
print x, y
