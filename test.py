#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from romajitool import *


class RTTestCase(unittest.TestCase):

    def test_lemma_list(self):
        """
        Check that the number of lemmas in master list is correct.
        """
        self.assertEqual(len(defs.LEMMAS_ALL), 153)

    def test_format_lemma_coverage(self):
        """
        Check that for each format, all produced lemmas are in master list,
          lemmas in master list are converted to format.
        """
        for fmt in FORMATS.values():
            for lemma in fmt.outputtable_lemmas():
                self.assertIn(
                    lemma,
                    defs.LEMMAS_ALL,
                    ("Lemma '{}' produced by format '{}'' not in master list."
                     .format(fmt.name, lemma)))
            for lemma in defs.LEMMAS_ALL:
                self.assertIn(
                    lemma,
                    defs.HIRAGANA.inputtable_lemmas(),
                    "Lemma '{}' not handled by format '{}'.".format(lemma, fmt.name))

    def test_hira_to_roma(self):
        # sanity test
        self.assertEqual(
            convert("いちご", in_fmt="hiragana", out_fmt="nihon"),
            "itigo")

    def test_roma_to_hiragana(self):
        # sanity test
        self.assertEqual(
            convert("itigo", in_fmt="nihon", out_fmt="hiragana"),
            "いちご")

    def test_katakana(self):
        self.assertEqual(
            convert("バナナ", in_fmt="katakana", out_fmt="nihon"),
            "banana")
        self.assertEqual(
            convert("banana", in_fmt="nihon", out_fmt="katakana"),
            "バナナ")

    def test_kunrei_consonants(self):
        self.assertEqual(
            convert("しち", in_fmt="hiragana", out_fmt="kunrei"),
            "siti")
        self.assertEqual(
            convert("siti", in_fmt="kunrei", out_fmt="hiragana"),
            "しち")
        self.assertEqual(
            convert("はなぢ", in_fmt="hiragana", out_fmt="kunrei"),
            "hanazi")
        self.assertNotEqual(
            convert("hanazi", in_fmt="kunrei", out_fmt="hiragana"),
            "はなぢ")

    def test_hepburn_consonants(self):
        self.assertEqual(
            convert("しち", in_fmt="hiragana", out_fmt="hepburn"),
            "shichi")
        self.assertEqual(
            convert("shichi", in_fmt="hepburn", out_fmt="hiragana"),
            "しち")
        self.assertEqual(
            convert("はなぢ", in_fmt="hiragana", out_fmt="hepburn"),
            "hanaji")
        self.assertNotEqual(
            convert("hanaji", in_fmt="hepburn", out_fmt="hiragana"),
            "はなぢ")

    def test_nasal_before_vowel(self):
        self.assertEqual(
            convert("ぜんいん", in_fmt="hiragana", out_fmt="hepburn"),
            "zen'in")
        self.assertEqual(
            convert("とんかつ", in_fmt="hiragana", out_fmt="hepburn"),
            "tonkatsu")


if __name__ == '__main__':
    unittest.main()
    # (convert("ぜんいん", in_fmt="hiragana", out_fmt="hepburn"))
    # (convert("zen'in", in_fmt="hepburn", out_fmt="hiragana"))
    # (convert("hiragana", in_fmt="wapuro", out_fmt="hiragana"))
