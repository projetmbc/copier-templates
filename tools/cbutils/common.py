#!/usr/bin/env python3

from pathlib import Path

from cbutils.core.common import *


# --------------- #
# -- CONSTANTS -- #
# --------------- #

TAG_DEBUG_FOLDER = 'x-debug-x/'


# ----------- #
# -- TOOLS -- #
# ----------- #

def is_debug_folder(
    path      : Path,
    copier_dir: Path
) -> bool:
    global TAG_DEBUG_FOLDER

    relpath = get_relpath(
        path       = path,
        copier_dir = copier_dir
    )

    return str(relpath).startswith(TAG_DEBUG_FOLDER)
