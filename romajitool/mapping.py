# -*- coding: utf-8 -*-

import re

from . import util


class Mapping(object):
    """
    Defines mapping from a surface string to the internal representation.
    """

    def __init__(self, base_map=None, in_map=None, out_map=None):
        """
        base_map -- a dict containing a bidirectional mapping of surface:internal pairs
        in_map -- a dict containing a unidirectional mapping from surface to internal rep
        out_map -- a dict containing a unidirectional mapping from internal to surface rep

        Contents of `in_map` and `out_map` override `base_map`.
        """
        if base_map is None:
            base_map = {}
        if in_map is None:
            in_map = {}
        if out_map is None:
            out_map = {}

        inverse_base_map = {lemma: text for text, lemma in base_map.items()}
        out_map = {lemma: text for text, lemma in out_map.items()}

        self._surface_to_underlying = dict(**base_map, **in_map)
        self._underlying_to_surface = dict(**inverse_base_map, **out_map)

        self._parse_pattern = re.compile(
            "|".join(sorted(list(self._surface_to_underlying.keys()),
                            key=len, reverse=True)))
        self._emit_pattern = re.compile(
            "|".join(sorted(list(self._underlying_to_surface.keys()),
                            key=len, reverse=True)))

    def __str__(self):
        return (
            "{}\n"
            "\n"
            "{}\n"
            .format(
                ",  ".join(" ".join(pair) for pair in self._surface_to_underlying.items()),
                ",  ".join(" ".join(pair) for pair in self._underlying_to_surface.items()))
        )

    def accepted_surface_substrings(self):
        """
        Returns iterator over list of keys in mapping from format to internal rep.
        """
        return iter(self._surface_to_underlying.keys())

    def accepted_internal_substrings(self):
        """
        Returns iterator over list of keys in mapping to format from internal rep.
        """
        return iter(self._underlying_to_surface.keys())

    def produced_surface_substrings(self):
        """
        Returns iterator over list of values in mapping to surface from internal rep.
        """
        return iter(self._underlying_to_surface.values())

    def produced_internal_substrings(self):
        """
        Returns iterator over list of values in mapping from surface to internal rep.
        """
        return iter(self._surface_to_underlying.values())

    def match_surface(self, string):
        """
        Returns True if entire string can be matched by surface format, False otherwise.
        """
        return re.match(pattern=self._parse_pattern,
                        string=string)

    def match_underlying(self, string):
        """
        Returns True if entire string can be matched by internal format, False otherwise.
        """
        return re.match(pattern=self._emit_pattern,
                        string=string)

    def parse(self, string):
        """
        Return a string (partially) converted to the internal representation.
        """
        return re.sub(pattern=self._parse_pattern,
                      repl=lambda x: self._surface_to_underlying[x.group(0)],
                      string=string)

    def emit(self, string):
        """
        Return a string (partially) converted to surface representation.
        """
        return re.sub(pattern=self._emit_pattern,
                      repl=lambda x: self._underlying_to_surface[x.group(0)],
                      string=string)
