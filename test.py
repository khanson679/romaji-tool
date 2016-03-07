#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest

from romajitools import *

class RTTestCase(unittest.TestCase):
    def test_lemma_tables(self):
        # sanity test
        self.assertEqual(len(LEMMAS), 233)
        
        # have all lemmas in the full table been categorized?
        self.assertEqual(
            len(LEMMAS),
            len(LEMMAS_BASIC) + len(LEMMAS_EXTENDED) + len(LEMMAS_EXTRA))
    
    def test_hiragana_table(self):
        # check that all Hiragana entries have a lemma, and vis versa
        for lemma in FROM_HIRA.itervalues():
            self.assertTrue(lemma in LEMMAS)
        for lemma in LEMMAS:
            self.assertTrue(lemma in FROM_HIRA.itervalues())
        
    def test_convert_from_hira(self):
        # sanity test
        self.assertEqual(to_wapuro("ひらがな"), "hiragana")

if __name__ == '__main__':
    unittest.main()
