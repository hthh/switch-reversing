# How to use for a new version

*Step 1:* Extract all the sysmodule NSO and KIP files, using their name as their filename. Extract all the applet NSOs to a separate directory:

```
% ls 7.0.0-5.0
Bus             boot            erpt            grc             ncm             nvservices      psc             spl
LogManager.Prod boot2.ProdBoot  es              hid             nfc             olsc            ptm             ssl
account         bsdsocket       eupld           jpegdec         nifm            pcie.withoutHb  ro              tma.stub
am              btm             fatal           lbl             nim             pctl            safemode        usb
audio           capsrv          friends         ldn             npns            pcv             sdb             vi
bcat            creport         fs              ldr             ns              pm              settings        wlan
bluetooth       eclct           glue            migration       nvnflinger      ppc             sm
% ls 7.0.0-5.0-applets 
LibAppletAuth   LibAppletShop   cabinet         error           myPage          photoViewer     starter
LibAppletLns    LibAppletWeb    controller      maintenance     netConnect      playerSelect    swkbd
LibAppletOff    auth            dataErase       miiEdit         overlayDisp     qlaunch
```

*Step 2:* Update `hashes_gen.py` by running `generatehashes.py` on both sysmodules and applets. If you have an nnSdk binary matching the version you should include it as well. This may take several minutes.

```
% time python generatehashes.py 7.0.0-5.0/* 7.0.0-5.0-applets/*
doing '7.0.0-5.0/Bus'...
doing '7.0.0-5.0/LogManager.Prod'...
doing '7.0.0-5.0/account'...
TODO: UcError:  Unhandled CPU exception (UC_ERR_EXCEPTION)
[snip]
doing '7.0.0-5.0-applets/starter'...
TODO: UcError:  Unhandled CPU exception (UC_ERR_EXCEPTION)
TODO: UcError:  Unhandled CPU exception (UC_ERR_EXCEPTION)
TODO: UcError:  Unhandled CPU exception (UC_ERR_EXCEPTION)
TODO: UcError:  Unhandled CPU exception (UC_ERR_EXCEPTION)
bad 24565 90100
bad 24565 90100
doing '7.0.0-5.0-applets/swkbd'...
TODO: UcError:  Unhandled CPU exception (UC_ERR_EXCEPTION)
TODO: UcError:  Unhandled CPU exception (UC_ERR_EXCEPTION)
TODO: UcError:  Unhandled CPU exception (UC_ERR_EXCEPTION)
TODO: UcError:  Unhandled CPU exception (UC_ERR_EXCEPTION)
bad 24565 90100
python generatehashes.py 7.0.0-5.0/* 7.0.0-5.0-applets/*  182.18s user 14.90s system 99% cpu 3:17.64 total

% python
>>> from hashes_gen import all_hashes
>>> len(all_hashes)
248
```

(The errors printed are normal, I hope they'll only cause missing names.)

*Step 3:* Run `ipcserver.py` on the sysmodules (now takes only about 15 seconds for everything, assuming you decompress the NSOs with hactool first!)

```
% time python ipcserver.py 7.0.0-5.0/* > data700.py
python ipcserver.py 7.0.0-5.0/* > data700.py  14.36s user 0.39s system 98% cpu 15.024 total
```

The output should start something like this, with some names missing but others recovered. The `hash:` comments suggest possible names when there are multiple hits for a single hash.

```
# 7.0.0-5.0/Bus
# hash:  0x710000C690 ['nn::visrv::sf::IApplicationRootService', 'nn::sasbus::IManager', 'nn::fan::detail::IManager', 'nn::mii::detail::IStaticService']
# hash:  0x710002AFD0 ['nn::visrv::sf::IApplicationRootService', 'nn::sasbus::IManager', 'nn::fan::detail::IManager', 'nn::mii::detail::IStaticService']
'Bus': {
  '0x710000C690': {
    0:      {"inbytes":     4, "outbytes":     0, "outinterfaces": ['0x710000C9C0']},
  },
  '0x710000C9C0': {
    0:      {"inbytes":     4, "outbytes":     0},
    1:      {"inbytes":     0, "outbytes":     4},
    2:      {"inbytes":     4, "outbytes":     0},
  },
  'nn::sf::hipc::detail::IHipcManager': {
    0:      {"inbytes":     0, "outbytes":     4},
    1:      {"inbytes":     4, "outbytes":     0, "outhandles": [2]},
    2:      {"inbytes":     0, "outbytes":     0, "outhandles": [2]},
    3:      {"inbytes":     0, "outbytes":     2},
    4:      {"inbytes":     4, "outbytes":     0, "outhandles": [2]},
  },
  'nn::gpio::IManager': {
    0:      {"inbytes":     4, "outbytes":     0, "outinterfaces": ['nn::gpio::IPadSession']},
    1:      {"inbytes":     4, "outbytes":     0, "outinterfaces": ['nn::gpio::IPadSession']},
    2:      {"inbytes":     4, "outbytes":     0, "outinterfaces": ['nn::gpio::IPadSession']},
    6:      {"inbytes":     4, "outbytes":     0},
    7:      {"inbytes":     8, "outbytes":     0, "outinterfaces": ['nn::gpio::IPadSession']},
    8:      {"inbytes":     4, "outbytes":     1},
    9:      {"inbytes":     8, "outbytes":     0},
    10:     {"inbytes":     8, "outbytes":     0},
  },
```

*Step 4:* Add the `data700 = {` and `}` lines to the start and end of the resulting `.py` file, and clean up manually by comparing with the previous version by hand, and reversing where necessary. Diff with the previous version and read through it to find cases where the wrong name has been used.
