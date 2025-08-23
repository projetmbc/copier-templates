#!/usr/bin/env python3

from pathlib import Path

from cbutils.core.logconf import *


# ----------- #
# -- PATHS -- #
# ----------- #

###
# prototype::
#     title : X
#     desc  : X
###
def get_relpath(
    path      : Path,
    copier_dir: Path
) -> bool:
    return path.relative_to(copier_dir)


# ------------------------------ #
# -- CREATION, DELETION & CO. -- #
# ------------------------------ #

###
# prototype::
#     title : X
#     desc  : X
###
def add_missing_dir(path : Path) -> None:
    if not path.is_dir():
        path.mkdir(
            parents  = True,
            exist_ok = True
        )

        logging.warning(f"Folder added: '{path}'")


###
# prototype::
#     title : X
#     desc  : X
###
def empty_dir(path : Path) -> None:
    add_missing_dir(path)

    if path.is_dir():
        logging.warning(f"Emptying folder: '{path}'")

        for root, dirs, files in path.walk(top_down = False):
            for name in files:
                (root / name).unlink()
            for name in dirs:
                (root / name).rmdir()
