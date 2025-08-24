#!/usr/bin/env python3

import              ast
from pathlib import Path
import              re

from black import (
    FileMode,
    format_file_in_place,
    format_str,
    WriteBack,
)

from cbutils.core.logconf import *


# --------------- #
# -- CONSTANTS -- #
# --------------- #

PATTERN_PYSUGLIFY = re.compile(r'[\s\-.]+')


# ----------------------- #
# -- BUILD PYTHON CODE -- #
# ----------------------- #

def pysuglify(name):
    return PATTERN_PYSUGLIFY.sub('_', name)


###
# prototype::
#     folder : a folder path.
#
#     :action: add an path::''init__.py'' file to the folder if one
#              does not already exist.
###
def add_missing_init(folder: Path) -> None:
    initfile = folder / INIT_FILE

    if not initfile.is_file():
        initfile.touch()
        initfile.write_text(SHEBANG_PYTHON)

        logging.info(f"{INIT_FILE} file added.")


###
# prototype::
#     code : a \python code.
#     file : a file path.
#
#     :action: creation of the file with the \python code given as
#              a parameter as its content, formatted by the \black
#              package.
###
def add_black_pyfile(
    code: Path,
    file: Path
) -> None:
    file.write_text(code)

    format_file_in_place(
        file,
        fast       = False,
        mode       = FileMode(),
        write_back = WriteBack.YES,
    )


###
# prototype::
#     code    : :see: add_black_pyfile
#     file    : :see: add_black_pyfile
#     nbempty : the number of empty lines added before the code
#               that will be added.
#
#     :action: append to the file the \python code formatted by the
#              \black package.
###
def append_black_pyfile(
    code   : Path,
    file   : Path,
    nbempty: int = 1
) -> None:
    code = format_str(
        code,
        mode = FileMode()
    )
    code = '\n' * nbempty + code
    code = file.read_text() + code

    file.write_text(code)


# ------------------------- #
# -- ANALYZE PYTHON CODE -- #
# ------------------------- #

###
# prototype::
#     file         : a file path.
#     func_name    : a \func name.
#     ignore_error : set to ''True'', this indicates to return
#                    ''None'' if no \func has the given name;
#                    otherwise, a ''ValueError'' is raised.
#
#     :return: the list of its \args in case of success; otherwise,
#              see the \desc of the \arg ''ignore_error''.
###
def get_parse_signature(
    file        : Path,
    func_name   : str,
    ignore_error: bool = False,
) -> list[str] | None:
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

# Not use but useful to get the default values.
#             for i, default in enumerate(node.args.defaults, start=len(args)-len(node.args.defaults)):
#                 args[i] += f"={ast.unparse(default)}"

            return args

    if not ignore_error:
        raise ValueError(
            f"'{func_name}' is not a function of the file:\n{file}"
        )
