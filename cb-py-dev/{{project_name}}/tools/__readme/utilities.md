


Expliquons les différents élément du dossier `tools`.

  1.

     * KKK

     * KKK

     * KKK

  1. XXX

  1. XXX

  1. XXX

  1. XXX


> ***ASTUCE.*** *Supposons avoir le fichier `my-tool.py` dans le dossier `tools`. XXXX*

~~~python
#!/usr/bin/env python3

from pathlib import Path
import sys

sys.path.append(str(Path(__file__).parent))

import utilities

...
~~~
