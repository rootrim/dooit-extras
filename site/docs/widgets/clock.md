# Clock

A widget to show current time

| Key|<div style="width: 100px">Default</div> |Description|
| ------------- | :----------------:  | :----------------------------------------------------------------------------------------|
| api           |                     | The api object provided within the function                                              |
| fmt           | `" {} "`            | Specify how the text should be formatted, `{}` represents the value that'll be displayed |
| format        | `"%H:%M:%S"`        | Format to show the clock in, by default it shows in hh:mm:ss format                      |
| fg            | `theme.foreground1`| Color to show the text in, defaults to `theme.foreground1` or `white` based on theme    |
| bg            | `theme.primary`     | Color to show the background in, defaults to `theme.primary` or `accent` based on theme  |

::: tip
Check out [strfmt time cheetsheat](https://strftime.org/) for formats
:::


## Usage

```python
from dooit_extras.bar_widgets import Clock
from dooit.ui.api.events import subscribe, Startup

@subscribe(Startup)
def setup(api, _):
    api.bar.set( 
        [
            # ....
            Clock(api),
            # ....
        ]
    )
```
