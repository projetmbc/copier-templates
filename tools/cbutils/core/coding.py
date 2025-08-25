#!/usr/bin/env python3

from pathlib import Path
import              re

from cbutils.core.constants import *
from cbutils.core.logconf   import *


# ------------ #
# -- TYPING -- #
# ------------ #

type NestedDictPath = dict[str, Path | NestedDictPath]


# -------------------- #
# -- SPLIT IN PARTS -- #
# -------------------- #

###
# prototype::
#     file        : YYY
#     pat_headers : YYY
#     strip_parts : YYY
#
#     :return: YYY
###
def split_in_parts(
    file       : Path,
    pat_headers: list[re.Pattern],
    strip_parts: bool = True,
) -> NestedDictPath:
    return _recu_split_in_parts(
        content     = file.read_text(),
        pat_headers = pat_headers,
        strip_parts = strip_parts,
    )


###
# prototype::
#     content     : YYY
#     pat_headers : :see: split_in_parts
#     strip_parts : :see: split_in_parts
#
#     :return: YYY
###
def _recu_split_in_parts(
    content    : str,
    pat_headers: list[re.Pattern],
    strip_parts: bool,
) -> NestedDictPath:
# No pattern.
    if not pat_headers:
        return content

# One pattern.
    parts = dict()
    curhd = TAG_ROOT_HEADER # Current header.

    pattern, *other_patterns = pat_headers

    for i, piece in enumerate(pattern.split(content)):
        if i % 2 == 1:
            curhd = piece.strip()

        else:
            if strip_parts:
                piece = piece.strip()

            parts[curhd] = _recu_split_in_parts(
                content     = piece,
                pat_headers = other_patterns,
                strip_parts = strip_parts,
            )

# Nothing left to do.
    return parts
