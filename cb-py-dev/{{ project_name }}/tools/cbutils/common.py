#!/usr/bin/env python3

###
# note::
#     The command term::''python -m rich.color'' shows the 256 colors
#     available with their ''rich'' name.
###

from typing import Any

import              ast
from copy    import copy
from pathlib import Path
import              re

import           tomli
from yaml import safe_load

from black import (
    format_str,
    format_file_in_place,
    FileMode,
    WriteBack
)


# --------------- #
# -- CONSTANTS -- #
# --------------- #

TAG_CONSTANTS = "constants"
TAG_SIGNS     = "signatures"
TAG_SPECS     = "specs"
TAG_FLAVOURS  = "flavours"

CONSTANTS_FILE = f"{TAG_CONSTANTS}.py"
SIGNS_FILE     = f"{TAG_SIGNS}.py"
SPECS_FILE     = f"{TAG_SPECS}.py"
FLAVOURS_FILE  = f"{TAG_FLAVOURS}.py"

TAG_OPTIONAL   = '*'

META_TAGS = [
    TAG_SPECS_ALT_ALL   := "__ALT_ALL__",
    TAG_SPECS_ALT_TUPLES:= "__ALT_TUPLES__",
    TAG_SPECS_BLOCK     := "__BLOCK__",
    TAG_SPECS_CONTENT   := "__CONTENT__",
    TAG_SPECS_DATA      := "__DATA__",
    TAG_SPECS_LIST_OF   := "__LIST_OF__",
    TAG_SPECS_MAPPER    := "__MAPPER__",
    TAG_SPECS_PARSER    := "__PARSER__",
    TAG_SPECS_REQUIRED  := "__REQUIRED__",
    TAG_SPECS_OPTIONAL  := "__OPTIONAL__",
    TAG_SPECS_TOOLS     := "__TOOLS__",
    TAG_SPECS_TYPE      := "__TYPE__",
]

# --------------- #
# -- TEMPLATES -- #
# --------------- #

TEMPL_CODE_HEADER = """
#!/usr/bin/env python3

# ------------------------------------------------------- #
# -- File created automatically from YAML spec. files. -- #
# --                                                   -- #
# -- Formatting done by the Python project "black".    -- #
# ------------------------------------------------------- #
""".strip()


# ---------------------- #
# -- LOGGING MESSAGES -- #
# ---------------------- #

def raise_validation_error(
    key,
    yfile_name,
    desc,
    xtra = ""
):
    if key:
        key = f"'{key}' key in "

    desc = f"See {key}'{yfile_name}' file: {desc}"

    logging.error(
        msg_title(
            TAG_BAD_VALIDATION,
            desc = desc
        )
    )

    if xtra:
        xtra = f" {xtra}"

    raise ValueError(f"{desc}{xtra}")


# ----------- #
# -- PATHS -- #
# ----------- #

def get_specs_folders(
    context,
    this_dir,
    contrib_dir_name,
    nbtest,
    subfolder = "code",
):
    projdir  = this_dir.parent.parent
    projname = projdir.name

    contribdir = projdir / "contrib" / contrib_dir_name / subfolder
    statusdir  = contribdir.parent / "status"
    srcdir     = projdir / "src" / projname / TAG_SPECS / context
    testsdir   = projdir / "tests" / f"{nbtest:02d}-{context}"

    return (
        projdir,
        projname,
        contribdir,
        statusdir,
        srcdir,
        testsdir
    )


# WARNING!
# "No status" ==> "No parser to add"
def get_accepted_paths(
    context,
    contribdir,
    statusdir,
    subfolder = "",
    ext       = 'py',
):
    logging.info(
        f"{context.upper()} - Looking for accepted contribs."
    )

    files = []

    if subfolder:
        subfolder += "/"

    for yaml_file in statusdir.glob(
        f"{subfolder}*.yaml"
    ):
        statusdata = safe_load(yaml_file.read_text())

        if statusdata[TAG_STATUS] != TAG_OK:
            continue

        file = contribdir / f"{yaml_file.stem}.{ext}"

        if not file.is_file():
            raise IOError(f"missing file:\n{file}")

        files.append(file)

    files.sort()

    return files


# --------------------- #
# -- PYTHON ANALYSIS -- #
# --------------------- #

def get_metatags(
    allvars,
    vals = META_TAGS
):
    return [
        vname
        for vname in allvars
        if allvars[vname] in vals
    ]


def code_with_metatags(
    allvars,
    metavars,
    code
):
    for name in metavars:
        code = code.replace(f"{allvars[name]!r}", name)

    return code


def get_pyname(yaml_name):
    pyname = yaml_name

    for (old, new) in [
        ('-', '_'),
    ]:
        pyname = pyname.replace(old, new)

    return pyname


# --------------------- #
# -- YAML ANALYSIS -- #
# --------------------- #

def get_name_required(name):
    if name[-1] == TAG_OPTIONAL:
        is_required = False
        name        = name[:-1].strip()

    else:
        is_required = True
        name        = name

    return name, is_required
