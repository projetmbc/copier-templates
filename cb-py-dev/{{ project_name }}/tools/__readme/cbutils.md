Some basic utilities
--------------------

The `tools/cbutils` folder is a "local" package containing your scripts that can be used by different tools (never forget the DRY principle). It contains the `core` module, which provides certain commonly used tools. Please refer to the `README.md` file for details on what is offered.




XXXX






---


> ***NOTE.*** *The file `cbutils/core/MANUAL.md` presents the functions offered by the `cbutils.core` module.*


---


> ***TIP.*** *Let's assume that the file `my-tool.py` is located directly in the `tools` folder. The `cbutils` package can be imported in a somewhat inelegant but functional manner, as follows.*

~~~python
#!/usr/bin/env python3

from pathlib import Path
import sys

# We go back as many levels as necessary via the `parent` attribute
# (just one level in our case).
_tools_dir = Path(__file__).parent

# `sys.path` is a list of strings.
sys.path.append(str(_tools_dir))

# Now everything works as if we had installed the `cbutils` package.
import cbutils

# This is where your coding begins.
...
~~~
