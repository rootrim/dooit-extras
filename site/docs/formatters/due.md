# Due Formatters

## Casual Format

This widget shows the date in a simple format

Eg: Instead of the default `yyyy-mm-dd`, it'll show in the format: \
`{Mon} {day} ['year(optional)]`

### Usage:

```python

from dooit_extras.formatters import due_causal_format
from dooit.ui.api.events import subscribe, Startup

@subscribe(Startup)
def setup(api, _):
    # ...
    api.formatter.todos.due.add(due_causal_format)
    # ...
```


## Danger Today

This widget shows a bold red `Danger` when the todo is due on the same day

```python

from dooit_extras.formatters import due_danger_today
from dooit.ui.api.events import subscribe, Startup

@subscribe(Startup)
def setup(api, _):
    # ...
    api.formatter.todos.due.add(due_danger_today)
    # ...
```