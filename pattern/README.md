# pattern

This is my alternative to FLIRT signatures or Diaphora for symbol porting. It tries to address the shortcomings of FLIRT on arm64. It is comically slow and simple, but generally gets more names (about 75% more in the one test I bothered doing). On the other hand, FLIRT may be superior when using a mismatched `sdk` version, just because it's less careful about checking the code matches exactly. I didn't look into this. There are some false-positives, but I ran into those with FLIRT too. 

You will need an nnSdk (`sdk`) binary matching the target binary as closely as possible. I have also used it to port symbols from `subsdk` binaries and games (that have symbols for statically linked libraries) to the system software.

The technique used is simple, and painfully slow, but effective. I didn't want to release this because I've been trying for ages to replace it with a better approach, but it's still the best I've got.


## Usage

First use `makepattern.py` on a file with symbols (usually an `sdk` binary) to generate a pattern file. This may take a few minutes:

```
% time python makepattern.py sdk-0.16.29 > pattern-100.txt
python makepattern.py sdk-0.16.29 > pattern-100.txt  345.02s user 3.12s system 99% cpu 5:48.98 total
% wc -l pattern-100.txt
    6403 pattern-100.txt
```

Then use `applypattern.py` to match the symbols:

```
% time python applypattern.py pattern-100.txt ns-1.0
python applypattern.py pattern-100.txt ns-1.0  27.41s user 0.21s system 99% cpu 27.727 total
% wc -l ns-1.0-sdk-syms.py 
     897 ns-1.0-sdk-syms.py
```

The generated `ns-1.0-sdk-syms.py` is an IDAPython script which is loaded via File -> Script File.

`applypattern.py` can run on multiple files, its output is always written to a file of the same name plus the `-sdk-syms.py` suffix. Since it takes 30+ seconds to run, I like to run it ahead of time on every binary, e.g. `python applypattern.py pattern-100.txt 1.0.0/*`


## How it works

Functions are generally byte-for-byte identical in the nnSdk and the system software statically linked against the same version. The exception is instructions modified by the linker, so we ignore these instructions, and match on everything else in the function.

How can we match a pattern where we only care about some of the bytes? Regular expressions.

Yes, this tool creates a list of over six thousand regular expressions and runs each, in sequence, across the binary you pass in.

I really hate it, but it's been extremely useful. I hope to replace it soon™.
