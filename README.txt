##FLUENT_TUI

Simple tui command line helpers for Ansys Fluent. Current state is mostly non-existant.

Usage:

```
import fluent_tui as tui
d = tui.display()
d.picture_options(x=1024,y=768,dpi=300)
d.save_picture()
d.write_journal()
```