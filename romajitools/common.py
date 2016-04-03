#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function

from defs import *
from util import *
from textformat import TextFormat

FORMATS = ("hira", "hira-half", "kata", "kata-half",
    "wapuro", "kunrei", "hepburn", "hepburn-trad")


#
# public functions
#

def convert(in_str, in_fmt, out_fmt, in_opts=None, out_opts=None):
    """
    Convert `in_str` from the specified input format to the specified output format
    via an internal representation.
    """

    if in_opts == None:
        in_opts = []
    if out_opts == None:
        out_opts = []

    # load formats
    try:
        in_format = FORMATS[in_fmt]
    except KeyError:
        raise ValueError("in_fmt must be one of: {}."
                         " Got '{}' instead.".format(FORMATS, in_fmt))
    try:
        out_format = FORMATS[out_fmt]
    except KeyError:
        raise ValueError("out_fmt must be one of: {}."
                         " Got '{}' instead.".format(FORMATS, out_fmt))

    # map to output format
    intermediate = in_format.parse(in_str)
    out_str = out_format.emit(intermediate).lower()

    return out_str


# def to_wapuro(in_str):
#     """
#     Convert any format to wapuro romaji.
#     """
#     return convert(in_str, "hiragana", "wapuro")


#
# Debug functions
#

def dump_tables():
    print("--------------------",
          "Lemma Table - Full",
          "--------------------",
          ",  ".join(LEMMAS),
          "Total: {}".format(len(LEMMAS)),
          sep='\n')

    # print("--------------------"
    #       "Lemma Table - Basic"
    #       "--------------------")
    # print(LEMMAS_BASIC)
    # print("Total:", len(LEMMAS_BASIC))

    # print("--------------------"
    #       "Lemma Table - Extended"
    #       "--------------------")
    # print(LEMMAS_EXTENDED)
    # print("Total:", len(LEMMAS_EXTENDED))

    # print("--------------------"
    #       "Lemma Table - Extra"
    #       "--------------------")
    # print(LEMMAS_EXTRA)
    # print("Total:", len(LEMMAS_EXTRA))

    print("--------------------"
          "Hiragana Table"
          "--------------------")
    print(unicode(FORMATS["hiragana"]).encode('utf-8'))


#
# init lemma data
#

LEMMAS_BASIC    = LEMMA_TAB_BASIC.split()
LEMMAS_EXTENDED = LEMMA_TAB_EXTENDED.split()
LEMMAS_EXTRA    = LEMMA_TAB_EXTRA.split()
LEMMAS_SMALL_KANA_POST = LEMMA_TAB_SMALL_KANA_POST.split()
LEMMAS = (LEMMAS_BASIC + LEMMAS_EXTENDED + LEMMAS_EXTRA +
        LEMMAS_SMALL_KANA_POST + [LEMMA_SOKUON, LEMMA_CHOUON])


#
# build formats
#

FORMATS = {"hiragana" : TextFormat.from_string("Hiragana", HIRAGANA_TAB),
           "wapuro"   : TextFormat.from_string("Wapuro", WAPURO_TAB)}
