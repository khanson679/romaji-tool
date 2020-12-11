"""
Classes to implement mapping between input/output text and internal
representation.
"""

import re


class Mapping(object):
    """
    Implements bidirectional mapping between input/output text and
    internal representation. Combines bidirectional mapping data with
    unidirectional mapping data and parses/emits text using combined mapping.
    """

    def __init__(self, base_map=None, in_map=None, out_map=None):
        """
        base_map -- a dict containing a bidirectional mapping of
            surface:internal pairs
        in_map -- a dict containing a unidirectional mapping from surface
            to internal rep
        out_map -- a dict containing a unidirectional mapping from internal
            to surface rep

        Contents of `in_map` and `out_map` override `base_map`.
        """
        if base_map is None:
            base_map = {}
        else:
            base_map = dict(base_map)

        if in_map is None:
            in_map = {}
        else:
            in_map = dict(in_map)

        if out_map is None:
            out_map = {}
        else:
            out_map = {lemma: text for text, lemma in out_map}

        inverse_base_map = {lemma: text for text, lemma in base_map.items()}

        self._surface_to_internal = dict(**base_map, **in_map)
        self._internal_to_surface = dict(**inverse_base_map, **out_map)

        self._parse_pattern = re.compile(
            "|".join(sorted(list(self._surface_to_internal.keys()),
                            key=len,
                            reverse=True)),
            flags=re.IGNORECASE)
        self._emit_pattern = re.compile(
            "|".join(sorted(list(self._internal_to_surface.keys()),
                            key=len,
                            reverse=True)),
            flags=re.IGNORECASE)

    def pformat(self):
        return (
            "{}\n"
            "\n"
            "{}\n"
            .format(
                ",  ".join(" ".join(pair) for pair in self._surface_to_internal.items()),
                ",  ".join(" ".join(pair) for pair in self._internal_to_surface.items()))
        )

    def inputtable_lemmas(self):
        """
        Returns view of values in mapping from surface to internal rep.
        """
        return self._surface_to_internal.values()

    def outputtable_lemmas(self):
        """
        Returns view of keys in mapping to format from internal rep.
        """
        return self._internal_to_surface.keys()

    def accepted_substrings(self):
        """
        Returns view of keys in mapping from format to internal rep.
        """
        return self._surface_to_internal.keys()

    def produced_substrings(self):
        """
        Returns view of values in mapping to surface from internal rep.
        """
        return self._internal_to_surface.values()

    def match_surface(self, string):
        """
        Returns True if entire string can be matched by surface format,
        False otherwise.
        """
        return re.match(pattern=self._parse_pattern,
                        string=string)

    def match_internal(self, string):
        """
        Returns True if entire string can be matched by internal format,
        False otherwise.
        """
        return re.match(pattern=self._emit_pattern,
                        string=string)

    def parse(self, string):
        """
        Return a string (partially) converted to the internal representation.
        """
        return re.sub(pattern=self._parse_pattern,
                      repl=lambda x: self._surface_to_internal[x.group(0).lower()],
                      string=string)

    def emit(self, string):
        """
        Return a string (partially) converted to output format.
        """
        return re.sub(pattern=self._emit_pattern,
                      repl=lambda x: self._internal_to_surface[x.group(0).upper()],
                      string=string)


class ContextualMapping(object):
    """
    Implments mapping between a single surface and internal representation
    that is depended on context.
    """

    def __init__(self, surface, internal, context):
        self._surface = surface
        self._internal = internal
        self._context = context

        self._parse_pattern = re.compile("{}(?={})".format(surface, context),
                                         flags=re.I)
        self._emit_pattern = re.compile("{}(?={})".format(internal, context),
                                        flags=re.I)

    def parse(self, string):
        return re.sub(self._parse_pattern, self._internal, string)

    def emit(self, string):
        return re.sub(self._emit_pattern, self._surface, string)
