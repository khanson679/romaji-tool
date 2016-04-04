#!/usr/bin/env python

from __future__ import unicode_literals
from __future__ import print_function

import defs
import textformat


FORMATS = {"hiragana" : textformat.HIRAGANA,
           "wapuro"   : textformat.WAPURO}


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
          ",  ".join(defs.LEMMAS),
          "Total: {}".format(len(defs.LEMMAS)),
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
