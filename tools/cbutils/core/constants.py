#!/usr/bin/env python3

import re

from cbutils.core.constants import *
from cbutils.core.constants import *

# ------------ #
# -- README -- #
# ------------ #

TAG_README = 'readme'


# ------------ #
# -- CODING -- #
# ------------ #

TAG_ROOT_HEADER = ".:-R-O-O-T-:."


# --------------------- #
# -- CODING - PYTHON -- #
# --------------------- #

TAG_INIT     = "__init__"
INIT_FILE    = f"{TAG_INIT}.py"

SHEBANG_PYTHON = "#!/usr/bin/env python3\n"


PATTERN_COMMENT_HD_1 = re.compile(
    r"#\s+-+\s+#\n# --(.*)-- #\n# -+ #\n"
)

PATTERN_COMMENT_HD_2 = re.compile(
    r"# ~~(.*)~~ #\n"
)

# -------------- #
# -- CONTRIB. -- #
# -------------- #

TAG_CONTRIB_DIR = "contrib"

TAG_STATUS = "status"
TAG_OK     = "ok"

TAG_BAD_VALIDATION = "bad validation"
TAG_FILE           = "file"

TAG_WARNING  = "warning"
TAG_CRITICAL = "critical"
TAG_ERROR    = "error"
