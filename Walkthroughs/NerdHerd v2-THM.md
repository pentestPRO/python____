[*] NerdHerd v2 [*]

# Date : 22/01/2022

# ->Enumeration phase:

# Nmap 7.91 scan initiated Fri Jan 21 21:33:40 2022 as: nmap -vv -sV -sC -p- -oN nmap_udp 10.10.98.83
Nmap scan report for 10.10.98.83
Host is up, received echo-reply ttl 63 (0.33s latency).
Scanned at 2022-01-21 21:33:41 IST for 2895s
Not shown: 65530 closed ports
Reason: 65530 resets
PORT     STATE SERVICE     REASON         VERSION
21/tcp   open  ftp         syn-ack ttl 63 vsftpd 3.0.3
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_drwxr-xr-x    3 ftp      ftp          4096 Sep 11  2020 pub
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:10.8.162.88
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 19
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
22/tcp   open  ssh         syn-ack ttl 63 OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 0c:84:1b:36:b2:a2:e1:11:dd:6a:ef:42:7b:0d:bb:43 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCYrqlEH/5dR4LGfKThK3BQuCVPxx91asS9FfOewAooNFJf4zsESd/VCHcfQCXEHucZo7+xdceZklC7PwhzmybjkN79iQcd040gw5kg0htMWuVzdzcVFowV0hC1o7Rbze7zLya1B1C105aEoRKVHVeTx0ishoJfJlkJBlx2nKrKWciDYbJQvG+1TxEJaEM4KkmkO31y0L7C3nsdaEd+Z/lNIo6JfbxwrOb6vBonPLS/lZDJdaY0vrdZJ81FRiMbSuUIj3lEtDAZNWBTwXx5kO3fwodw4KbS0ukW5srZX5TLmf/Q/T8ooCnJMLvaksIXKl0r8fjJIx0QucoCwhCTR2o1
|   256 e2:5d:9e:e7:28:ea:d3:dd:d4:cc:20:86:a3:df:23:b8 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBNSB3jALoSxl/A6Jtpf21NoRfbr8ICR6FpH+bbprQ17LUFUm6pUrhDSx134JBYKLOfFljhNKR57LLS6LAK0bKB0=
|   256 ec:be:23:7b:a9:4c:21:85:bc:a8:db:0e:7c:39:de:49 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAII4VHJRelvecImJNkkZcKdI+vK0Hn1SjMT2r8SaiLiK3
139/tcp  open  netbios-ssn syn-ack ttl 63 Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp  open  netbios-ssn syn-ack ttl 63 Samba smbd 4.3.11-Ubuntu (workgroup: WORKGROUP)
1337/tcp open  http        syn-ack ttl 63 Apache httpd 2.4.18 ((Ubuntu))
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
Service Info: Host: NERDHERD; OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
|_clock-skew: mean: -27m47s, deviation: 1h09m15s, median: 12m10s
| nbstat: NetBIOS name: NERDHERD, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
| Names:
|   NERDHERD<00>         Flags: <unique><active>
|   NERDHERD<03>         Flags: <unique><active>
|   NERDHERD<20>         Flags: <unique><active>
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
|   Check 1 (port 43624/tcp): CLEAN (Couldn't connect)
|   Check 2 (port 49940/tcp): CLEAN (Couldn't connect)
|   Check 3 (port 9143/udp): CLEAN (Failed to receive data)
|   Check 4 (port 50413/udp): CLEAN (Failed to receive data)
|_  0/4 checks are positive: Host is CLEAN or ports are blocked
| smb-os-discovery: 
|   OS: Windows 6.1 (Samba 4.3.11-Ubuntu)
|   Computer name: nerdherd
|   NetBIOS computer name: NERDHERD\x00
|   Domain name: \x00
|   FQDN: nerdherd
|_  System time: 2022-01-21T19:03:41+02:00
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2022-01-21T17:03:42
|_  start_date: N/A

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Fri Jan 21 22:21:57 2022 -- 1 IP address (1 host up) scanned in 2896.53 seconds

# found directories:

[22:30:20] Starting: 
[22:30:38] 403 -  278B  - /.htaccess.bak1
[22:30:38] 403 -  278B  - /.htaccess.save
[22:30:38] 403 -  278B  - /.htaccess.orig
[22:30:38] 403 -  278B  - /.htaccess.sample
[22:30:38] 403 -  278B  - /.htaccess_extra
[22:30:38] 403 -  278B  - /.htaccess_orig
[22:30:38] 403 -  278B  - /.htaccessOLD
[22:30:38] 403 -  278B  - /.htaccessBAK
[22:30:38] 403 -  278B  - /.htaccessOLD2
[22:30:38] 403 -  278B  - /.htaccess_sc
[22:30:38] 403 -  278B  - /.htm
[22:30:38] 403 -  278B  - /.html
[22:30:38] 403 -  278B  - /.htpasswds
[22:30:38] 403 -  278B  - /.ht_wsr.txt
[22:30:39] 403 -  278B  - /.htpasswd_test
[22:30:39] 403 -  278B  - /.httr-oauth
[22:31:19] 200 -    4KB - /admin/
[22:31:20] 301 -  317B  - /admin  ->  http://10.10.98.83:1337/admin/
[22:31:20] 403 -  278B  - /admin/.htaccess
[22:31:20] 200 -    4KB - /admin/?/login
[22:31:21] 200 -    4KB - /admin/index.html
[22:32:34] 200 -   11KB - /index.html
[22:33:21] 403 -  278B  - /server-status
[22:33:21] 403 -  278B  - /server-status/

>> in ftp one directory is found called pub in which  youfoundme.png image found 
>> after running exiftool on that png image i found a owener of this image.
# Owner Name                      : fijbxslz
>> this is vegenar cipher so deocode the cipher using key=birdistheword as hint give in the youtube song
>> so the real name : easypass

>> in directory .jokesonyou hellon3rd.txt text file is found.
# content of hellon3rd.txt file:
all you need is in the leet

>> then i run enum4linux tool .
# enum4linux -a <IP>

Starting enum4linux v0.8.9 ( http://labs.portcullis.co.uk/application/enum4linux/ ) on Fri Jan 21 22:07:28 2022                                   
                                                                                                                                                  
 ==========================                                                                                                                       
|    Target Information    |                                                                                                                      
 ==========================                                                                                                                       
Target ........... 10.10.98.83                                                                                                                    
RID Range ........ 500-550,1000-1050                                                                                                              
Username ......... ''                                                                                                                             
Password ......... ''                                                                                                                             
Known Usernames .. administrator, guest, krbtgt, domain admins, root, bin, none                                                                   
                                                                                                                                                  
                                                                                                                                                  
 ===================================================                                                                                              
|    Enumerating Workgroup/Domain on 10.10.98.83    |                                                                                             
 ===================================================                                                                                              
[+] Got domain/workgroup name: WORKGROUP                                                                                                          
                                                                                                                                                  
 ===========================================                                                                                                      
|    Nbtstat Information for 10.10.98.83    |                                                                                                     
 =========================================== 
Looking up status of 10.10.98.83
        NERDHERD        <00> -         B <ACTIVE>  Workstation Service
        NERDHERD        <03> -         B <ACTIVE>  Messenger Service
        NERDHERD        <20> -         B <ACTIVE>  File Server Service
        ..__MSBROWSE__. <01> - <GROUP> B <ACTIVE>  Master Browser
        WORKGROUP       <00> - <GROUP> B <ACTIVE>  Domain/Workgroup Name
        WORKGROUP       <1d> -         B <ACTIVE>  Master Browser
        WORKGROUP       <1e> - <GROUP> B <ACTIVE>  Browser Service Elections
                                                                                                                                                  
        MAC Address = 00-00-00-00-00-00

 ==================================== 
|    Session Check on 10.10.98.83    |
 ==================================== 
[+] Server 10.10.98.83 allows sessions using username '', password ''

 ========================================== 
|    Getting domain SID for 10.10.98.83    |
 ========================================== 
Domain Name: WORKGROUP
Domain Sid: (NULL SID)
[+] Can't determine if host is part of domain or part of a workgroup

 ===================================== 
|    OS information on 10.10.98.83    |
 ===================================== 
Use of uninitialized value $os_info in concatenation (.) or string at ./enum4linux.pl line 464.
[+] Got OS info for 10.10.98.83 from smbclient: 
[+] Got OS info for 10.10.98.83 from srvinfo:
        NERDHERD       Wk Sv PrQ Unx NT SNT nerdherd server (Samba, Ubuntu)
        platform_id     :       500
        os version      :       6.1
        server type     :       0x809a03

 ============================ 
|    Users on 10.10.98.83    |
 ============================ 
index: 0x1 RID: 0x3e8 acb: 0x00000010 Account: chuck    Name: ChuckBartowski    Desc: 

user:[chuck] rid:[0x3e8]

 ======================================== 
|    Share Enumeration on 10.10.98.83    |
 ======================================== 

        Sharename       Type      Comment
        ---------       ----      -------
        print$          Disk      Printer Drivers
        nerdherd_classified Disk      Samba on Ubuntu
        IPC$            IPC       IPC Service (nerdherd server (Samba, Ubuntu))
SMB1 disabled -- no workgroup available

[+] Attempting to map shares on 10.10.98.83
//10.10.98.83/print$    Mapping: DENIED, Listing: N/A
//10.10.98.83/nerdherd_classified       Mapping: DENIED, Listing: N/A
//10.10.98.83/IPC$      [E] Can't understand response:
NT_STATUS_OBJECT_NAME_NOT_FOUND listing \*

 =================================================== 
|    Password Policy Information for 10.10.98.83    |
 =================================================== 


[+] Attaching to 10.10.98.83 using a NULL share

[+] Trying protocol 139/SMB...
[+] Found domain(s):

        [+] NERDHERD
        [+] Builtin

[+] Password Info for Domain: NERDHERD

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
Minimum Password Length: 5                                                                                                               [216/902]


 ============================= 
|    Groups on 10.10.98.83    |
 ============================= 

[+] Getting builtin groups:

[+] Getting builtin group memberships:

[+] Getting local groups:

[+] Getting local group memberships: 

[+] Getting domain groups:

[+] Getting domain group memberships:

 ====================================================================== 
|    Users on 10.10.98.83 via RID cycling (RIDS: 500-550,1000-1050)    |
 ====================================================================== 
[I] Found new SID: S-1-22-1
[I] Found new SID: S-1-5-21-2306820301-2176855359-2727674639
[I] Found new SID: S-1-5-32
[+] Enumerating users using SID S-1-22-1 and logon username '', password ''
S-1-22-1-1000 Unix User\chuck (Local User)
S-1-22-1-1002 Unix User\ftpuser (Local User)
[+] Enumerating users using SID S-1-5-21-2306820301-2176855359-2727674639 and logon username '', password ''
S-1-5-21-2306820301-2176855359-2727674639-500 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-500 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-501 NERDHERD\nobody (Local User)
S-1-5-21-2306820301-2176855359-2727674639-502 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-503 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-504 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-505 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-506 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-507 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-508 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-509 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-510 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-511 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-512 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-513 NERDHERD\None (Domain Group)
S-1-5-21-2306820301-2176855359-2727674639-514 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-515 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-516 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-517 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-518 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-519 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-520 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-521 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-522 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-523 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-524 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-525 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-526 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-527 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-528 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-529 *unknown*\*unknown* (8)                                                                    [158/902]
S-1-5-21-2306820301-2176855359-2727674639-530 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-531 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-532 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-533 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-534 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-535 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-536 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-537 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-538 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-539 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-540 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-541 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-542 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-543 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-544 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-545 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-546 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-547 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-548 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-549 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-550 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-1000 NERDHERD\chuck (Local User)
S-1-5-21-2306820301-2176855359-2727674639-1001 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-1002 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-1003 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-1004 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-1005 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-1006 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-1007 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-1008 *unknown*\*unknown* (8)                                                                   [128/902]
S-1-5-21-2306820301-2176855359-2727674639-1009 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-1010 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-1011 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-1012 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-1013 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-1014 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-1015 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-1016 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-1017 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-1018 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-1019 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-1020 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-1021 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-1022 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-1023 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-1024 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-1025 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-1026 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-1027 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-1028 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-1029 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-1030 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-1031 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-1032 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-1033 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-1034 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-1035 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-1036 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-1037 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-1038 *unknown*\*unknown* (8)                                                                    [98/902]
S-1-5-21-2306820301-2176855359-2727674639-1039 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-1040 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-1041 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-1042 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-1043 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-1044 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-1045 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-1046 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-1047 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-1048 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-1049 *unknown*\*unknown* (8)
S-1-5-21-2306820301-2176855359-2727674639-1050 *unknown*\*unknown* (8)
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
S-1-5-32-516 *unknown*\*unknown* (8)                                                                                                      [68/902]
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
S-1-5-32-546 BUILTIN\Guests (Local Group)                                                                                                 [38/902]
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
S-1-5-32-1025 *unknown*\*unknown* (8)                                                                                                      [8/902]
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

 ============================================ 
|    Getting printer info for 10.10.98.83    |
 ============================================ 
 No printers returned.


enum4linux complete on Fri Jan 21 22:37:32 2022

# -> Exploitation Phase:

>> above enumeration give two users
>> 1] chuck : smb
>> 2] ftpuser : ftp

>> then i visit http service on port 1337. default php page is displayed.
>> after visiting display two pops, in which room maker told that somithing  hidden in this page.
>> at bottom there is link of youtube of someone song.
>> then i goto admin directory and login page is displayed.and in the source code two base64 strings are found.

# Y2liYXJ0b3dza2k= : aGVoZWdvdTwdasddHlvdQ==
# cibartowski : hehegou<.jÇ].[ÝD

>> so i username chuck and password easypass and enumerate more through smb
>> and at last i find scre3t.txt file .content of that file is:

Ssssh! don't tell this anyone because you deserved it this far:

	check out "/this1sn0tadirect0ry"

Sincerely,
	0xpr0N3rd
<3

>> go to that directory and found creds.txt file in which ssh cridentials are present.

alright, enough with the games.

here, take my ssh creds:
	
	chuck : th1s41ntmypa5s

>> so lets login into ssh.

# USER.TXT : THM{7fc91d70e22e9b70f98aaf19f9a1c3ca710661be}

# ->PostExploitation Phase:

>> first i found suid permissions binaries and i found pkexec binary and chuck user in the sudo group.
>> pkexec: it is a binary used to execute command of another user by current user.
>> so i exploit it by following:

>> it requires two shells.
>> first find the process id of current session.
# echo $$
--> <Process_id>
>> now run in second shell:
# pkttyagent --porcess <Process_id>
>> now in the first shell run:
# pkexec /bin/bash
>> on second shell:
# password prompt is display : write the password of chuck and press enter
>> at last got a root shell on first shell.

# ROOT.TXT : THM{5c5b7f0a81ac1c00732803adcee4a473cf1be693}

>> bonus flag found in .bash_history file

# bonus.txt : THM{a975c295ddeab5b1a5323df92f61c4cc9fc88207}





