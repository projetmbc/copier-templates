#!/usr/bin/env python3

import                   logging
from rich.logging import RichHandler
from rich.console import Console


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
# Let's apply our configurations.
###
setup_logging()
