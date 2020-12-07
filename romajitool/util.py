
import re


def read_table(tablestr):
    """
    Take a table of the form "repr lemma, repr lemma, ..."
    and return a dictionary of representations to lemmas.

    Split on commas (ignoring adjacent whitespace), then on spaces.
    """
    entry_str_list = re.split(r"\s*,\s*", tablestr)
    entry_list = [entry.split() for entry in entry_str_list]
    return entry_list


def join_maps_at_shared_char(prefixmap, suffixmap):
    """
    Given a list of 2-tuples of strings, yields a generator for all combinations
        where there is exactly one shared character at the concatenation point.

    >>> list(join_overlapping([("ab", "AB")], [("bc", "BC")]))
    [("ac", "AC")]
    """
    for pre_surface, pre_underlying in prefixmap:
        for suf_surface, suf_underlying in suffixmap:
            comb_surface = join_at_shared_char(pre_surface, suf_surface)
            comb_underlying = join_at_shared_char(pre_underlying, suf_underlying)
            if comb_surface is not None and comb_underlying is not None:
                yield (comb_surface, comb_underlying)


def join_at_shared_char(s1, s2):
    return "".join((s1[:-1], s2[1:])) if s1[-1] == s2[0] else None
