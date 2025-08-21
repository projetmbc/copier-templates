Some basic utilities
--------------------

The `tools/cbutils` folder is a "local" package containing your scripts that can be used by different tools (never forget the DRY principle). It contains the `core` module, which provides certain commonly used tools. Please refer to the `README.md` file for details on what is offered.




XXXX

---

> ***NOTE.*** *Voir le fichier `cbutils/core/MANUAL.md` présente les fontions proposés par le module `cbutils.core`.*

---

> ***TIP.*** *Let's assume we have the file `my-tool.py` in the `tools` folder. Importing the `cbutils` package can be done in an ugly way as follows.*

~~~python
#!/usr/bin/env python3

from pathlib import Path
import sys

# We go back as many levels as necessary via the `parent`
# attribute (just one level in our case).
_tools_dir = Path(__file__).parent

# `sys.path` is a list of strings.
sys.path.append(str(_tools_dir))

# Now, everything works as if we had installed the `cbutils`
# package.
import cbutils

# This is where your coding begins.
...
~~~
