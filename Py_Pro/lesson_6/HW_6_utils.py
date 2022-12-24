# what_to_change = {
#     "\n": "<br>",
# }


def convert_req_to_html(text: str) -> str:
    """Adds numbering to requirements and convert break line for HTML"""
    lines = text.split("\n")
    for i in range(len(lines)):
        if lines[i]:
            lines[i] = f"{i+1}. {lines[i]}"
    return "<br>".join(lines)
