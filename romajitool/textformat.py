"""
Classes to organize mapping data into a user-friendly format.
"""


class TextFormat(object):
    """
    Defines mapping between a text format and the internal representation.

    This class is used for simple cases. More difficult cases are handled
    by subclasses.
    """

    def __init__(self, name, mapping):
        """
        name    -- the name of the format
        mapping -- a mapping between this format and internal representation
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
        """
        Returns view of values in mapping from surface to internal rep.
        """
        return self._mapping.inputtable_lemmas()

    def outputtable_lemmas(self):
        """
        Returns view of keys in mapping to format from internal rep.
        """
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
    Defines a mapping between a romanization format and the internal representation.

    Combines several individual mappings to handle sokuon, etc.
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
        return self._name

    def pformat(self):
        raise NotImplementedError

    def inputtable_lemmas(self):
        """
        Returns view of values in mapping from surface to internal rep.
        """
        return self._base_map.inputtable_lemmas()

    def outputtable_lemmas(self):
        """
        Returns view of keys in mapping to format from internal rep.
        """
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


class MultiFormat(TextFormat):
    """
    Format that applies several mappings in sequence.

    Used to parse text containing any combination of hiragana, katakata,
    and a single romanization format. Not useful for output.
    """

    def __init__(self, name, mappings):
        """
        name    -- the name of the format
        mapping -- list of mappings to be applied
        """
        self._name = name
        self._mappings = mappings

    def pformat(self):
        raise NotImplementedError

    def inputtable_lemmas(self):
        raise NotImplementedError

    def outputtable_lemmas(self):
        raise NotImplementedError

    def parse(self, string):
        """
        Return a string converted to the internal representation.
        """
        out = string
        for mapping in self._mappings:
            out = mapping.parse(out)
        return out

    def emit(self, string):
        """
        Return a string converted to this format.
        """
        raise NotImplementedError("MultiFormat not suitable for output.")
