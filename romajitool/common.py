#!/usr/bin/env python

from . import defs
# from . import textformat

IN_FORMATS = ["hiragana", "katakana", "nihon", "kunrei", "hepburn",
              "hepburn-strict", "hepburn-plus-kana"]
OUT_FORMATS = ["hiragana", "katakana", "nihon", "kunrei", "hepburn",
               "hepburn-strict"]

_name_to_fmt = {"hiragana": defs.HIRAGANA,
                "katakana": defs.KATAKANA,
                "nihon": defs.NIHON,
                "kunrei": defs.KUNREI,
                "hepburn": defs.HEPBURN,
                "hepburn-strict": defs.HEPBURN_STRICT,
                "hepburn-plus-kana": defs.HEPBURN_PLUS_KANA}


#
# public functions
#

def convert(in_str, in_fmt, out_fmt, in_opts=None, out_opts=None):
    """
    Convert `in_str` from the specified input format to the specified output format
    via an internal representation.
    """

    if in_opts is None:
        in_opts = []
    if out_opts is None:
        out_opts = []

    # load formats
    if in_fmt not in IN_FORMATS:
        raise ValueError("in_fmt must be one of: {}."
                         " Got '{}' instead.".format(IN_FORMATS, in_fmt))
    if out_fmt not in OUT_FORMATS:
        raise ValueError("out_fmt must be one of: {}."
                         " Got '{}' instead.".format(OUT_FORMATS, out_fmt))
    in_format = _name_to_fmt[in_fmt]
    out_format = _name_to_fmt[out_fmt]

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
    """
    Print contents of loaded data.
    """
    print("Lemma List",
          "--------------------",
          ",  ".join(defs.LEMMAS),
          "Total: {}".format(len(defs.LEMMAS)),
          sep='\n', end="\n\n")

    print(str(_name_to_fmt["hiragana"]).encode('utf-8'))

    print(str(_name_to_fmt["wapuro"]).encode('utf-8'))
