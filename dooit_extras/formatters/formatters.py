from typing import Optional
from rich.style import Style
from dooit.api.todo import datetime, Todo
from dooit.ui.api import DooitAPI
from rich.style import Style
from rich.text import Text
from dooit.ui.api import DooitAPI, allow_multiple_formatting
import re


@allow_multiple_formatting
def description_highlight_link(value: str, _: Todo, api: DooitAPI):
    """
    Highlight URLs in the description.
    """

    url_pattern = re.compile(
        r"http[s]?://"
        r"(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|"
        r"(?:%[0-9a-fA-F][0-9a-fA-F]))+",
        re.IGNORECASE,
    )

    text = Text.from_markup(value)
    text.highlight_regex(
        url_pattern,
        style=Style(
            color=api.vars.theme.primary,
            underline=True,
            italic=True,
        ),
    )

    return text.markup


def due_causal_format(due: Optional[datetime], _: Todo) -> str:
    """
    Shows the date in a more simple format: 
    Example: `23 Oct` instead of `23-10-2024`
    """

    if not due:
        return ""

    current_year = datetime.now().year
    dt_format = "%b %d"

    if due.year != current_year:
        dt_format += " '%y"

    if due.hour != 0 or due.minute != 0:
        dt_format += " (%-I:%M)"

    return due.strftime(dt_format)


def due_danger_today(due: Optional[datetime], _: Todo, api: DooitAPI) -> Optional[str]:
    """
    If the due date is today, show a bold red "Today" text.
    """

    if not due:
        return ""

    if due.date() == datetime.today().date():
        return Text(
            "Today",
            style=Style(
                color=api.vars.theme.red,
                bold=True,
            ),
        ).markup
