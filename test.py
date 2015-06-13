#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest

from romajitools import *

class RTTestCase(unittest.TestCase):
    def test_convert_from_hira(self):
        self.assertEqual(to_wapuro("ひらがな"), "hiragana")

if __name__ == '__main__':
    unittest.main()
