#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Definitions for mapping between kana/romaji and an internal representation.
"""


from . import util
from . import data
from .mapping import Mapping, ContextualMapping
from .textformat import TextFormat, RomajiFormat, MultiFormat


#
# Lemmas
#
# These are unambiguous representations of one or more kana,
#   essentially wapuro-style Kunrei-shiki.
# Implementated as space-separated lists, which can be easily parsed
#   into lists of strings.
#

LEMMAS_BASE = data.LEMMA_TAB_BASE.split()
LEMMAS_BORROWED = data.LEMMA_TAB_EXTENDED.split()
LEMMAS_ARCHAIC = data.LEMMA_TAB_ARCHAIC.split()
LEMMAS_RARE = data.LEMMA_TAB_RARE.split()
LEMMAS_SMALL_KANA = data.LEMMA_TAB_SMALL_KANA.split()

LEMMAS_STANDARD = LEMMAS_BASE + LEMMAS_BORROWED
LEMMAS_ALL = LEMMAS_STANDARD + LEMMAS_ARCHAIC + LEMMAS_RARE + LEMMAS_SMALL_KANA


#
# Mappings
#

HIRAGANA_MAP = util.read_table(data.HIRAGANA_TAB)
KATAKANA_MAP = util.read_table(data.KATAKANA_TAB)

# ROMAJI_MAP_BASE = util.read_table(data.ROMAJI_TAB_BASE)
ROMAJI_MAP_NIHON = util.read_table(data.NIHON_TAB)
ROMAJI_MAP_KUNREI = util.read_table(data.KUNREI_TAB)
ROMAJI_MAP_KUNREI_OUTONLY = util.read_table(data.KUNREI_TAB_OUTONLY)
ROMAJI_MAP_HEPBURN = util.read_table(data.HEPBURN_TAB)
ROMAJI_MAP_HEPBURN_OUTONLY = util.read_table(data.HEPBURN_TAB_OUTONLY)
ROMAJI_MAP_HEPBURN_EXTENDED = util.read_table(data.ROMAJI_TAB_HEPBURN_EXTENDED)
ROMAJI_MAP_HEPBURN_EXTRA = util.read_table(data.ROMAJI_TAB_HEPBURN_EXTRA)
ROMAJI_MAP_HEPBURN_EXTRA_OUTONLY = util.read_table(data.ROMAJI_TAB_HEPBURN_EXTRA_OUTONLY)

SOKUON_MAP_BASE = util.read_table(data.SOKUON_TAB_BASE)
SOKUON_MAP_HEPBURN = util.read_table(data.SOKUON_TAB_HEPBURN)
SOKUON_MAP_HEPBURN_EXTENDED = util.read_table(data.SOKUON_TAB_HEPBURN_EXTENDED)
SOKUON_MAP_HEPBURN_ALTERNATE = util.read_table(data.SOKUON_TAB_HEPBURN_ALTERNATE)

CHOUON_MAP_MACRON = util.read_table(data.CHOUON_MACRON)
CHOUON_MAP_CIRCUMFLEX = util.read_table(data.CHOUON_CIRCUMFLEX)
CHOUON_MAP_DOUBLE_VOWEL = util.read_table(data.CHOUON_DOUBLE_VOWEL)

# NASAL_MAP_BASE = util.read_table(data.NASAL_BASE)
# NASAL_MAP_EXTENDED = util.read_table(data.NASAL_EXTENDED)
# NASA_MAP_ALTERNATE = util.read_table(data.NASAL_ALTERNATE)

NASAL_MAP_DEFAULT = ContextualMapping("n", "N'", "[KGSZRDNHBPMRW]|$")
NASAL_MAP_MOD_HEP_N = ContextualMapping("n", "N'", "[KGSZRDNHRW]|$")
NASAL_MAP_MOD_HEP_M = ContextualMapping("m", "N'", "[BPM]|$")


#
# Text Formats
#

HIRAGANA = TextFormat("Hiragana", Mapping(HIRAGANA_MAP))
KATAKANA = TextFormat("Hiragana", Mapping(KATAKANA_MAP))

# WAPURO = TextFormat("Wapuro", Mapping())

NIHON = RomajiFormat(
    "Nihon",
    Mapping(ROMAJI_MAP_NIHON),
    NASAL_MAP_DEFAULT,
    Mapping(SOKUON_MAP_BASE),
    Mapping(CHOUON_MAP_CIRCUMFLEX))

KUNREI = RomajiFormat(
    "Kunrei",
    Mapping(ROMAJI_MAP_KUNREI, out_map=ROMAJI_MAP_KUNREI_OUTONLY),
    NASAL_MAP_DEFAULT,
    Mapping(SOKUON_MAP_BASE),
    Mapping(CHOUON_MAP_CIRCUMFLEX))

HEPBURN_STRICT = RomajiFormat(
    "Hepburn Strict",
    Mapping(ROMAJI_MAP_HEPBURN, out_map=ROMAJI_MAP_HEPBURN_OUTONLY),
    NASAL_MAP_DEFAULT,
    Mapping(SOKUON_MAP_BASE + SOKUON_MAP_HEPBURN),
    Mapping(CHOUON_MAP_MACRON))

HEPBURN = RomajiFormat(
    "Hepburn",
    Mapping(ROMAJI_MAP_HEPBURN + ROMAJI_MAP_HEPBURN_EXTENDED
            + ROMAJI_MAP_HEPBURN_EXTRA,
            out_map=ROMAJI_MAP_HEPBURN_OUTONLY + ROMAJI_MAP_HEPBURN_EXTRA_OUTONLY),
    NASAL_MAP_DEFAULT,
    Mapping(SOKUON_MAP_BASE + SOKUON_MAP_HEPBURN + SOKUON_MAP_HEPBURN_EXTENDED),
    Mapping(CHOUON_MAP_MACRON))

# special format for mixed kana + romaji input
HEPBURN_PLUS_KANA = MultiFormat("Any", [
    Mapping(HIRAGANA_MAP),
    Mapping(KATAKANA_MAP),
    Mapping(ROMAJI_MAP_HEPBURN + ROMAJI_MAP_HEPBURN_EXTENDED
            + ROMAJI_MAP_HEPBURN_EXTRA,
            out_map=ROMAJI_MAP_HEPBURN_OUTONLY + ROMAJI_MAP_HEPBURN_EXTRA_OUTONLY),
    NASAL_MAP_DEFAULT,
    Mapping(SOKUON_MAP_BASE + SOKUON_MAP_HEPBURN + SOKUON_MAP_HEPBURN_EXTENDED),
    Mapping(CHOUON_MAP_MACRON)])

ALL_FORMATS = [HIRAGANA, KATAKANA, NIHON, KUNREI, HEPBURN_STRICT, HEPBURN]
