<!----------------------------------------------------------------
  -- File created by the ''multimd'' project, version 1.0.0.    --
  --                                                            --
  -- ''multimd'', soon to be available on PyPI, is developed at --
  -- https://github.com/bc-tools/for-dev/tree/main/multimd      --
  ---------------------------------------------------------------->


Development tools
=================

The `tools` folder contains `Python` tools that are useful for developing the project, but are not part of the project itself.

**Table of contents**

<a id="MULTIMD-GO-BACK-TO-TOC"></a>
- [Initial structure of the tools folder](#MULTIMD-TOC-ANCHOR-0)
- [Le fichier launch.bash](#MULTIMD-TOC-ANCHOR-1)
- [A turnkey tool](#MULTIMD-TOC-ANCHOR-2)
- [Some basic utilities](#MULTIMD-TOC-ANCHOR-3)

<a id="MULTIMD-TOC-ANCHOR-0"></a>
Initial structure of the tools folder <a href="#MULTIMD-GO-BACK-TO-TOC" style="text-decoration: none;"><span style="margin-left: 0.25em; font-weight: bold; position: relative; top: -.5pt;">&#x2191;</span></a>
-------------------------------------

Here is the initial content of the `tools` folder, which serves as the basis for developing "in-house" tools.

~~~
+ tools
  * launch.bash
  * README.md
  + 01-contrib
    * 90-README-folders-struct.py
  + utilities
    * README.md
    * __init__.py
    + core/
      * __init__.py
      * common.py
      * cnp_code.py
      * need_tests.py
~~~

The following sections explain how this set of files and folders works.

<a id="MULTIMD-TOC-ANCHOR-1"></a>
Le fichier launch.bash <a href="#MULTIMD-GO-BACK-TO-TOC" style="text-decoration: none;"><span style="margin-left: 0.25em; font-weight: bold; position: relative; top: -.5pt;">&#x2191;</span></a>
----------------------

Le fichier `launch.bash` permet de lancer tous les outils en suivant les règles suivantes.

- Les fichiers trouvés sont ordonnées de façon naturelle via la commande `sort` appliqué à leur chemin relativement au dossier `tools`. Ceci est très utile pour des traitements devant être séquentiels.

<a id="MULTIMD-TOC-ANCHOR-2"></a>
A turnkey tool <a href="#MULTIMD-GO-BACK-TO-TOC" style="text-decoration: none;"><span style="margin-left: 0.25em; font-weight: bold; position: relative; top: -.5pt;">&#x2191;</span></a>
--------------

The file `01-contrib/90-README-folders-struct.py` automatically updates the `contrib` folder treeview inside the file `contrib/README.md`.

<a id="MULTIMD-TOC-ANCHOR-3"></a>
Some basic utilities <a href="#MULTIMD-GO-BACK-TO-TOC" style="text-decoration: none;"><span style="margin-left: 0.25em; font-weight: bold; position: relative; top: -.5pt;">&#x2191;</span></a>
--------------------

The `tools/utilities` folder is a "local" package containing your scripts that can be used by different tools (never forget the DRY principle). It contains the `core` module, which provides certain commonly used tools.

> ***ASTUCE.*** *Let's assume we have the file `my-tool.py` in the `tools` folder. Importing the `utilities` package will be done in an ugly way as follows.*

~~~python
#!/usr/bin/env python3

from pathlib import Path
import sys

# We go back as many levels as necessary via the `parent`
# attribute (just one level in our case).
TOOLS_DIR = Path(__file__).parent

# `sys.path` is a list of strings.
sys.path.append(str(TOOLS_DIR))

# Now, everything works as if we had installed the `utilities`
# package.
import utilities

# This is where your coding begins.
...
~~~
