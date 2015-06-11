#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

from defs import *

# from python-romkan
try:
    from functools import cmp_to_key
except ImportError:
    # for python < 3.2; nicked from python 3.2
    def cmp_to_key(mycmp):
        """Convert a cmp= function into a key= function"""
        class K(object):
            __slots__ = ['obj']
            def __init__(self, obj):
                self.obj = obj
            def __lt__(self, other):
                return mycmp(self.obj, other.obj) < 0
            def __gt__(self, other):
                return mycmp(self.obj, other.obj) > 0
            def __eq__(self, other):
                return mycmp(self.obj, other.obj) == 0
            def __le__(self, other):
                return mycmp(self.obj, other.obj) <= 0
            def __ge__(self, other):
                return mycmp(self.obj, other.obj) >= 0
            def __ne__(self, other):
                return mycmp(self.obj, other.obj) != 0
            __hash__ = None
        return K


FORMATS = ("hira", "hira-half", "kata", "kata-half",
    "wapuro", "kunrei", "hepburn", "hepburn-trad")


#
# public functions
#

def convert(in_str, in_fmt, out_fmt, in_opts, out_opts):
    # temporarily hardcode
    in_fmt = "hira"
    out_fmt = "wapuro"

    if in_fmt not in FORMATS:
        raise Exception("Invalid arg for in_fmt: " + in_fmt)
    if out_fmt not in FORMATS:
        raise Exception("Invalid arg for out_fmt: " + out_fmt)

    in_mapping = {"hira":FROM_HIRA}[in_fmt]
    # intermediate = 


#
# init format converstion data
#

LEMMAS_BASIC = LEMMA_TAB_BASIC.split()
LEMMAS_EXTENDED = LEMMA_TAB_EXTENDED.split()

# build mappings

FROM_HIRA = {}
TO_HIRA = {}

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

_len_cmp = lambda x: -len(x)
TO_HIRA_PAT = re.compile("|".join(sorted(TO_HIRA.keys(), key=_len_cmp)) )

def _kanpat_cmp(x, y):
    if len(y) > len(x):
        return 1
    elif len(y) < len(x):
        return -1
    elif len(FROM_HIRA_PAT[x]) > len(FROM_HIRA_PAT[x]):
        return 1
    elif len(FROM_HIRA_PAT[x]) < len(FROM_HIRA_PAT[x]):
        return -1
    else:
        return 0

FROM_HIRA_PAT = re.compile("|".join(sorted(FROM_HIRA.keys(), key=cmp_to_key(_kanpat_cmp))))

KUNREI = [y for (x, y) in pairs(re.split("\s+", KUNREITAB)) ]
HEPBURN = [y for (x, y) in pairs(re.split("\s+", HEPBURNTAB) )]

KUNPAT = re.compile("|".join(sorted(KUNREI, key=_len_cmp)) )
HEPPAT = re.compile("|".join(sorted(HEPBURN, key=_len_cmp)) )

TO_HEPBURN = {}
TO_KUNREI = {}

for kun, hep in zip(KUNREI, HEPBURN):
    TO_HEPBURN[kun] = hep
    TO_KUNREI[hep] = kun

TO_HEPBURN.update( {'ti': 'chi' })