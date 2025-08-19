Les outils
===========================

Le dossier `tools` est l'habitat des outils utiles au développement du projet, sans faire partie du projet lui-même.

Le fichier `launch.bash`permet de lancer tous les outils en suivant les règles suivantes.

  1. XXX

  1. Les fichiers trouvés sont ordonnées de façon naturelle via la commande `sort` appliqué à leur cehemin relativement au dossier `tools`.

  1. XXX

  1. XXX

  1. XXX

  1. XXX


> ***TIP.*** *MM*

~~~python
#!/usr/bin/env python3

# Path of this file: ./tools/my-name.py

from pathlib import Path
import              sys

sys.path.append(str(Path(__file__).parent))

import utilities
~~~
