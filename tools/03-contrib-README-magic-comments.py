#!/usr/bin/env python3

from cbutils.core import *


# --------------- #
# -- CONSTANTS -- #
# --------------- #

THIS_DIR         = Path(__file__).parent
COPIER_TMPL_DIR  = THIS_DIR.parent

MAIN_CONTRIB_README = COPIER_TMPL_DIR / 'contrib' / 'README.md'

UNCOMMENTED_STRUCT_FOLDER = """
~~~
+ contrib
~~~
    """.strip()

COMMENTED_STRUCT_FOLDER = f"""
<!-- FOLDER STRUCT. AUTO - START -->
{UNCOMMENTED_STRUCT_FOLDER}
<!-- FOLDER STRUCT. AUTO - END -->
    """.strip() + '\n'


# ---------------------------- #
# -- IMPORTANT BASIC UPDATE -- #
# ---------------------------- #

logging.info(
     "Magic comments added into "
    f"'{MAIN_CONTRIB_README.relative_to(COPIER_TMPL_DIR)}'."
)

content = MAIN_CONTRIB_README.read_text()

content = content.replace(
    UNCOMMENTED_STRUCT_FOLDER,
    COMMENTED_STRUCT_FOLDER
)

MAIN_CONTRIB_README.write_text(content)
