#!/usr/bin/env python3

from pathlib import Path

from cbutils.core.log_conf import *


# ----------- #
# -- PATHS -- #
# ----------- #

def get_relpath(
    path      : Path,
    copier_dir: Path
) -> bool:
    return path.relative_to(copier_dir)


# --------------------- #
# -- FOLDERS / FILES -- #
# --------------------- #

def add_missing_dir(path : Path) -> None:
    if not path.is_dir():
        path.mkdir(
            parents  = True,
            exist_ok = True
        )

        logging.warning(f"Folder added: '{path}'")

def remove_dir(path : Path) -> None:
    if path.is_dir():
        logging.warning(f"Removed: '{path}'")

        for root, dirs, files in path.walk(top_down = False):
            for name in files:
                (root / name).unlink()
            for name in dirs:
                (root / name).rmdir()
