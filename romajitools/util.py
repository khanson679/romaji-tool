# -*- coding: utf-8 -*-

from __future__ import unicode_literals

"""
Convert a flat list representing pairs of words into a list of lists.
  ex. [a, b, c, d] -> [[a,b], [c,d]]
Returned as a generator.
"""
def pairs(arr):
    size = 2
    for i in range(0, len(arr)-1, size):
        yield arr[i:i+size]

