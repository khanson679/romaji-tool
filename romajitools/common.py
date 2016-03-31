#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function

import re
import itertools
from pprint import pprint, pformat

from defs import *
from util import *


FORMATS = ("hira", "hira-half", "kata", "kata-half",
    "wapuro", "kunrei", "hepburn", "hepburn-trad")


#
# public functions
#

def convert(in_str, in_fmt, out_fmt, in_opts=None, out_opts=None):
    # temporarily hardcode format args
    in_fmt = "hira"
    out_fmt = "wapuro"

    if in_opts == None:
        in_opts = []
    if out_opts == None:
        out_opts = []

    # map to internal representation, replacing matched lemmas as they occur
    try:
        in_mapping = IN_MAPPINGS[in_fmt]
    except KeyError:
        raise ValueError("in_fmt must be one of: {}."
                         " Got '{}' instead.".format(FORMATS, in_fmt))
    pattern = IN_PATTERNS[in_fmt]
    intermediate = FROM_HIRA_PAT.sub(lambda x: in_mapping[x.group(0)], in_str)

    # map to output format
    try:
        out_mapping = OUT_MAPPINGS[out_fmt]
    except KeyError:
        raise ValueError("out_fmt must be one of: {}."
                         " Got '{}' instead.".format(FORMATS, out_fmt))

def to_wapuro(in_str):
    """
    Convert any format to wapuro romaji.
    """
    
    intermediate = FROM_HIRA_PAT.sub(lambda x: FROM_HIRA[x.group(0)], in_str)
    return intermediate.lower()

def dump_tables():
    print("--------------------"
          "Lemma Table - Full"
          "--------------------")
    print(LEMMAS)
    print("Total:", len(LEMMAS))

    print("--------------------"
          "Lemma Table - Basic"
          "--------------------")
    print(LEMMAS_BASIC)
    print("Total:", len(LEMMAS_BASIC))

    print("--------------------"
          "Lemma Table - Extended"
          "--------------------")
    print(LEMMAS_EXTENDED)
    print("Total:", len(LEMMAS_EXTENDED))

    print("--------------------"
          "Lemma Table - Extra"
          "--------------------")
    print(LEMMAS_EXTRA)
    print("Total:", len(LEMMAS_EXTRA))

    print("--------------------"
          "Hiragana Table"
          "--------------------")
    print(pformat(FROM_HIRA).encode('utf8'))
    print("Total:", len(FROM_HIRA))

#
# init format converstion data
#

LEMMAS_BASIC    = LEMMA_TAB_BASIC.split()
LEMMAS_EXTENDED = LEMMA_TAB_EXTENDED.split()
LEMMAS_EXTRA    = LEMMA_TAB_EXTRA.split()
LEMMA_SOKUON = LEMMA_SOKUON
LEMMAS_SMALL_KANA_POST = LEMMA_TAB_SMALL_KANA_POST.split()
LEMMAS = list(itertools.chain(LEMMAS_BASIC, LEMMAS_EXTENDED, LEMMAS_EXTRA,
        [LEMMA_SOKUON], LEMMAS_SMALL_KANA_POST))

# build mappings

FROM_HIRA = {}
for entry in re.split(",\s*", HIRAGANA_TAB):
    hira, lemma = entry.split()
    FROM_HIRA[hira] = lemma
    # add sokuon, if applicable
    # ex. ka -> kka   but not wa -> wwa
    consonant = lemma[0]
    if consonant in SOKUON_CONSONANTS:
        sokuon_lemma = consonant + lemma
        sokuon_hira = HIRAGANA_SOKUON + hira
        FROM_HIRA[sokuon_hira] = sokuon_lemma

IN_MAPPINGS = {"hira":FROM_HIRA}

TO_HIRA = {lemma : hira for hira, lemma in FROM_HIRA.iteritems()}
OUT_MAPPINGS = {"hira":TO_HIRA}
dump_tables()

# build regex patterns, sorting so that longer sequences get matched first
# this ensures that multi-kana lemmas are matched correctly

TO_HIRA_PAT = re.compile(
        "|".join(sorted(TO_HIRA.keys(), key=len, reverse=True)))
FROM_HIRA_PAT = re.compile(
        "|".join(sorted(FROM_HIRA.keys(), key=len, reverse=True)))

IN_PATTERNS = {'hira':TO_HIRA_PAT}
OUT_PATTERNS = {'hira':FROM_HIRA_PAT}