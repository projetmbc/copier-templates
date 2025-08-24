#!/usr/bin/env python3

import re


# ------------ #
# -- README -- #
# ------------ #

TAG_README = 'readme'


# ----------------- #
# -- PYTHON FILE -- #
# ----------------- #

TAG_INIT     = "__init__"
INIT_FILE    = f"{TAG_INIT}.py"

SHEBANG_PYTHON = "#!/usr/bin/env python3\n"


PATTERN_SECTION_COMMENT = re.compile(
    r"#\s+-+\s+#\n# --(.*)-- #\n# -+ #\n"
)

PATTERN_SUB_SECTION_COMMENT = re.compile(
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
