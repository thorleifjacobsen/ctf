# Admin (beginner)

Can you get the flag?

Author: martcl

http://20.100.136.71:1027/

# Writeup

I met a website with a link saying `Get the flag`. Pressing it gives me a new site saying `You are not the admin!`. Opening the inspector I see a cookie named `admin`.

![cookie.png](cookie.png)

Changing the value to `true` and I get the flag:

![cookie_changed](cookie_changed.png)

# Flag 

```
wack{you_are_the_captain_now!}
```