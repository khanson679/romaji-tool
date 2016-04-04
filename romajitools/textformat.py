# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import re


class TextFormat(object):
    """
    Defines mapping from a Kana or romanization format to the internal representation.
    """

    def __init__(self, name, base_map, from_map=None, to_map=None):
        """
        name     -- the name of the format
        base_map -- a dict containing bidirectional mapping, as text:lemma pairs
        from_map -- a dict containing unidirectional mapping from this format to internal rep
        to_map   -- a dict containing unidirectional mapping to this format from internal rep

        Contents of `from_map` and `to_map` override `base_map`.
        """
        if from_map is None:
            from_map = {}
        if to_map is None:
            to_map = {}

        inverse_base_map = {lemma:text for text, lemma in base_map.iteritems()}

        self._name = name
        self._moras_to_lemmas = dict(base_map, **from_map)
        self._lemmas_to_moras = dict(inverse_base_map, **to_map)
        
        self._parse_pattern = None
        self._emit_pattern = None

    def __unicode__(self):
        return "{}\n\n{}\n\n{}\n".format(
                unicode(self._name),
                ",  ".join(" ".join(pair) for pair in self._moras_to_lemmas.iteritems()),
                ",  ".join(" ".join(pair) for pair in self._lemmas_to_moras.iteritems()))

    @classmethod
    def from_string(cls, name, base_table, from_table=None, to_table=None):
        """
        Read mapping tables and return an object constructed from those tables.
        """
        base_map = cls._read_table(base_table)
        from_map = cls._read_table(from_table) if from_table is not None else None
        to_map = cls._read_table(to_table) if from_table is not None else None

        return cls(name, base_map, to_map, from_map)


    @staticmethod
    def _read_table(table):
        """
        Take a table of the form "repr lemma, repr lemma, ..."
        and return a dictionary of representations to lemmas.

        Split on commas (ignoring adjacent whitespace), then on spaces.
        """
        entry_str_list = re.split("\s*,\s*", table)
        entry_dict = dict([entry.split() for entry in entry_str_list])
        return entry_dict


    @property
    def parse_pattern(self):
        """
        Return a regex pattern for union of the base map and "to" map.

        Sorted so that longer sequences get matched first.
        This ensures that multi-kana moras are matched correctly.
        """
        if self._parse_pattern is None:
            self._parse_pattern = re.compile(
            "|".join(sorted(self._moras_to_lemmas.keys(), key=len, reverse=True)))
        return self._parse_pattern


    @property
    def emit_pattern(self):
        """
        Return a regex pattern for union of the base map and "to" map.

        Sorted so that longer sequences get matched first.
        This ensures that multi-kana lemmas are matched correctly.
        """
        if self._emit_pattern is None:
            self._emit_pattern = re.compile(
            "|".join(sorted(self._lemmas_to_moras.keys(), key=len, reverse=True)))
        return self._emit_pattern


    def accepted_moras(self):
        """
        Returns iterator over list of keys in mapping from format to internal rep.
        """
        return self._moras_to_lemmas.iterkeys()


    def accepted_lemmas(self):
        """
        Returns iterator over list of keys in mapping to format from internal rep.
        """
        return self._lemmas_to_moras.iterkeys()


    def produced_moras(self):
        """
        Returns iterator over list of values in mapping to format from internal rep.
        """
        return self._lemmas_to_moras.itervalues()


    def produced_lemmas(self):
        """
        Returns iterator over list of values in mapping from format to internal rep.
        """
        return self._moras_to_lemmas.itervalues()


    def match(self, string):
        """
        Returns True if string matches format, False otherwise.
        """
        return re.match(pattern=self.parse_pattern,
                        string=string)


    def parse(self, string):
        """
        Return a string converted to the internal representation.
        """
        return re.sub(pattern=self.parse_pattern,
                      repl=lambda x: self._moras_to_lemmas[x.group(0)],
                      string=string)


    def emit(self, string):
        """
        Return a string converted to this format.
        """
        return re.sub(pattern=self.emit_pattern,
                      repl=lambda x: self._lemmas_to_moras[x.group(0)],
                      string=string)
