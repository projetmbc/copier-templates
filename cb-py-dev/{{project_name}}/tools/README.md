Des outils de développement
======================================

Le dossier `tools` est l'habitat des outils utiles au développement du projet, sans faire partie du projet lui-même.
Via le fichier `launch.bash`, il est possible de lancer tous les outils en suivant les règles suivantes.

  1. XXX

  1. Les fichiers trouvés sont ordonnées de façon naturelle via la commande `sort` appliqué à leur chemin relativement au dossier `tools`. Ceci est très utile pour des traitements devant être séquentiels.

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
