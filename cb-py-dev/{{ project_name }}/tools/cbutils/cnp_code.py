def get_code_parts(file, context, sections_ignored):
    content = file.read_text()

# 1st paring.
    parts   = dict()
    section = SECTION_MAIN

    for i, piece in enumerate(
        PATTERN_SECTION_COMMENT.split(content)
    ):
        piece = piece.strip()

        if i % 2 == 1:
            section = piece

        elif not section in sections_ignored:
            parts[section] = piece

    all_sections = list(parts)

# Missing mandatory "context" section?
    if (
        context in CTXTS_AS_SECTIONS
        and
        not context.upper() in all_sections
    ):
        return {}

# We have to clean MAIN and CONSTANTS secrtion by taking care
# of sub sections. This can make empty these sections.
    section_to_remove = []

    for section in parts:
        if section in SECTIONS_WITH_SUB_ONES:
            part = cleaned_part(
                parts[section],
                sections_ignored,
            )

            if part:
                parts[section] = part

            else:
                section_to_remove.append(section)

    for section in section_to_remove:
        del parts[section]

# Nothing left to do.
    return parts


def cleaned_part(
    part,
    sections_ignored,
):
    cleaned_part = []
    section      = SECTION_MAIN

    for i, piece in enumerate(
        PATTERN_SUB_SECTION_COMMENT.split(part)
    ):
        piece = piece.strip()

        if i % 2 == 1:
            section = piece

        elif not section in sections_ignored:
            cleaned_part.append(piece.strip())

    cleaned_part = '\n\n'.join(cleaned_part)

    return cleaned_part


def get_final_code(code_parts, sections_ignored):
    code = []

    for section, part in code_parts.items():
        if section in sections_ignored:
            continue

        code += [
            '',
            '',
            magic_comment(section),
            '',
            part
        ]

    code = '\n'.join(code)
    code = code.strip()

    return code


def magic_comment(section):
    if section == SECTION_MAIN:
        return ""

    section = f"-- {section} --"

    rule = '-'*len(section)
    rule = f"# {rule} #"

    section = f"""
{rule}
# {section} #
{rule}
    """.strip()

    return section
