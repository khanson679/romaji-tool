
# import re

# from . import defs
# from . import mapping


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

    def __str__(self):
        return self._name

    def pformat(self):
        return (
            "{}\n"
            "---------------\n"
            "{}\n"
            .format(self._name, self._mapping.pformat)
        )

    @property
    def name(self):
        return self._name

    def inputtable_lemmas(self):
        return self._mapping.inputtable_lemmas()

    def outputtable_lemmas(self):
        return self._mapping.outputtable_lemmas()

    def parse(self, string):
        """
        Return a string converted to the internal representation.
        """
        out = self._mapping.parse(string)
        return out

    def emit(self, string):
        """
        Return a string converted to this format.
        """
        out = self._mapping.emit(string)
        return out


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

    def __str__(self):
        return (
            "{}\n"
            "---------------\n"
            "{}\n"
            .format(str(self._name), str(self._base_map))
        )

    def inputtable_lemmas(self):
        return self._base_map.inputtable_lemmas()

    def outputtable_lemmas(self):
        return self._base_map.outputtable_lemmas()

    def parse(self, string):
        """
        Return a string converted to the internal representation.
        """
        out = string
        for mapping in (self._chouon_map,
                        self._sokuon_map,
                        self._nasal_map,
                        self._base_map):
            out = mapping.parse(out)
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
            out = mapping.emit(out)
        return out
