#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import unittest

from romajitools import *


class RTTestCase(unittest.TestCase):

    def test_lemma_tables(self):
        # sanity test
        self.assertEqual(len(defs.LEMMAS), 153)
    
    def test_hiragana_lemmas(self):
        # check that all Hiragana table lemmas in master list, and vis versa
        for lemma in FORMATS["hiragana"].produced_lemmas():
            self.assertIn(
                lemma,
                defs.LEMMAS,
                "Lemma from Hiragana table not in lemma list: {}".format(lemma))
        for lemma in defs.LEMMAS:
            self.assertIn(
                lemma,
                FORMATS["hiragana"].accepted_lemmas(),
                "Hiragana table missing a lemma: {}".format(lemma))

    def test_hira_to_wapuro(self):
        # sanity test
        self.assertEqual(
            convert("ひらがな", in_fmt="hiragana", out_fmt="wapuro"),
            "hiragana")


if __name__ == '__main__':
    unittest.main()