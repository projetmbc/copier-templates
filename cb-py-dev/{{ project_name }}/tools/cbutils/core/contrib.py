#!/usr/bin/env python3

from pathlib     import Path
import sys
sys.path.append(str(Path(__file__).parent.parent.parent))




from collections import defaultdict
from pathlib     import Path

from yaml import safe_load

from cbutils.core.constants import *
from cbutils.core.logconf   import *
from cbutils.core.messages  import *


# ----------------------- #
# -- ACCEPTED CONTRIB. -- #
# ----------------------- #

def get_accepted_paths(projdir: Path) -> dict[Path, str]:
    logging.info("Looking for accepted contribs.")

    contrib_dir    = projdir / TAG_CONTRIB_DIR
    accepted_paths = defaultdict(list)

    for yaml_file in contrib_dir.rglob("status/*.yaml"):
        statusdata = safe_load(yaml_file.read_text())

        if statusdata[TAG_STATUS] != TAG_OK:
            continue

        locdir = yaml_file.parent.parent
        stem   = yaml_file.stem

# Acceptable folder?
        is_folder = (locdir / stem).is_dir()

# Acceptable files?
        files = [
            p
            for p in locdir.glob(f"*/{stem}.*")
            if p.is_file() and p.parent.name != TAG_STATUS
        ]

# Ambiguity?
        if is_folder and files:
            desc = "illegal OK contrib status"

            xtra = []

            if is_folder:
                xtra.append('One folder.')

            for p in files:
                xtra.append(f"File: '{p.name}'.")

            xtra = (
                  f'Several acceptable contribs.\n{TAB_ITEM_1}'
                + TAB_ITEM_1.join(xtra)
            )

            log_raise_error(
                exception = IOError,
                desc      = desc,
                xtra      = xtra,
            )

# Nothing found.
        if not(is_folder or files):
            log_raise_error(
                exception = IOError,
                desc      = f"no contrib. found for '{stem}'.",
            )

# Contrib. found.
        if is_folder:
            path = parent / stem

        else:
            path = files[0]

        accepted_paths[path.parent].append(path.name)

# Let's sort the lists of paths for a better output.
    for parent in accepted_paths:
        accepted_paths[path.parent].sort()

# Let's sort the lists of paths for a better output.
    return accepted_paths
