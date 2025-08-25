#!/usr/bin/env python3

from pathlib import Path


# --------------- #
# -- CONSTANTS -- #
# --------------- #

THIS_DIR         = Path(__file__).parent
CBUTILS_CORE_DIR = THIS_DIR / 'cbutils' / 'core'


# ----------- #
# -- TOOLS -- #
# ----------- #

TMPL_INIT = """
#!/usr/bin/env python3

{names}
""".lstrip()

TMPL_ABOUT = """
toc:
  - prologue.md
{names}
""".lstrip()

def format_list_init(names):
    maxlen = max(len(n) for n in names)

    names = '\n'.join([
        f"from .{n.ljust(maxlen)} import *"
        for n in names
    ])

    return names

def format_list_about(names):
    names = '\n'.join([f"  - {n}.md" for n in names])

    return names



TODO = [
# file, formater, tmpl
    (
        CBUTILS_CORE_DIR / "__init__.py",
        format_list_init,
        TMPL_INIT,
    ),
    (
        CBUTILS_CORE_DIR / "__manual" / "about.yaml",
        format_list_about,
        TMPL_ABOUT,
    ),
]


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

for file, formater, tmpl in TODO:
    code = tmpl.format(names = formater(names))

    file.touch()
    file.write_text(code)
