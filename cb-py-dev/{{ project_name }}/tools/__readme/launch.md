The launch.bash file
--------------------

The `launch.bash` file is used to launch all the tools. It works as follows.

   1. The files to be launched are all `Python` files. They are sorted naturally using the `sort` command applied to their path relative to the `tools` folder. **This allows for sequential processing.**

   1. The `tools/cbutils` folder is excluded from the search; it is the only one.

   1. The `-q` option, or `--quick`, is used to ignore files whose names end with `-slow`.
