#!/usr/bin/env python3

from cbutils.core     import *
from cbutils.pathxtra import *


# --------------- #
# -- CONSTANTS -- #
# --------------- #

THIS_DIR         = Path(__file__).parent
COPIER_TMPL_DIR  = THIS_DIR.parent
CBUTILS_CORE_DIR = THIS_DIR / 'cbutils' / 'core'


TAG_DEBUG_FOLDER = 'x-debug-x/'


TAG_LAUNCH_FILE = 'launch.sh'
TAG_MANUAL_FILE = 'MANUAL.md'

TO_UPDATE  = [p for p in CBUTILS_CORE_DIR.glob("*.py")]
TO_UPDATE += [
    CBUTILS_CORE_DIR / TAG_MANUAL_FILE,
    THIS_DIR / TAG_LAUNCH_FILE,
]


# ----------- #
# -- TOOLS -- #
# ----------- #

def ignore_cbutils(
    path      : Path,
    copier_dir: Path
) -> bool:
    global TAG_DEBUG_FOLDER

    relpath = get_relpath(
        subpath  = path,
        mainpath = copier_dir
    )

    return (
        path.parent == copier_dir
        or
        str(relpath).startswith(TAG_DEBUG_FOLDER)
    )


# ------------------ #
# -- UPDATE FILES -- #
# ------------------ #

for dest_folder in COPIER_TMPL_DIR.glob(f"**/tools"):
    if not_common_folder(
        path       = dest_folder,
        copier_dir = COPIER_TMPL_DIR
    ):
        continue

# Start with an empty core folder.
    core_folder = dest_folder / "cbutils" / "core"

    empty_dir(core_folder)

# Update the files.
    for model_file in TO_UPDATE:
        dest_file = dest_folder / model_file.relative_to(THIS_DIR)

        logging.info(
            f"Updating '{dest_file.relative_to(COPIER_TMPL_DIR)}'."
        )

        model_code = model_file.read_text()

        dest_file.touch()
        dest_file.write_text(model_code)
