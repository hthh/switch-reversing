# binutils

Useful scripts for inspecting at switch binaries.

`nxo64.py` as always does the hard work of parsing the binaries, so each of the other scripts is under 100 lines and should be easy to modify if needed.


## getinfo.py

This is my most used one. I use it to check an `sdk` version, check if it's 64-bit or not, check what library a  `subsdk` binary is, or check what static libraries are linked into a game:

```
% python getinfo.py sdk    
File: sdk
Module: nnSdk
64-bit
FS SDK Version: 3.5.1
Number of Symbols: 19850
SDK MW+Nintendo+NintendoSDK_libz-3_5_1-Release
SDK MW+Nintendo+NintendoSdk_nnSdk-3_5_1-Release
SDK MW+Nintendo+NintendoSDK_NVN-3_5_1-Release

% python getinfo.py main
File: main
Module: D:\home\Project\Blitz_MasterVer27\App\Rom\NX64\Product\code\Blitz.nss
64-bit
Number of Symbols: 24
SDK MW+Nintendo+PiaCommon-5_9_1
SDK MW+Nintendo+Pia-5_9_1
SDK MW+Nintendo+PiaInet-5_9_1
SDK MW+Nintendo+PiaNat-5_9_1
SDK MW+Nintendo+PiaLan-5_9_1
SDK MW+Nintendo+PiaSession-5_9_1
SDK MW+Nintendo+PiaTransport-5_9_1
SDK MW+Nintendo+NEX-4_3_10-appblz
SDK MW+Nintendo+NintendoSDK_libcurl-3_4_1-Release
SDK MW+Nintendo+NintendoSDK_gfx-3_4_1-Release
SDK MW+Nintendo+NintendoWare_G3d-3_4_1-Release
SDK MW+Nintendo+NintendoWare_Vfx-3_4_1-Release
SDK MW+Nintendo+NintendoWare_Atk-3_4_1-Release
SDK MW+Nintendo+NintendoSDK_libz-3_4_1-Release
SDK MW+Nintendo+NEX_MM-4_3_10
SDK MW+Nintendo+NEX_DS-4_3_10
SDK MW+Nintendo+NEX_RK-4_3_10
SDK MW+Nintendo+NEX_UT-4_3_10
SDK MW+Nintendo+NEX_CO-4_3_10
SDK MW+Nintendo+PiaChat-5_9_1
SDK MW+Nintendo+PiaClone-5_9_1
SDK MW+Nintendo+PiaLocal-5_9_1
SDK MW+Nintendo+NintendoWare_Ui2d-3_4_1-Release
SDK MW+Nintendo+NintendoWare_Font-3_4_1-Release

% python getinfo.py subsdk0 
File: subsdk0
Module: libz
64-bit
Number of Symbols: 66
```

## findmagic.py

Search for a 4-byte magic number or an error code in binaries. Often misses things, but can save a lot of time when it finds them.

Note that you have to manually look for pairs with both halves of the value close together:

```
% python findmagic.py NCA3 3.0.0-10.0/*
3.0.0-10.0/fs(7100049E64): MOVK W9, 0x434E # 'NC'
3.0.0-10.0/fs(7100049E74): MOVK W9, 0x434E # 'NC'
3.0.0-10.0/fs(7100049E88): MOVK W9, 0x434E # 'NC'
3.0.0-10.0/fs(7100049E94): MOVZ W9, 0x33410000 # 'A3'
3.0.0-10.0/fs(7100049E98): MOVK W9, 0x434E # 'NC'
3.0.0-10.0/fs(710004BCF4): MOVZ W9, 0x33410000 # 'A3'
3.0.0-10.0/fs(710004BCF8): MOVK W9, 0x434E # 'NC'

% python findmagic.py 0x234E02 3.0.0-10.0/fs 
3.0.0-10.0/fs(7100018C50): MOVZ W21, 0x230000 # '#\x00'
3.0.0-10.0/fs(710001BC54): MOVZ W8, 0x230000 # '#\x00'
3.0.0-10.0/fs(7100036630): MOVZ W19, 0x230000 # '#\x00'
3.0.0-10.0/fs(710003727C): MOVZ W22, 0x230000 # '#\x00'
3.0.0-10.0/fs(7100038B34): MOVZ W26, 0x230000 # '#\x00'
3.0.0-10.0/fs(710003DBEC): MOVK W24, 0x4E02 # '\x02N'
3.0.0-10.0/fs(7100049E44): MOVZ W23, 0x230000 # '#\x00'
3.0.0-10.0/fs(710004A040): MOVZ W8, 0x230000 # '#\x00'
3.0.0-10.0/fs(710004A048): MOVK W8, 0x4E02 # '\x02N'
[snip]
```


## strings.py

This dumps strings with a filename and address prefix. I dump strings from every binary from a version to one huge file and grep for whatever I'm looking for:

```
% python strings.py 4.0.1/*/main > 4.0.1-strings.txt
% grep http 4.0.1-strings.txt
4.0.1/010000000000000C-bcat/main(71001E0C61): https://%s/api/nx/v1/list/%s
4.0.1/010000000000000C-bcat/main(71001E1349): https://%s/api/nx/v1/list/%s?l=%s%s%s
4.0.1/010000000000000C-bcat/main(71001E18C4): https://%s/api/nx/v1/titles/%016llx/topics?l=%s%s%s
[snip]
4.0.1/0100000000001013-myPage/main(7100524878): # http://curl.haxx.se/docs/http-cookies.html
4.0.1/0100000000001013-myPage/main(710052908B): https://mii-secure-%%.cdn.nintendo.net/%s_normal_face.png
4.0.1/0100000000001013-myPage/main(7100583FA0): N2nn2sf4cmif6client6detail13CmifProxyImplINS_7account4http15IOAuthProcedureENS2_15CmifDomainProxyINS0_4hipc6client38Hipc2ClientSessionManagedProxyKindBaseINSA_18Hipc2ProxyKindBaseILNS9_6detail11MessageTypeE4EEEEEEENS0_25StatelessAllocationPolicyINS0_22ExpHeapStaticAllocatorILm2048ENS5_6detail12ObjectHolder24ObjectHolderAllocatorTagEEEEENS5_3nas40IOAuthProcedureForNintendoAccountLinkageEEE
4.0.1/0100000000001013-myPage/main(7100584170): N2nn7account4http15IOAuthProcedureE
```


## nm.py

Just lists symbols:

```
% python nm.py 3.0.0-10.0/fs
           DEFAULT   NOTYPE  LOCAL    0        0 
00000000 T DEFAULT   SECTION LOCAL    1        0 
           DEFAULT   NOTYPE  WEAK     0        0 __rel_plt_start
           DEFAULT   NOTYPE  WEAK     0        0 __got_end
           DEFAULT   NOTYPE  WEAK     0        0 __rela_dyn_end
           DEFAULT   NOTYPE  WEAK     0        0 __rela_plt_end
[snip]
00e887d0 B DEFAULT   OBJECT  WEAK    21     4030 _ZN2nn2sf22ExpHeapStaticAllocatorILm16384ENS_8settings22IFactorySettingsServerEE8_globalsE
00e8c840 B DEFAULT   OBJECT  GLOBAL  21       10 _ZN3nne7prfile212pf_allocatorE
00e8c850 B DEFAULT   OBJECT  GLOBAL  21       10 _ZN3nne7prfile214pf_deallocatorE
00e8c860 B DEFAULT   OBJECT  GLOBAL  21      490 _ZN3nne7prfile212pdm_disk_setE
00e8ccf0 B DEFAULT   OBJECT  GLOBAL  21        4 _ZN3nne7prfile210pf_sys_setE
00e8ce48 B DEFAULT   OBJECT  GLOBAL  21        8 __cxa_new_handler
00e8dda0 B DEFAULT   OBJECT  GLOBAL  21        4 __horizon_max_num_modules
00e8dda8 B DEFAULT   OBJECT  GLOBAL  21        8 nnmuslThreadPointerInitializer
00e8ddb0 B DEFAULT   OBJECT  GLOBAL  21        8 nnmuslThreadPointerDestroyer
00e8e000 ? DEFAULT   NOTYPE  GLOBAL  21        0 end
```