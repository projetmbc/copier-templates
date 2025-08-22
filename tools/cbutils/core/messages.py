#!/usr/bin/env python3


# ---------- #
# -- XXX -- #
# ---------- #

###
# XXXXXXX
###
def log_title(
    title,
    desc,
):
    return f"{title.upper()} - {desc}"

###
# XXXXXXX
###
def message_creation_update(
    context,
    upper   = True,
    plurial = True,
):
    if upper:
        context = context.upper()

    plurial = 's' if plurial else ''

    return f"{context} code{plurial}: creation or update."
