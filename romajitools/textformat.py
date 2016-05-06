# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import re

import defs
import mapping

class TextFormat(object):
    """
    Defines mapping from a Kana or romanization format to the internal representation.
    """

    def __init__(self, name, mapping):
        """
        name    -- the name of the format
        mapping -- a mapping from this format to the underlying representation
        """
        self._name = name
        self._mapping = mapping

    def __unicode__(self):
        return (
            "{}\n"
            "---------------\n"
            "{}\n"
            .format(unicode(self._name), unicode(self.mapping))
        )

    @property
    def name(self):
        return self._name
    
    def accepted_lemmas(self):
        return self._mapping.accepted_internal_substrings()

    def produced_lemmas(self):
        return self._mapping.produced_internal_substrings()

    def parse(self, string):
        """
        Return a string converted to the internal representation.
        """
        return self._mapping.parse(string)

    def emit(self, string):
        """
        Return a string converted to this format.
        """
        return self._mapping.emit(string)


class RomajiFormat(TextFormat):
    """
    Defines a mapping from a romanization format to the internal representation.

    Handles sokuon, etc.
    """

    def __init__(self, name, base, nasal, sokuon, chouon):
        """
        Build format from the given lists of Mappings.

        Moras that are not handled will be unchanded during conversion.
        
        base -- base moras and you-on
        nasal -- nasal mora with preceding consonants
        sokuon -- sokuon moras with proceding consonants
        chouon -- chou-on mark with preceding vowels
        """
        self._name = name
        self._base_map = base
        self._nasal_map = nasal
        self._sokuon_map = sokuon
        self._chouon_map = chouon

    def accepted_lemmas(self):
        return self._base_map.accepted_internal_substrings()

    def produced_lemmas(self):
        return self._base_map.produced_internal_substrings()

    def parse(self, string):
        """
        Return a string converted to the internal representation.
        """
        out = string
        for mapping in (self._chouon_map,
                        self._sokuon_map,
                        self._nasal_map,
                        self._base_map):
            out = mapping.parse(string)
        return out

    def emit(self, string):
        """
        Return a string converted to this format.
        """
        out = string
        for mapping in (self._base_map,
                        self._nasal_map,
                        self._sokuon_map,
                        self._chouon_map):
            out = mapping.emit(string)
        return out


#
# init text formats
#

WAPURO   = TextFormat("Wapuro", mapping.Mapping())
HIRAGANA = TextFormat("Hiragana", mapping.Mapping(defs.HIRAGANA_TAB))
NIHON    = RomajiFormat("Nihon",
                        mapping.Mapping(defs.MORAS_NIHON),
                        mapping.Mapping(defs.NASAL_BASE),
                        mapping.Mapping(defs.SOKUON_BASE),
                        mapping.Mapping(defs.CHOUON_DOUBLE_VOWEL))
