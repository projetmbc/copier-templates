#!/usr/bin/env python3

from cbutils.common   import *
from cbutils.log_conf import *


# --------------- #
# -- CONSTANTS -- #
# --------------- #

THIS_DIR = Path(__file__).parent
COPIER_TMPL_DIR = THIS_DIR.parent

TAG_LAUNCH_FILE = 'launch.bash'
TAG_LOG_FILE    = 'log_conf.py'

TO_UPDATE = [
# (model_file, model_code, pattern)
    (
        MODEL_LAUNCH_FILE:= THIS_DIR / TAG_LAUNCH_FILE,
        MODEL_LAUNCH_CODE:= MODEL_LAUNCH_FILE.read_text(),
        TAG_LAUNCH_FILE
    ),
    (
        MODEL_LOG_FILE:= THIS_DIR / 'cbutils' / TAG_LOG_FILE,
        MODEL_LOG_CODE:= MODEL_LOG_FILE.read_text(),
        f"cbutils/core/{TAG_LOG_FILE}"
    ),
]


# ------------------ #
# -- UPDATE FILES -- #
# ------------------ #

for (
    model_file,
    model_code,
    pattern,
) in TO_UPDATE:
    for dest_file in COPIER_TMPL_DIR.glob(f"**/{pattern}"):
        if dest_file == model_file or is_debug(
            path       = dest_file,
            copier_dir = COPIER_TMPL_DIR
        ):
            continue

        logging.info(
            f"Updating '{dest_file.relative_to(COPIER_TMPL_DIR)}'."
        )

        dest_file.write_text(model_code)
