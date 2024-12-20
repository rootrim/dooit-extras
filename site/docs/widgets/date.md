# Date

A widget to show today's date

| Key|<div style="width: 100px">Default</div> |Description|
| ------------- | :----------------:  | :----------------------------------------------------------------------------------------|
| api           |                     | The api object provided within the function                                              |
| fmt           | `" {} "`            | Specify how the text should be formatted, `{}` represents the value that'll be displayed |
| format        | `"%b %d"`           | Format to show the clock in, by default it shows in hh:mm:ss format                      |
| fg            | `theme.foreground1`| Color to show the text in, defaults to `theme.foreground1` or `white` based on theme    |
| bg            | `theme.primary`     | Color to show the background in, defaults to `theme.primary` or `accent` based on theme  |

::: tip
Check out [strfmt time cheetsheat](https://strftime.org/) for formats
:::


## Usage

```python
from dooit_extras.bar_widgets import Date
from dooit_extras.bar_widgets import CurrentWorkspace
from dooit.ui.api.events import subscribe, Startup

@subscribe(Startup)
def setup(api, _):
    api.bar.set( 
        [
            # ....
            Date(api),
            # ....
        ]
    )
```
