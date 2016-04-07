# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import re

import defs


class Mapping(object):
    """
    Defines a partial mapping from the internal representation to a surface form.

    A mapping can be one-to-one, one-to-many, or many-to-one.
    """

    def __init__(self, mapping, direction="both", *addons):
        """
        mapping -- a list of tuples of the form surface:underlying
        addon   -- additional 
        context -- a regex lookahead/lookbehind string
        """
        pass