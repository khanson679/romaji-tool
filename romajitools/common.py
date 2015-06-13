#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function

import re

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


#
# init format converstion data
#

LEMMAS_BASIC = LEMMA_TAB_BASIC.split()
LEMMAS_EXTENDED = LEMMA_TAB_EXTENDED.split()

# build mappings

FROM_HIRA = {}
IN_MAPPINGS = {"hira":FROM_HIRA}

TO_HIRA = {}
OUT_MAPPINGS = {"hira":TO_HIRA}

for hira, lemma in pairs(HIRAGANA_TAB.split()):
    FROM_HIRA[hira] = lemma
    TO_HIRA[lemma] = hira

    # add sokuon, if applicable
    # ex. ka -> kka   but not wa -> wwa
    if lemma[0] in SOKUON_CONSONANTS:
        sokuon_lemma = lemma[0] + lemma
        sokuon_hira = HIRAGANA_SOKUON + hira
        FROM_HIRA[sokuon_hira] = sokuon_lemma
        TO_HIRA[sokuon_lemma] = sokuon_hira

# validate table
for lemma in TO_HIRA:
    if lemma not in LEMMAS_BASIC and lemma not in LEMMAS_EXTENDED:
        raise Exception("Lemma for entry {},{} in hiragana table"
                        " not in lemma list.".format(hira, lemma))


# build regex patterns, sorting so that longer sequences get matched first
# this ensures that multi-kana lemmas are matched correctly

TO_HIRA_PAT = re.compile("|".join(
                         sorted(TO_HIRA.keys(), key=len, reverse=True)))
FROM_HIRA_PAT = re.compile("|".join(
                           sorted(FROM_HIRA.keys(), key=len, reverse=True)))

IN_PATTERNS = {'hira':TO_HIRA_PAT}
OUT_PATTERNS = {'hira':FROM_HIRA_PAT}