# switch-reversing

These are my personal Switch reversing scripts.

This is all a bit messy and chaotic, but I'm going to try to push my personal RE scripts and tools a bit more, since they can be pretty useful. Use at your own risk, no warranty, etc.

* `swipc-gen` is code for automated extraction of IPC information used to generate these diffs: https://gist.github.com/hthh/bb896c743878a2c0c337f41febdc0426
* `binutils` has simple utilities for dumping information from the system software binaries.
* `pattern` is a pair of tools for identifying and naming common library code in 64-bit binaries (where you have one file with the code with symbols, and another with the same code, but without symbols).

