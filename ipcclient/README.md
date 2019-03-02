# ipcclient

This one is insanely useful, but it's a bit of a hassle to use.

## Usage

First we load the binary we're reversing in IDA, then we generate the IDAPython client script.

```
% python genidaclientscript.py sdk-3.5.0 > sdk-3.5.0-client-script.py
% grep decompile sdk-3.5.0-client-script.py | wc -l
     608
```

In IDA, I right-click in the "Output window" and click "Clear" - the type information will be output there as the script runs. Then just run the script and wait. (This script needs to decompile every serialization function and IPC client vtable function to get the types right, so it'll take a minute or two to run.)

The output looks like this:

```
struct nn::fssrv::sf::IFileSystemProxy::DomainClient;
struct nn::fssrv::sf::IFileSystemProxy::DomainClient::vt { /* 71008ce158-71008ce358 */
  /* 71000527E4 */ __int64 (*__fastcall AddReference)(nn::fssrv::sf::IFileSystemProxy::DomainClient *this);
  /* 71000527EC */ __int64 (*__fastcall Release)(nn::fssrv::sf::IFileSystemProxy::DomainClient *this);
  /* 7100052868 */ __int64 (*__fastcall GetProxyInfo)(nn::fssrv::sf::IFileSystemProxy::DomainClient *this);
  /* 7100042380 */ __int64 (*__fastcall GetInterfaceTypeInfo)(nn::fssrv::sf::IFileSystemProxy::DomainClient *this);
  /* 7100052870 */ unsigned int (*__fastcall Cmd1)(nn::fssrv::sf::IFileSystemProxy::DomainClient *this, __int64 a2);
  /* 7100052890 */ unsigned int (*__fastcall Cmd2)(nn::fssrv::sf::IFileSystemProxy::DomainClient *this, __int64 *a2);
  /* 7100052914 */ unsigned int (*__fastcall Cmd7)(nn::fssrv::sf::IFileSystemProxy::DomainClient *this, __int64 *a2, __int64 a3, int a4);
  /* 71000529B0 */ unsigned int (*__fastcall Cmd8)(nn::fssrv::sf::IFileSystemProxy::DomainClient *this, __int64 *a2, __int64 a3, __int64 a4, int a5);
  /* 7100052A5C */ unsigned int (*__fastcall Cmd9)(nn::fssrv::sf::IFileSystemProxy::DomainClient *this, __int64 *a2, __int64 a3);
  ...
};
struct nn::fssrv::sf::IFileSystemProxy::DomainClient {
  nn::fssrv::sf::IFileSystemProxy::DomainClient::vt *_v;
  _BYTE byte8;
  _BYTE byte9;
  unsigned int handle;
  void *_vt10;
  _DWORD dword18;
  _QWORD qword20;
};
```

Or, if there are symbols in the binary for that IPC service, they get included:

```
struct nn::account::baas::IGuestLoginRequest::DomainClient;
struct nn::account::baas::IGuestLoginRequest::DomainClient::vt { /* 71008d21b8-71008d2210 */
  /* 71000AFD08 */ __int64 (*__fastcall AddReference)(nn::account::baas::IGuestLoginRequest::DomainClient *this);
  /* 71000AFD10 */ __int64 (*__fastcall Release)(nn::account::baas::IGuestLoginRequest::DomainClient *this);
  /* 71000AFD84 */ __int64 (*__fastcall GetProxyInfo)(nn::account::baas::IGuestLoginRequest::DomainClient *this);
  /* 7100042380 */ __int64 (*__fastcall GetInterfaceTypeInfo)(nn::account::baas::IGuestLoginRequest::DomainClient *this);
  /* 71000AFD8C */ unsigned int (*__fastcall Cmd0_GetSessionId)(nn::account::baas::IGuestLoginRequest::DomainClient *this, _QWORD *a2);
  /* 71000AFDAC */ unsigned int (*__fastcall Cmd12_GetAccountId)(nn::account::baas::IGuestLoginRequest::DomainClient *this, _QWORD *a2);
  /* 71000AFDCC */ unsigned int (*__fastcall Cmd13_GetLinkedNintendoAccountId)(nn::account::baas::IGuestLoginRequest::DomainClient *this, _QWORD *a2);
  /* 71000AFDEC */ unsigned int (*__fastcall Cmd14_GetNickname)(nn::account::baas::IGuestLoginRequest::DomainClient *this, __int64 *a2);
  /* 71000AFE14 */ unsigned int (*__fastcall Cmd15_GetProfileImage)(nn::account::baas::IGuestLoginRequest::DomainClient *this, _DWORD *a2, __int64 *a3);
  /* 71000AFE3C */ unsigned int (*__fastcall Cmd21_LoadIdTokenCache)(nn::account::baas::IGuestLoginRequest::DomainClient *this, _DWORD *a2, __int64 *a3);
  /* 71000AFE64 */ __int64 (*__fastcall GetCmifBaseObject)(nn::account::baas::IGuestLoginRequest::DomainClient *this);
};
struct nn::account::baas::IGuestLoginRequest::DomainClient {
  nn::account::baas::IGuestLoginRequest::DomainClient::vt *_v;
  _BYTE byte8;
  _BYTE byte9;
  unsigned int handle;
  void *_vt10;
  _DWORD dword18;
  _QWORD qword20;
};
```

Next I open the "Local types" window, right-click "Insert..." and paste the whole lot in. (In case you get syntax errors you may have to split it up to bisect where the output is wrong, but I didn't have that issue today.)

Now in IDA where you see something like:

```
int __fastcall nn::fs::GetGlobalAccessLogMode(unsigned int *a1)
{
  unsigned int *v1; // x19
  unsigned int v2; // w19
  __int64 v4; // [xsp+0h] [xbp-20h]
  __int64 v5; // [xsp+8h] [xbp-18h]

  v1 = a1;
  nn::fs::detail::GetFileSystemProxyServiceObject(&v5);
  v2 = (*(__int64 (__fastcall **)(__int64, unsigned int *))(*(_QWORD *)v5 + 488LL))(v5, v1);
```

You can just click on `v5` and press `y` and change the type to `nn::fssrv::sf::IFileSystemProxy::DomainClient*` to get:

```
int __fastcall nn::fs::GetGlobalAccessLogMode(unsigned int *a1)
{
  unsigned int *v1; // x19
  unsigned int v2; // w19
  __int64 v4; // [xsp+0h] [xbp-20h]
  nn::fssrv::sf::IFileSystemProxy::DomainClient *v5; // [xsp+8h] [xbp-18h]

  v1 = a1;
  nn::fs::detail::GetFileSystemProxyServiceObject(&v5);
  v2 = v5->_v->Cmd1005(v5, v1);
```

## Missing symbols

The script silently ignores anything it can't figure out the name of. To list all ignored methods, run:

```
% python ipcclient.py 7.0.0-5.0/ns | grep IUnknown
  'IUnknown_2deb984d_0x7100223578': {
  'IUnknown_6218fa21_0x71002236D0': {
  'IUnknown_f4e4f171_0x71002256F8': {
  'IUnknown_b171b62c_0x7100225758': {
  'IUnknown_c72d14a7_0x71002257C8': {
  'IUnknown_cc86b99b_0x71002258B8': {
  'IUnknown_0868914f_0x7100225950': {
  'IUnknown_f4e4f171_0x71002284E0': {
  'IUnknown_cc86b99b_0x7100228540': {
  'IUnknown_0868914f_0x710022C4F8': {
  'IUnknown_d22f428b_0x710022C560': {
  'IUnknown_2cc737b7_0x710022EF20': {
  'IUnknown_ef63a7f7_0x710022F288': {
  'IUnknown_9c8f78df_0x7100237A40': {
```

Figure out the name by reversing, guessing from the command numbers in the `ipcclient.py` output, or just making up something useful, then add an entry to the `MANUAL_NAME_LOOKUP` table at the top of `ipcclient.py`:

```
MANUAL_NAME_LOOKUP = {
	'IUnknown_2deb984d_0x7100223578': 'FooBar',
}
```

Run it again and your entry will appear:

```
% python genidaclientscript.py 7.0.0-5.0/ns | grep FooBar
client_vtable('FooBar::Client', 0x7100223578, 0x71002236A8, ['AddReference', 'Release', 'GetProxyInfo', 'GetInterfaceTypeInfo', 'Cmd1', 'Cmd2', 'Cmd3', 'Cmd4', 'Cmd5', 'Cmd7', 'Cmd21', 'Cmd23', 'Cmd25', 'Cmd26', 'Cmd101', 'Cmd102', 'Cmd103', 'Cmd104', 'Cmd111', 'Cmd120', 'Cmd6', 'Cmd11', 'Cmd12', 'Cmd13', 'Cmd22', 'Cmd24', 'Cmd31', 'Cmd32', 'Cmd33', 'Cmd34', 'Cmd105', 'Cmd112', 'Cmd113', 'Cmd114', 'Cmd115', 'Cmd201', 'Cmd202', 'GetCmifBaseObject'])
```

(if you prefer to have the IUnknown names in the output delete the line `if 'IUnknown' in interface: continue` from `genidaclientscript.py`)

## Notes

The `DomainClient` structure is wrong.

Some of the really big command IDs (>65536) show up incorrectly.

It'd be practical and useful to embed command names from an `sdk` binary (or https://switchbrew.org ) when running on sysmodules and applets that don't have symbols.

