#!/usr/bin/env python3

from cbutils.core     import *
from cbutils.pathxtra import *


# --------------- #
# -- CONSTANTS -- #
# --------------- #

THIS_DIR         = Path(__file__).parent
COPIER_TMPL_DIR  = THIS_DIR.parent
MAIN_CONTRIB_DIR = COPIER_TMPL_DIR / 'contrib'

TO_UPDATE = [
    TAG_LICENSE_FILE:= 'LICENSE.txt',
    TAG_README_FILE := 'README.md',
]

TO_UPDATE = [MAIN_CONTRIB_DIR / n for n in TO_UPDATE]


MAIN_TITLE = """
Contribute to copier-templates
==============================
""".strip()

JINJA_TITLE = """
{% set __deco = '='*(14 + project_name | length) -%}
Contribute to {{ project_name }}
{{ __deco }}
""".strip()


# ----------- #
# -- TOOLS -- #
# ----------- #

def get_model_code(file: Path) -> str:
    code = model_file.read_text()

    if file.name == TAG_README_FILE:
        code = code.replace(MAIN_TITLE, JINJA_TITLE)

    return code


# -------------------------------- #
# -- UPDATE ALL COMMON CONTRIBS -- #
# -------------------------------- #

for dest_folder in COPIER_TMPL_DIR.glob(f"**/contrib"):
    if not_common_folder(
        path       = dest_folder,
        copier_dir = COPIER_TMPL_DIR
    ):
        continue

# Update the files.
    for model_file in TO_UPDATE:
        dest_file  = dest_folder

        if model_file.name == TAG_README_FILE:
            dest_file /= f"{model_file.name}.jinja"

        else:
            dest_file /= model_file.name

        logging.info(
            f"Updating '{dest_file.relative_to(COPIER_TMPL_DIR)}'."
        )


        model_code = get_model_code(model_file)

        dest_file.touch()
        dest_file.write_text(model_code)
