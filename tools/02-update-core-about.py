#!/usr/bin/env python3

from pathlib import Path


# --------------- #
# -- CONSTANTS -- #
# --------------- #

THIS_DIR         = Path(__file__).parent
CBUTILS_CORE_DIR = THIS_DIR / 'cbutils' / 'core'

ABOUT_FILE = CBUTILS_CORE_DIR / "__manual" / "about.yaml"


# ----------------------- #
# -- UPDATE ABOUT FILE -- #
# --------------------------- #

names = []

for pyfile in CBUTILS_CORE_DIR.glob("*.py"):
    this_name = pyfile.stem

    if this_name == "__init__":
        continue

    names.append(this_name)

names.sort()

names = '\n'.join([f"  - {n}.md" for n in names])

code = f"""
toc:
  - prologue.md
{names}
""".lstrip()

ABOUT_FILE.touch()
ABOUT_FILE.write_text(code)
