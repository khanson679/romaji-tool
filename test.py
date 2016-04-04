#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import unittest

from romajitools import *


class RTTestCase(unittest.TestCase):

    def test_lemma_tables(self):
        # sanity test
        self.assertEqual(len(defs.LEMMAS), 153)
    
    def test_format_lemma_coverage(self):
        # check that for each format, all produced lemmas are in master list,
        #   lemmas in master list are converted to format
        for fmt in FORMATS.itervalues():
            for lemma in fmt.produced_lemmas():
                self.assertIn(
                    lemma,
                    defs.LEMMAS,
                    "Lemma '{}' produced by format '{}'' not in master list.".format(fmt.name, lemma))
            for lemma in defs.LEMMAS:
                self.assertIn(
                    lemma,
                    textformat.HIRAGANA.accepted_lemmas(),
                    "Lemma '{}' not handled by format '{}'.".format(fmt.name, lemma))

    def test_hira_to_wapuro(self):
        # sanity test
        self.assertEqual(
            convert("ひらがな", in_fmt="hiragana", out_fmt="wapuro"),
            "hiragana")


if __name__ == '__main__':
    unittest.main()