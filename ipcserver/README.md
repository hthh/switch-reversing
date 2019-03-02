# ipcserver

I always use these scripts when reversing IPC service implementations. They automatically find the implementation of each IPC command.

There are two scripts, `ipcserver_classic.py` and `ipcserver_modern.py`.


## ipcserver_classic.py

This works on system software versions 1.0 to 3.0.2 and generates an IDAPython script to name the functions. It's pretty slow, but the results are excellent.

If your reversing problem can be solved by looking at a 3.0 binary instead of the latest, I recommend starting there.

```
% time python ipcserver_classic.py 3.0.2-0.0/fs > 3.0.2-0.0/fs-server.py
python ipcserver_classic.py 3.0.2-0.0/fs > 3.0.2-0.0/fs-server.py  50.93s user 0.45s system 99% cpu 51.728 total
% tail 3.0.2-0.0/fs-server.py 
MakeName(0x7100032474,'CmifProcessFunctionTableGetterImpl__nn::fssrv::sf::IFileSystemProxyForLoader__::Process_Cmd1')
MakeName(0x7100032830,'CmifProcessFunctionTableGetterImpl__nn::fssrv::sf::IProgramRegistry__::Process_Cmd0')
MakeName(0x71000329F0,'CmifProcessFunctionTableGetterImpl__nn::fssrv::sf::IProgramRegistry__::Process_Cmd256')
MakeName(0x7100035F30,'nn::fssrv::sf::IFile_IpcObj_nn::fssrv::detail::FileInterfaceAdapter::Cmd0')
MakeName(0x7100036040,'nn::fssrv::sf::IFile_IpcObj_nn::fssrv::detail::FileInterfaceAdapter::Cmd1')
MakeName(0x71000360D4,'nn::fssrv::sf::IFile_IpcObj_nn::fssrv::detail::FileInterfaceAdapter::Cmd2')
MakeName(0x71000360F8,'nn::fssrv::sf::IFile_IpcObj_nn::fssrv::detail::FileInterfaceAdapter::Cmd3')
MakeName(0x710003612C,'nn::fssrv::sf::IFile_IpcObj_nn::fssrv::detail::FileInterfaceAdapter::Cmd4')
MakeName(0x7100036260,'nn::fssrv::sf::IDirectory_IpcObj_nn::fssrv::detail::DirectoryInterfaceAdapter::Cmd0')
MakeName(0x7100036338,'nn::fssrv::sf::IDirectory_IpcObj_nn::fssrv::detail::DirectoryInterfaceAdapter::Cmd1')
```

Load the script into IDA via "File -> Script File" and reverse any IPC command quickly and easily.


## ipcserver_modern.py

On 4.0 and later the symbols used by `ipcserver_classic.py` are missing. I worked around this in `swipc-gen` to dump the type information, but it still couldn't find the implementations. SciresM then developed a heuristic to find the implementations (matching the implementation by vtable length, with a bit of extra magic), which is implemented in `ipcserver_modern.py`:

```
% python ipcserver_modern.py /Users/dougallj/Projects/switch-research/system-software/sysmodules/7.0.0-5.0/fs 
'fs': {
  '0x71000B98F0': { # single hash match 'nn::fssrv::sf::IFileSystemProxy'
      1:     {"vt":  0x20, "func": 0x7100082230, "lr": 0x71000BA458, "inbytes":     8, "outbytes":     0, "pid": True},
      2:     {"vt":  0x28, "func": 0x7100082250, "lr": 0x71000BA5F0, "inbytes":     0, "outbytes":     0, "outinterfaces": ['0x71000C5340']},
      7:     {"vt":  0x30, "func": 0x7100082280, "lr": 0x71000BA7C4, "inbytes":  0x10, "outbytes":     0, "outinterfaces": ['0x71000C5340']},
      8:     {"vt":  0x38, "func": 0x71000822B0, "lr": 0x71000BA9DC, "inbytes":  0x10, "outbytes":     0, "buffers": [25], "outinterfaces": ['0x71000C5340']},
      9:     {"vt":  0x40, "func": 0x71000822E0, "lr": 0x71000BAC24, "inbytes":     8, "outbytes":     0, "outinterfaces": ['0x71000C5340']},
      11:    {"vt":  0x48, "func": 0x7100082310, "lr": 0x71000BAE3C, "inbytes":     4, "outbytes":     0, "buffers": [25], "outinterfaces": ['0x71000C5340']},
      12:    {"vt":  0x50, "func": 0x7100082340, "lr": 0x71000BB074, "inbytes":     4, "outbytes":     0, "outinterfaces": ['0x71000C8240']},
...
  '0x71000C71F0': { # , vtable size 6, possible vtables [0x7100230B90 6, 0x71002300C0 6, 0x7100244D78 6]
      0:     {"vt":  0x20, "lr": 0x71000C7438, "inbytes":  0x18, "outbytes":     8, "buffers": [70]},
      1:     {"vt":  0x28, "lr": 0x71000C7644, "inbytes":  0x18, "outbytes":     0, "buffers": [69]},
      2:     {"vt":  0x30, "lr": 0x71000C77F8, "inbytes":     0, "outbytes":     0},
      3:     {"vt":  0x38, "lr": 0x71000C794C, "inbytes":     8, "outbytes":     0},
      4:     {"vt":  0x40, "lr": 0x71000C7ABC, "inbytes":     0, "outbytes":     8},
      5:     {"vt":  0x48, "lr": 0x71000C7C40, "inbytes":  0x18, "outbytes":  0x40},
  },
```

This doesn't always work, and doesn't generate a script, but when it works, the "func" field tells you where the to find the implementation of each command.


## Notes

These are forked/duplicated from the `swipc-gen` code. There's tons of room for improvement, and I think there are bugfixes in `swipc-gen` that should be ported over. But these are the scripts as I've been using them, and they're good enough to save a ton of time.
