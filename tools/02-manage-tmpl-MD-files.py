#!/usr/bin/env python3

from cbutils.core     import *
from cbutils.pathxtra import *

from multimd import Builder, Path


# --------------- #
# -- CONSTANTS -- #
# --------------- #

THIS_DIR        = Path(__file__).parent
COPIER_TMPL_DIR = THIS_DIR.parent


TAG_JINJA_EXT = '.jinja'

JINJA_PATTERNS = [
    JINJA_PATTERN_CODE:= re.compile(r"({%.*?%})", re.DOTALL),
    JINJA_PATTERN_VAR := re.compile("{{.*?}}"),
]


PARENTS_KEPT = [
    TAG_COPIER := 'copier-templates',
    TAG_CONTRIB:= 'contrib',
    TAG_TOOLS  := 'tools',
]


TAG_INFO    = 'info'
TAG_WARNING = 'warning'


README_DIRS = [
    '__readme',
    TAG_README:= 'readme',
    '__manual',
]


# ----------- #
# -- TOOLS -- #
# ----------- #

def get_md_file(md_dir: Path) -> Path:
    name = md_dir.name
    name = name.replace('_', '')
    name = name.upper()

    return md_dir.parent / f"{name}.md"



def is_md_jinja(md_dir: Path) -> bool:
    for _ in md_dir.rglob("*.md.jinja"):
        return True

    return False

def remove_escaped_in_jinja(match: re.Match) -> str:
    text = match.group(0)

    for c in "_*":
        text = text.replace(rf'\{c}', c)

    return text



def keep_this_readme(readme: Path) -> bool:
    return readme.parent.name in PARENTS_KEPT

def compile_this_readme(readme: Path) -> bool:
    assert not(
        hidden_readme_folder(readme).is_dir()
        and
        readme_folder(readme).is_dir()
    ), (
         "Illegal use of '__readme' and 'readme' folders. See:\n"
        f"{readme.parent}"
    )

    return (
        hidden_readme_folder(readme).is_dir()
        or
        readme_folder(readme).is_dir()
    )

def readme_folder(readme: Path) -> Path:
    return readme.parent / "readme"

def hidden_readme_folder(readme: Path) -> Path:
    return readme.parent / "__readme"


def log_print(
    md_name: str,
    about  : str,
    folder : str | Path,
    kind   : str = TAG_INFO,
):
    match kind:
        case "info":
            logger = logging.info

        case "warning":
            logger = logging.warning

        case _:
            raise ValueError(f"unmanaged kind '{kind}'.")

    folder = "main" if str(folder) == '.' else f"'{folder}'"

    logger(
        f"{md_name} {about} in the {folder} folder."
    )


# ---------------------------------- #
# -- REMOVE UNWANTED README FILES -- #
# ---------------------------------- #

for readme in COPIER_TMPL_DIR.rglob('README.md'):
# Ignore me.
    if is_debug_folder(
        path       = readme,
        copier_dir = COPIER_TMPL_DIR
    ):
        continue

# Remove me.
    if not keep_this_readme(readme):
        log_print(
            kind    = TAG_WARNING,
            md_name = TAG_README.upper(),
            about   = "removed",
            folder  = get_relpath(
                path       = readme,
                copier_dir = COPIER_TMPL_DIR
            ),
        )

        readme.unlink()


# --------------------------- #
# -- BUILD WANTED MD FILES -- #
# --------------------------- #

for dirname in README_DIRS:
    for md_dir in COPIER_TMPL_DIR.rglob(dirname):
# Ignore me.
        if is_debug_folder(
            path       = md_dir,
            copier_dir = COPIER_TMPL_DIR
        ) or (
            md_dir.name == TAG_README
            and
            not keep_this_readme(md_dir)
        ):
            continue

# Compile me.
        md_file = get_md_file(md_dir)

        if is_md_jinja(md_dir):
            md_file = md_file.parent / f"{md_file.name}{TAG_JINJA_EXT}"

        log_print(
            about   = "compilation",
            md_name = md_file.name,
            folder  = get_relpath(
                subpath  = md_dir.parent,
                mainpath = COPIER_TMPL_DIR
            ),
        )

        mybuilder = Builder(
            src   = md_dir,
            dest  = md_file,
            erase = True
        )

        mybuilder.build()

        if md_file.suffix == TAG_JINJA_EXT:
            code = md_file.read_text()

            for p in JINJA_PATTERNS:
                code = p.sub(remove_escaped_in_jinja, code)

            md_file.write_text(code)
