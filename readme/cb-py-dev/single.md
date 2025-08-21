### An isolated project

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
~~~~


Here is how the different elements will be used.

  1. `changes` is used to write the change log for developers, via `dev`, and for users, via `stable`. The method used complies with the specifications of the `tnschges` project currently under development.

  1. `contrib` allows technical contributions or translations to be managed separately. By isolating contributions, we need to abstract certain parts of the code, which is a good thing.

  1. `readme` is a folder containing the project's `README.md` file, which is being created via the `multimd` project currently being finalised.

  1. `src` is the folder for source code development.

  1. `tests` is used for coding the unit tests.

  1. `tools` is for coding tools that facilitate development: contribution management, updating the project's `README.md` file, etc.
