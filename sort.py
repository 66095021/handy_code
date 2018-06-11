#!/bin/env python

# sort by multiple items
a = [{'a': 'a', 'b': 2}, {'a': 'b', 'b': 1}, {'a': 'c', 'b': 3}, {'a': 'c', 'b': 2}]
b = sorted(a, key = lambda x:(x["a"] ,-x["b"]))
print b


