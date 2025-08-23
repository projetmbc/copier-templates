#!/usr/bin/env python3

import              ast
from pathlib import Path

from black import (
    FileMode,
    format_file_in_place,
    WriteBack,
)

from cbutils.core.logconf import *


# ----------- #
# -- XXX -- #
# ----------- #

###
# prototype::
#     folder : a folder path.
#
#     :action: X
###
def add_missing_init(folder: Path):
    initfile = folder / INIT_FILE

    if not initfile.is_file():
        initfile.touch()
        initfile.write_text(SHEBANG_PYTHON)

        logging.info(f"{INIT_FILE} file added.")


###
# prototype::
#     code : XX
#     file : XX
#
#     :action: X
###
def add_black_pyfile(
    code: Path,
    file: Path
):
    file.write_text(code)

    format_file_in_place(
        file,
        fast       = False,
        mode       = FileMode(),
        write_back = WriteBack.YES,
    )


###
# prototype::
#     title : X
#     desc  : X
#
#     :action: X
###
def append_black_pyfile(
    code   : Path,
    file   : Path,
    nbempty: int = 1
):
    code = format_str(
        code,
        mode = FileMode()
    )
    code = '\n' * nbempty + code
    code = file.read_text() + code

    file.write_text(code)


# --------------------- #
# -- PYTHON ANALYSIS -- #
# --------------------- #

###
# prototype::
#     title : X
#     desc  : X
#
#     :return: X
###
def get_parse_signature(
    file     : Path,
    func_name: str = "abc"
):
    src_code  = Path(file).read_text()
    tree      = ast.parse(src_code)
    arguments = []

    for node in ast.walk(tree):
        if (
            isinstance(node, ast.FunctionDef)
            and
            node.name == func_name
        ):
            args = [arg.arg for arg in node.args.args]

# # Not use but useful to get the default values.
#             for i, default in enumerate(node.args.defaults, start=len(args)-len(node.args.defaults)):
#                 args[i] += f"={ast.unparse(default)}"

            return args

    return None
