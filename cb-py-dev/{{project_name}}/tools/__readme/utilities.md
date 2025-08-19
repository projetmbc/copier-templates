Voici le contenu initial de ce dossier.

~~~
+ tools
  * launch.bash
  * README.md
  + 01-contrib
    * 90-README-folders-struct.py
  + utilities
    * README.md
    * __init__.py
    * need_tests.py
    * cnp_code.py
    * common.py
~~~


Expliquons les différents élément du dossier `tools`.

  1. Le fichier `launch.bash` permet de lancer tous les outils en suivant les règles suivantes.

     * Les fichiers trouvés sont ordonnées de façon naturelle via la commande `sort` appliqué à leur chemin relativement au dossier `tools`. Ceci est très utile pour des traitements devant être séquentiels.

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
