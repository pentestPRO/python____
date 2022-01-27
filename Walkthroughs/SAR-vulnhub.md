[*] SAR [*]

# Date : 27/01/2022

# ->Enumeration Phase:

# Nmap 7.91 scan initiated Thu Jan 27 15:53:54 2022 as: nmap -sC -sV -vv -p- -oN nmap_all 192.168.0.102
Nmap scan report for 192.168.0.102
Host is up, received arp-response (0.00032s latency).
Scanned at 2022-01-27 15:53:55 IST for 11s
Not shown: 65534 closed ports
Reason: 65534 resets
PORT   STATE SERVICE REASON         VERSION
80/tcp open  http    syn-ack ttl 64 Apache httpd 2.4.29 ((Ubuntu))
| http-methods: 
|_  Supported Methods: GET POST OPTIONS HEAD
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
MAC Address: 08:00:27:20:73:1D (Oracle VirtualBox virtual NIC)

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Thu Jan 27 15:54:06 2022 -- 1 IP address (1 host up) scanned in 12.08 seconds


>> robots.txt file is found.
    ->> sar2HTML 
        ->> Hint : sar2HTML vulnerbility

# ->Exploitation Phase:

>> searchsploit sar2HTML 
    ->> sar2html 3.2.1 - 'plot' Remote Code Execution      | php/webapps/49344.py
        Sar2HTML 3.2.1 - Remote Command Execution          | php/webapps/47204.txt

# user.txt : 427a7e47deb4a8649c7cab38df232b52

# ->PostExploitation Phase:

>> cronjob is running . every 5 min  'finally.sh' file run as a root user. and this script execute another script having writable permissions.
>> so change the content of 'write.sh' file with the reverse shell and after 5 min obtain a root shell.

# root.txt : 66f93d6b2ca96c9ad78a8a9ba0008e99

