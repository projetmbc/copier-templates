#!/usr/bin/env python3


# ------------------------------ #
# -- XXX -- #
# ------------------------------ #

###
# prototype::
#     title : X
#     desc  : X
###
def msg_title(
    title: str,
    desc : str,
) -> str:
    return f"{title.upper()} - {desc}"


###
# prototype::
#     context : X
#     upper   : X
#     plurial : X
###
def msg_creation_update(
    context: str,
    upper  : bool = True,
    plurial: bool = True,
) -> str:
    if upper:
        context = context.upper()

    plurial = 's' if plurial else ''

    return f"{context} code{plurial}: creation or update."
