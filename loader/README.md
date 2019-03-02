# loader

I wrote the original version of the ReSwitched loader (https://github.com/reswitched/loaders/ ), but this version has been extended with a number of other features:

* Support for loading binaries dumped from memory (mostly of historical interest, as we got DMA before we got keys)
* Improved ELF section identification to get `.hash`, `.gnu.hash`, `.eh_frame_hdr` and (unfortunately, all but the last entry of) `.eh_frame`.
* Loading the builtin IDA `eh_parse` plugin, which annotates the assembly to show exception handlers (and `; __unwind {` blocks and stuff).
* Loading multiple files (originally for use with CageTheUnicorn/Mephisto, might work with other emulators, or you could update it for that).
* SDK "arm64 .plt call rewriting hack". Usually every call in an SDK binary goes via the `.plt`. This is annoying for reversing, so this rewrites every `call` instruction that points to the `.plt` to instead point to the actual target function.
* Experimental "type guessing" (only enabled when ".plt call rewriting hack" is enabled). Usually when IDA sees the mangled symbol `nn::fs::detail::Allocate(u64)` it assumes the type is `nn::fs::detail::Allocate(nn::fs::detail *this, u64)`. In reality `nn::fs::detail` is a namespace (but IDA can't know this, the mangled symbol is the same as if it were a class). These incorrect types can get propagated all over the place by the decompiler. I find any mangled symbols in the `nn` namespace, where the class name would start with a lowercase letter, and provide a guess of the type name without the "this" argument. Results are very promising so far.

My personal copy of the loader has always had one or two "experimental" features or changes, like the type guessing described above. I've avoided releasing, because they might cause people problems. But instead I'm just going to aim to keep this repository up to date with whatever version of the loader I'm currently using.

(It may also be missing some features of the official loader, like patching support, sorry! It forked off a long time ago and I've just brought over fixes as I've run into issues.)

## Usage

Same as https://github.com/reswitched/loaders