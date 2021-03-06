https://steemit.com/shadowbrokers/@theshadowbrokers/lost-in-translation

# Exploits

- **EARLYSHOVEL** RedHat 7.0 - 7.1 Sendmail 8.11.x exploit 
- **EBBISLAND (EBBSHAVE)** root RCE via RPC XDR overflow in Solaris 6, 7, 8, 9 & 10 (possibly newer) both SPARC and x86.
- **ECHOWRECKER** remote Samba 3.0.x Linux exploit. 
- **EASYBEE** appears to be an MDaemon email server vulnerability
- **EASYFUN** EasyFun 2.2.0 Exploit for WDaemon / IIS MDaemon/WorldClient pre 9.5.6
- **EASYPI** is an IBM Lotus Notes exploit  that gets detected as Stuxnet 
- **EWOKFRENZY** is an exploit for IBM Lotus Domino 6.5.4 & 7.0.2
- **EXPLODINGCAN** is an IIS 6.0 exploit that creates a remote backdoor
- **ETERNALROMANCE** is a SMB1 exploit over TCP port 445 which targets XP, 2003, Vista, 7, Windows 8, 2008, 2008 R2, and gives SYSTEM privileges (MS17-010)
- **EDUCATEDSCHOLAR** is a SMB exploit (MS09-050)
- **EMERALDTHREAD** is a SMB exploit for Windows XP and Server 2003 (MS10-061)
- **EMPHASISMINE** is a remote IMAP exploit for IBM Lotus Domino 6.6.4 to 8.5.2
- **ENGLISHMANSDENTIST** sets Outlook Exchange WebAccess rules to trigger executable code on the client's side to send an email to other users
- **EPICHERO** 0-day exploit (RCE) for Avaya Call Server
- **ERRATICGOPHER** is a SMBv1 exploit targeting Windows XP and Server 2003 
- **ETERNALSYNERGY** is a SMBv3 remote code execution flaw  for Windows 8 and Server 2012 SP0 (MS17-010)
- **ETERNALBLUE is** a SMBv2 exploit for Windows 7 SP1 (MS17-010)
- **ETERNALCHAMPION** is a SMBv1 exploit
- **ESKIMOROLL** is a Kerberos exploit targeting 2000, 2003, 2008 and 2008 R2 domain controllers
- **ESTEEMAUDIT** is an RDP exploit and backdoor for Windows Server 2003
- **ECLIPSEDWING** is an RCE exploit for the Server service in Windows Server 2008 and later (MS08-067)
- **ETRE** is an exploit for IMail 8.10 to 8.22 
- **ETCETERABLUE** is an exploit for IMail 7.04 to 8.05
- **FUZZBUNCH** is an exploit framework, similar to MetaSploit
- **ODDJOB** is an implant builder and C&C server that can deliver exploits for Windows 2000 and later, also not detected by any AV vendors 
- **EXPIREDPAYCHECK** IIS6 exploit
- **EAGERLEVER** NBT/SMB exploit for Windows NT4.0, 2000, XP SP1 & SP2, 2003 SP1 & Base Release
- **EASYFUN** WordClient / IIS6.0 exploit
- **ESSAYKEYNOTE** 
- **EVADEFRED**


# Utilities

- **PASSFREELY** utility which "Bypasses authentication for Oracle servers"
- **SMBTOUCH** check if the target is vulnerable to samba exploits like ETERNALSYNERGY, ETERNALBLUE, ETERNALROMANCE 
- **ERRATICGOPHERTOUCH**  Check if the target is running some RPC
- **IISTOUCH** check if the running IIS version is vulnerable
- **RPCOUTCH** get info about windows via RPC
- **DOPU** used to connect to machines exploited by ETERNALCHAMPIONS


# Installation

### Requirement
- [Microsoft Windows 7 x86](https://developer.microsoft.com/en-us/microsoft-edge/tools/vms/)
- [Python 2.6 x86](https://www.python.org/download/releases/2.6/)
- [Pywin 2.6 x86](https://sourceforge.net/projects/pywin32/files/pywin32/Build%20221/)
### Install
1. Setup Python 2.6
1. Add `C:\Python26` to Path variable in System variables.
1. Extract `pywin32-221.win32-py2.6.exe` with WinRAR.
1. Copy everythings in `pywin32-221.win32-py2.6\PLATLIB` to `C:\Python26\Lib\site-packages`
1. Open `Command Prompt` with administrator.
1. Goto `pywin32-221.win32-py2.6\SCRIPTS` and run `python pywin32_postinstall.py -install`

# Usage
```winbatch
C:\shadowbroker-master\windows\python fb.py
```
