#!/usr/bin/env python3

from pathlib import Path


# --------------- #
# -- CONSTANTS -- #
# --------------- #

TAG_DEBUG_FOLDER = 'x-debug-x/'


# ----------- #
# -- TOOLS -- #
# ----------- #

def get_relpath(
    path      : Path,
    copier_dir: Path
) -> bool:
    return path.relative_to(copier_dir)


def is_debug(
    path      : Path,
    copier_dir: Path
) -> bool:
    global TAG_DEBUG_FOLDER

    relpath = get_relpath(
        path       = path,
        copier_dir = copier_dir
    )

    return str(relpath).startswith(TAG_DEBUG_FOLDER)
