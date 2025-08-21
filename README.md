<!----------------------------------------------------------------
  -- File created by the ''multimd'' project, version 1.0.0.    --
  --                                                            --
  -- ''multimd'', soon to be available on PyPI, is developed at --
  -- https://github.com/bc-tools/for-dev/tree/main/multimd      --
  ---------------------------------------------------------------->


The copier-templates project
============================

This project brings together [`copier`](https://github.com/copier-org/copier) templates that can give you, the reader, ideas for your own configuration.

**Table of contents**

<a id="MULTIMD-GO-BACK-TO-TOC"></a>
- [Python templates](#MULTIMD-TOC-ANCHOR-0)
    - [An isolated project](#MULTIMD-TOC-ANCHOR-1)

<a id="MULTIMD-TOC-ANCHOR-0"></a>
Python templates <a href="#MULTIMD-GO-BACK-TO-TOC" style="text-decoration: none;"><span style="margin-left: 0.25em; font-weight: bold; position: relative; top: -.5pt;">&#x2191;</span></a>
----------------

<a id="MULTIMD-TOC-ANCHOR-1"></a>
### An isolated project <a href="#MULTIMD-GO-BACK-TO-TOC" style="text-decoration: none;"><span style="margin-left: 0.25em; font-weight: bold; position: relative; top: -.5pt;">&#x2191;</span></a>

The initial general organisation is as follows.

~~~
+ your-python-project
    + changes
        + dev
        + stable
    + contrib
    + readme
    + src
    + tests
    + tools
~~~

Here is how the different elements will be used.

1. `changes` is used to write the change log for developers, via `dev`, and for users, via `stable`. The method used complies with the specifications of the `tnschges` project currently under development.
2. `contrib` allows technical contributions or translations to be managed separately. By isolating contributions, we need to abstract certain parts of the code, which is a good thing.
3. `readme` is a folder containing the project's `README.md` file, which is being created via the `multimd` project currently being finalised.
4. `src` is the folder for source code development.
5. `tests` is used for coding the unit tests.
6. `tools` is for coding tools that facilitate development: contribution management, updating the project's `README.md` file, etc.
