"""Misc. functions to work with dictionaries and collections."""

from collections.abc import Mapping


def all_in(keys, collection):
    """Check if all given keys are present in the given collection/dict."""
    for key in keys:
        if key not in collection:
            return False

    return True


def any_in(keys, collection):
    """Check any of the given keys is present in the given collection/dict."""
    for key in keys:
        if key in collection:
            return True

    return False


def none_in(keys, collection):
    """Check that collection contains none of the given keys."""
    for key in keys:
        if key in collection:
            return False

    return True


def d_key_path_exists(keys, collection):
    """
    Check that the keys given exist recursively.

    First key is expected to be at parent level, second key in the child dict
    of parent and so on. For embedded lists index values like 0, 1, 2 can be
    used as keys.

    Returns a 2-item tuple, where first boolean value indicates if path exists
    or not and second value contains the value present at path or None if
    path does not exist.
    """
    new_c = collection
    for k in keys:
        if isinstance(new_c, Mapping):
            if k not in new_c:
                return (False, None)
        elif isinstance(new_c, (list, tuple)):
            if len(new_c) <= k:
                return (False, None)
        elif new_c is None:
            return (False, None)

        new_c = new_c[k]

    return (True, new_c)


def l_set_val(l_in, v):
    """
    Set a value for a list only if value is not already present.

    If l_in is None then a new list is created.
    """
    if l_in is None:
        l_in = []

    if v not in l_in:
        l_in.append(v)

    return l_in


def dict_set_if_exists(dd, d_key, sd, s_keys):
    """
    Set an item in dictionary dd with key set as d_key if s_keys exist in sd.
    """
    exists, val = d_key_path_exists(s_keys, sd)
    if exists:
        dd[d_key] = val
