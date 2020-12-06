#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from romajitool import *


class RTTestCase(unittest.TestCase):

    def test_lemma_list(self):
        """
        Check that the number of lemmas in master list is correct.
        """
        self.assertEqual(len(defs.LEMMAS), 153)

    def test_format_lemma_coverage(self):
        """
        Check that for each format, all produced lemmas are in master list,
          lemmas in master list are converted to format.
        """
        for fmt in FORMATS.values():
            for lemma in fmt.produced_lemmas():
                self.assertIn(
                    lemma,
                    defs.LEMMAS,
                    "Lemma '{}' produced by format '{}'' not in master list.".format(fmt.name, lemma))
            for lemma in defs.LEMMAS:
                self.assertIn(
                    lemma,
                    textformat.HIRAGANA.accepted_lemmas(),
                    "Lemma '{}' not handled by format '{}'.".format(lemma, fmt.name))

    def test_hira_to_wapuro(self):
        # sanity test
        self.assertEqual(
            convert("ひらがな", in_fmt="hiragana", out_fmt="wapuro"),
            "hiragana")

    def test_wapuro_to_hiragana(self):
        # sanity test
        self.assertEqual(
            convert("hiragana", in_fmt="wapuro", out_fmt="hiragana"),
            "ひらがな")

    def test_hira_to_kunrei(self):
        self.assertEqual(
            convert("しち", in_fmt="hiragana", out_fmt="kunrei"),
            "siti")

    def test_kunrei_to_hira(self):
        self.assertEqual(
            convert("siti", in_fmt="kunrei", out_fmt="hiragana"),
            "しち")

    def test_hira_to_hepburn(self):
        self.assertEqual(
            convert("しち", in_fmt="hiragana", out_fmt="hepburn"),
            "shichi")

    def test_hepburn_to_hira_(self):
        self.assertEqual(
            convert("shichi", in_fmt="hepburn", out_fmt="hiragana"),
            "しち")


if __name__ == '__main__':
    unittest.main()
