#!/usr/bin/env python3

from pathlib import Path


# --------------- #
# -- CONSTANTS -- #
# --------------- #

THIS_DIR         = Path(__file__).parent
CBUTILS_CORE_DIR = THIS_DIR / 'cbutils' / 'core'

INIT_FILE = CBUTILS_CORE_DIR / "__init__.py"


# --------------------------- #
# -- UPDATE CORE INIT FILE -- #
# --------------------------- #

names = []

for pyfile in CBUTILS_CORE_DIR.glob("*.py"):
    this_name = pyfile.stem

    if this_name == "__init__":
        continue

    names.append(this_name)

names.sort()

maxlen = max(len(n) for n in names)

names = '\n'.join([
    f"from .{n.ljust(maxlen)} import *"
    for n in names
])

code = f"""
#!/usr/bin/env python3

{names}
""".lstrip()

INIT_FILE.touch()
INIT_FILE.write_text(code)
