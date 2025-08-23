#!/usr/bin/env python3

from pathlib import Path

from cbutils.core.logconf import *


# ----------- #
# -- XXX -- #
# ----------- #

###
# prototype::
#     title : X
#     desc  : X
###
def add_missing_init(srcdir):
    # Nothing left expect the addition of an ''__init__.py'' file.
    initfile = srcdir / INIT_FILE

    if not initfile.is_file():
        initfile.touch()
        initfile.write_text(INIT_CONTENT)

        logging.info("__init__.py file added.")


###
# prototype::
#     title : X
#     desc  : X
###
def add_black_pyfile(
    code,
    file
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
###
def append_black_pyfile(
    code,
    file,
    nbempty = 1
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
###
def get_parse_signature(
    file,
    func_name
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

            # for i, default in enumerate(node.args.defaults, start=len(args)-len(node.args.defaults)):
            #     args[i] += f"={ast.unparse(default)}"

            return args

    return None
