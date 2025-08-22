Some basic utilities
--------------------

The `tools/cbutils` folder is a "local" module for specific scripts intended for use by several tools (never forget the `DRY` principle). It contains the `core` submodule, which brings together some very commonly used tools.


---


> ***NOTE.*** *The file `tools/cbutils/core/MANUAL.md` provides a quick overview of the `core` submodule.*


---


> ***WARNING!*** *If you think the `core` submodule could be improved, please submit your suggestions via the `copier-templates` project at https://github.com/projetmbc/copier-templates. You will have to change the folder `tools/cbutils/core` of the repository, and not of the template.*


---


> ***TIP.*** *Let's assume that the file `my-tool.py` is located directly in the `tools` folder. The `cbutils` package can be imported in a somewhat inelegant but functional manner, as follows.*

~~~python
#!/usr/bin/env python3

from pathlib import Path
import sys

# We go back as many levels as necessary via the `parent` attribute
# (just one level in our case).
TOOLS_DIR = Path(__file__).parent

# `sys.path` is a list of strings.
sys.path.append(str(TOOLS_DIR))

# Now everything works as if we had installed the `cbutils` package.
import cbutils

# This is where your coding begins.
...
~~~
