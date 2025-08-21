#!/usr/bin/env python3

import                   logging
from rich.logging import RichHandler
from rich.console import Console

from multimd import Builder, Path


# ------------------------------- #
# -- LOGGING "DYNAMIC" CONFIG. -- #
# ------------------------------- #

LOG_FILE = "tools.log"


###
# XXXXXXX
###
class FileFormatter(logging.Formatter):
    def format(self, record):
        original_message = record.getMessage()
        cleaned_message  = re.sub(r'\[.*?\]', '', original_message)

        record.msg        = cleaned_message
        formatted_message = super().format(record)
        record.msg        = original_message

        return formatted_message


###
# XXXXXXX
###
class ColorFilter(logging.Filter):
    def filter(self, record):
        original_levelname = record.levelname

        if record.levelno >= logging.CRITICAL:
            record.msg = f"[black on wheat1]{record.msg}[/black on wheat1]"

        elif record.levelno >= logging.ERROR:
            record.msg = f"[bright_red]{record.msg}[/bright_red]"

        elif record.levelno >= logging.WARNING:
            record.msg = f"[dark_goldenrod]{record.msg}[/dark_goldenrod]"

        return True


###
# prototype::
#     no_color  : set to ''False'', the log information will be
#                 printed in color; otherwise, it will be printed
#                 in black and white.
#
#     :action: the function lives up to its name...
###
def setup_logging(no_color = False) -> None:
# Terminal handler
#
# ''color_system = "auto"'' detects whether the output is a real
# terminal. If not—such as when output is redirected via a pipe—no
# color is used
    console = Console(
        stderr=True,
        color_system=None if no_color else "auto"
    )

# File handler
    file_handler = logging.FileHandler(
        LOG_FILE,
        mode="a"
    )
    file_handler.setLevel(logging.ERROR)

    file_formatter = FileFormatter(
        "%(asctime)s [%(levelname)s] %(message)s"
    )
    file_handler.setFormatter(file_formatter)

# Terminal handler
    term_handler = RichHandler(
        console=console,
        rich_tracebacks=True,
        markup=True
    )
    term_handler.setLevel(logging.INFO)

# Apply global config
    logging.basicConfig(
# Resetting configurations
        force=True,
        level=logging.INFO,
        handlers=[term_handler, file_handler],
    )

# Appliquer le filtre UNIQUEMENT au gestionnaire de la console
    term_handler.addFilter(ColorFilter())


###
# XXXXXXX
###
setup_logging()


# --------------- #
# -- CONSTANTS -- #
# --------------- #

THIS_DIR = Path(__file__).parent
COPIER_TMPL_DIR = THIS_DIR.parent


TAG_DEBUG_FOLDER = 'x-debug-x/'

PARENTS_KEPT = [
    TAG_COPIER := 'copier-templates',
    TAG_CONTRIB:= 'contrib',
    TAG_TOOLS  := 'tools',
]


TAG_INFO    = 'info'
TAG_WARNING = 'warning'


# ----------- #
# -- TOOLS -- #
# ----------- #

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
    about : str,
    folder: str| Path,
    kind  : str = TAG_INFO,
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
        f"README.md {about} in the {folder} folder."
    )


# ---------------------------------- #
# -- REMOVE UNWANTED README FILES -- #
# -- &                            -- #
# -- BUILD WANTED README FILES    -- #
# ---------------------------------- #

for readme in COPIER_TMPL_DIR.rglob('README.md'):
    relpath = readme.relative_to(COPIER_TMPL_DIR)

    if str(relpath).startswith(TAG_DEBUG_FOLDER):
        continue

# Keep me.
    if keep_this_readme(readme):
        if not compile_this_readme(readme):
            log_print(
                about  = "static",
                folder = relpath.parent,
            )

            continue

# Compile me.
        log_print(
            about  = "compilation",
            folder = relpath.parent,
        )

        src = hidden_readme_folder(readme)

        if not src.is_dir():
            src = readme_folder(readme)

        mybuilder = Builder(
            src   = src,
            dest  = readme,
            erase = True
        )
        mybuilder.build()

# Remove me.
    else:
        log_print(
            kind   = TAG_WARNING,
            about  = "removed",
            folder = relpath.parent,
        )

        readme.unlink()
