# 2 - The Security Guard

Once in a remote Norwegian town, a group of skilled security professionals had convened in a fancy cabin to collaborate and achieve their objectives. On their network, they found a number of challenges that required their collective expertise. Do you have what it takes to tackle these challenges too?

http://rsxc.no:9006

# Note

Due to my findings in no 3-6 of this challenge the challenge has been updated. So flag is no longer in webroot but in system root. But all writeups still works but the flag seems to be moved to `/flag.txt`

# Writeup

Here I tried the same as last time, `;ls`. Then I got this message: `Illegal Input Discovered`.

Quickly thought they had blocked `;` so I tried the else operator in bash. `|| ls` and there we go. Had to use `||` which runs the following command only if the first fails, which it does due to missing `ping`.

```
flag.txt
index.php
style.css
```

Quickly cat the flag and index.php.

```php
<?php
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $ip = $_POST['ip'];
    
    if (preg_match('/[;`\'"]/',$ip)) {
        echo "<p align='center' style='color:red;'>Illegal Input Discovered</p>";
        die();
    }
    
    $output = shell_exec("ping -c 1 $ip");
    echo "<pre class='output'>$output</pre>";
}
```

This also seems broken with the ping command which might be the point to make the challenge harder?

# Flag 

```
RSXC{SOME_CHARACTERS_ARE_BLOCKED_SOME_ARE_NOT}
```