[*] EVM [*]

# Date : 28/01/2022

# ->Enumeration Phase:

# Nmap 7.91 scan initiated Fri Jan 28 13:51:08 2022 as: nmap -sC -sV -vv -p- -oN nmap_all 192.168.0.107
Nmap scan report for Red.Initech (192.168.0.107)
Host is up, received arp-response (0.00028s latency).
Scanned at 2022-01-28 13:51:09 IST for 23s
Not shown: 65528 closed ports
Reason: 65528 resets
PORT    STATE SERVICE     REASON         VERSION
22/tcp  open  ssh         syn-ack ttl 64 OpenSSH 7.2p2 Ubuntu 4ubuntu2.2 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 a2:d3:34:13:62:b1:18:a3:dd:db:35:c5:5a:b7:c0:78 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC0defjjR1wkIrdUKeTlYiEG2/PwOaaBSPs+pp11hljbqRiUim5Kkf5QCQXS5SsQE2ljdKAVzFbdIgwtGc1TPp1UAgi55uGyzuZMGDN5vItwvzzZxcrkS9CuH9NeBQh52Ak6Ki5gsgUf/odg90om62mSVX43mLP4v9nk51qnTc2InstJF37GXqGl05RaGjnramVbP/7vLTX5ondW0hfnwFjtsjkT8w1itwI/dGL/4tMnw+khj5BnTFOTxxC0S+tPlY3dE+jM31i2ftpEB5jOD74Fxeng6JF1/8fQi8o+9EeJcMUUs8fd9ygw1BNwzCU7gGCysz6yH62ENKApjO/WX+r
|   256 85:48:53:2a:50:c5:a0:b7:1a:ee:a4:d8:12:8e:1c:ce (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBGbko+cI1o2lFazvX9zJXiqPBgUYyd110OTvgudv/xMdK7IIJkskJ/kVm6XHHre472oDWrmxJRQfTnOS1EgJbTY=
|   256 36:22:92:c7:32:22:e3:34:51:bc:0e:74:9f:1c:db:aa (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAILux3BHKEWIkPrmFBz8ag3x3ZZBF638RTPw3GJ+ynllV
53/tcp  open  domain      syn-ack ttl 64 ISC BIND 9.10.3-P4 (Ubuntu Linux)
| dns-nsid: 
|_  bind.version: 9.10.3-P4-Ubuntu
80/tcp  open  http        syn-ack ttl 64 Apache httpd 2.4.18 ((Ubuntu))
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
110/tcp open  pop3        syn-ack ttl 64 Dovecot pop3d
|_pop3-capabilities: TOP RESP-CODES CAPA PIPELINING SASL AUTH-RESP-CODE UIDL
139/tcp open  netbios-ssn syn-ack ttl 64 Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
143/tcp open  imap        syn-ack ttl 64 Dovecot imapd
|_imap-capabilities: ENABLE have LITERAL+ SASL-IR Pre-login LOGINDISABLEDA0001 post-login listed more OK capabilities IDLE ID IMAP4rev1 LOGIN-REFERRALS
445/tcp open  netbios-ssn syn-ack ttl 64 Samba smbd 4.3.11-Ubuntu (workgroup: WORKGROUP)
MAC Address: 08:00:27:58:A8:FF (Oracle VirtualBox virtual NIC)
Service Info: Host: UBUNTU-EXTERMELY-VULNERABLE-M4CH1INE; OS: Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
|_clock-skew: mean: 1h40m05s, deviation: 2h53m12s, median: 4s
| nbstat: NetBIOS name: UBUNTU-EXTERMEL, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
| Names:
|   UBUNTU-EXTERMEL<00>  Flags: <unique><active>
|   UBUNTU-EXTERMEL<03>  Flags: <unique><active>
|   UBUNTU-EXTERMEL<20>  Flags: <unique><active>
|   WORKGROUP<00>        Flags: <group><active>
|   WORKGROUP<1e>        Flags: <group><active>
| Statistics:
|   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
|   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
|_  00 00 00 00 00 00 00 00 00 00 00 00 00 00
| p2p-conficker: 
|   Checking for Conficker.C or higher...
|   Check 1 (port 36000/tcp): CLEAN (Couldn't connect)
|   Check 2 (port 50829/tcp): CLEAN (Couldn't connect)
|   Check 3 (port 33023/udp): CLEAN (Failed to receive data)
|   Check 4 (port 64559/udp): CLEAN (Failed to receive data)
|_  0/4 checks are positive: Host is CLEAN or ports are blocked
| smb-os-discovery: 
|   OS: Windows 6.1 (Samba 4.3.11-Ubuntu)
|   Computer name: ubuntu-extermely-vulnerable-m4ch1ine
|   NetBIOS computer name: UBUNTU-EXTERMELY-VULNERABLE-M4CH1INE\x00
|   Domain name: \x00
|   FQDN: ubuntu-extermely-vulnerable-m4ch1ine
|_  System time: 2022-01-28T03:21:29-05:00
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2022-01-28T08:21:29
|_  start_date: N/A

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Fri Jan 28 13:51:32 2022 -- 1 IP address (1 host up) scanned in 24.60 seconds


# Enum4linux found :
    ->>  S-1-22-1-1000 Unix User\rooter (Local User)

# Gobuster found :
    ->> /wordpress            (Status: 301) [Size: 318] [--> http://192.168.0.107/wordpress/]
        /server-status        (Status: 403) [Size: 301] 

# ->Exploitaion Phase:

# wpscan found :

    ->> wpscan --url http://192.168.0.107/wordpress --enumerate u p --plugins-detection aggressive
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

    [+] URL: http://192.168.0.107/wordpress/ [192.168.0.107]
    [+] Started: Fri Jan 28 14:02:55 2022

    Interesting Finding(s):

    [+] Headers
    | Interesting Entry: Server: Apache/2.4.18 (Ubuntu)
    | Found By: Headers (Passive Detection)
    | Confidence: 100%

    [+] XML-RPC seems to be enabled: http://192.168.0.107/wordpress/xmlrpc.php
    | Found By: Direct Access (Aggressive Detection)
    | Confidence: 100%
    | References:
    |  - http://codex.wordpress.org/XML-RPC_Pingback_API
    |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_ghost_scanner
    |  - https://www.rapid7.com/db/modules/auxiliary/dos/http/wordpress_xmlrpc_dos
    |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_xmlrpc_login
    |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_pingback_access

    [+] WordPress readme found: http://192.168.0.107/wordpress/readme.html
    | Found By: Direct Access (Aggressive Detection)
    | Confidence: 100%

    [+] Upload directory has listing enabled: http://192.168.0.107/wordpress/wp-content/uploads/
    | Found By: Direct Access (Aggressive Detection)
    | Confidence: 100%

    [+] The external WP-Cron seems to be enabled: http://192.168.0.107/wordpress/wp-cron.php
    | Found By: Direct Access (Aggressive Detection)
    | Confidence: 60%
    | References:
    |  - https://www.iplocation.net/defend-wordpress-from-ddos
    |  - https://github.com/wpscanteam/wpscan/issues/1299

    [+] WordPress version 5.2.4 identified (Insecure, released on 2019-10-14).
    | Found By: Emoji Settings (Passive Detection)
    |  - http://192.168.0.107/wordpress/, Match: 'wp-includes\/js\/wp-emoji-release.min.js?ver=5.2.4'
    | Confirmed By: Meta Generator (Passive Detection)
    |  - http://192.168.0.107/wordpress/, Match: 'WordPress 5.2.4'

    [i] The main theme could not be detected.

    [+] Enumerating Users (via Passive and Aggressive Methods)
    Brute Forcing Author IDs - Time: 00:00:00 <================================================================================> (10 / 10) 100.00% Time: 00:00:00

    [i] User(s) Identified:

    [+] c0rrupt3d_brain
    | Found By: Author Id Brute Forcing - Author Pattern (Aggressive Detection)
    | Confirmed By: Login Error Messages (Aggressive Detection)

    [!] No WPScan API Token given, as a result vulnerability data has not been output.
    [!] You can get a free API token with 50 daily requests by registering at https://wpscan.com/register

    [+] Finished: Fri Jan 28 14:03:57 2022
    [+] Requests Done: 48
    [+] Cached Requests: 4
    [+] Data Sent: 12.007 KB
    [+] Data Received: 89.265 KB
    [+] Memory used: 150.875 MB
    [+] Elapsed time: 00:01:02

    # wpscan bruteforce the password of wordpress user:

    [!] Valid Combinations Found:
    | Username: c0rrupt3d_brain, Password: 24992499

>> Then use metasploit module : exploit/unix/webapp/wp_admin_shell_upload

# PostExploitation Phase:

# wp-config.php file found:
    ->>
    /** The name of the database for WordPress */
    define( 'DB_NAME', 'hackme_wp' );

    /** MySQL database username */
    define( 'DB_USER', 'root' );

    /** MySQL database password */
    define( 'DB_PASSWORD', '123' );

    /** MySQL hostname */
    define( 'DB_HOST', 'localhost' );

    /** Database Charset to use in creating database tables. */
    define( 'DB_CHARSET', 'utf8' );

    /** The Database Collate type. Don't change this if in doubt. */
    define( 'DB_COLLATE', '' );

>> Nothing found in mysql databases.
>> in directory /home/root3r/ ".root_password_ssh.txt" file is found containing password of root.

# Root Password : willy26

# Proof.txt :

voila you have successfully pwned me :) !!!
:D

 

