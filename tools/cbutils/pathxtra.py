#!/usr/bin/env python3

from pathlib import Path

from cbutils.core.pathplus import *


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
        subpath  = path,
        mainpath = copier_dir
    )

    return str(relpath).startswith(TAG_DEBUG_FOLDER)
